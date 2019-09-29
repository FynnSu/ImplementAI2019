import sys
import cv2
import wrnchAI
import pickle
from visualizer import Visualizer
from pynput.keyboard import Key, Controller
import numpy as np
import os

SPECIAL_KEYS = {"left":Key.left, "right":Key.right, "up":Key.up, "down":Key.down, "space":Key.space}

def find_largest(humans_list):
    max_ind = 0
    max_height = 0
    for idx, human in enumerate(humans_list):
        joints = human.joints()
        height = get_joints(joints, [8])[1] - get_joints(joints, [6])[1]
        if height > max_height:
            max_height = height
            max_ind = idx
    return max_ind

def get_pose(joint_numbers, webcam_index, estimator, visualizer, bone_pairs, options):
    print('Opening webcam...')
    cap = cv2.VideoCapture(webcam_index)

    if not cap.isOpened():
        sys.exit('Cannot open webcam.')

    for i in range(10):

        ret, frame = cap.read()

        if frame is not None:
            estimator.process_frame(frame, options)
            humans2d = estimator.humans_2d()

            visualizer.draw_image(frame)

            human = humans2d[find_largest(humans2d)]
            joints = human.joints()

            other_numbers = []
            for x in range(int(len(joints) / 2)):
                if x not in joint_numbers:
                    other_numbers.append(x)
            visualizer.draw_points(get_joints(joints, other_numbers))
            visualizer.draw_lines(joints, bone_pairs)
            visualizer.draw_points(get_joints(joints, joint_numbers), colour=(127.0,255.0,0.0))

            visualizer.show()

        key = cv2.waitKey(1)
        # print(key)

        if key & 255 == 27:
            break

    cap.release()
    return normalize(joints)

def normalize(joints):
    center = get_joints(joints, [8])
    height = center[1] - get_joints(joints, [6])[1]
    if height != 0:
        new_joints = (joints - np.tile(center, int(len(joints) / 2))) / height
    else:
        new_joints = (joints - np.tile(center, int(len(joints) / 2))) / 0.01
    return new_joints

def get_joints(joints, indices):
    cor_indices = np.repeat(indices, 2) * 2 + np.tile([0,1], len(indices))
    return joints[cor_indices]

    
def difference(old_joints, new_joints, imp_joints):
    # # diff = np.zeros(len(imp_joints))
    # old_diff = []
    # new_diff = []
    # # comparison of differences from head location x and y coordinates
    # for joint in imp_joints:
    #     old_diff.append(old_joints[joint] - old_joints[8])
    #     old_diff.append(old_joints[joint + 1] - old_joints[8])
    #     new_diff.append(new_joints[joint] - new_joints[8])
    #     new_diff.append(new_joints[joint + 1] - new_joints[8])
    # Diff_Score = 0
    # for index, coordinate_diff in enumerate(new_diff):
    #     if not (0.83*old_diff[index]) < coordinate_diff < (1.17*old_diff[index]):
    #         Diff_Score += coordinate_diff**2
    # return Diff_Score
    # print(type(old_joints), type(new_joints))
    sub = old_joints - new_joints
    diff = get_joints(sub, imp_joints)
    return np.sqrt(np.sum(np.square(diff)))

def do_action(keyboard, key):
    if key in SPECIAL_KEYS.keys():
        keyboard.press(SPECIAL_KEYS[key])
    else:
        keyboard.press(key)