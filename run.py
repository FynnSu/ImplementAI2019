from __future__ import print_function, division

import sys
import cv2
import wrnchAI
import pickle
from visualizer import Visualizer
from pynput.keyboard import Key, Controller
import numpy as np
import os

REFERENCE_JOINTS = [14,15]
DIFFERENCE_THRESHOLD = 0.1

SPECIAL_KEYS = {"left":Key.left, "right":Key.right, "up":Key.up, "down":Key.down, "space":Key.space}

def get_pose():
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
            for human in humans2d:
                joints = human.joints()

                visualizer.draw_points(joints)
                visualizer.draw_lines(joints, bone_pairs)

            visualizer.show()

        key = cv2.waitKey(1)
        # print(key)

        if key & 255 == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    return joints

def do_action(keyboard, key):
    if key in SPECIAL_KEYS.keys():
        keyboard.press(SPECIAL_KEYS[key])
    else:
        keyboard.press(key)

def difference(old_joints, new_joints, imp_joints):
    diff = np.subtract(old_joints, new_joints)
    squared = np.square(diff)
    return np.sum(squared[np.repeat(imp_joints, 2) + np.repeat((0,1), len(imp_joints))])

num_args = len(sys.argv)
if num_args < 3 or num_args > 4:
    sys.exit("Usage: python run.py MODEL_DIR/ ACTION_FILE camera_index")

if num_args == 4:
    webcam_index = int(sys.argv[3])
else:
    webcam_index = 0

params = wrnchAI.PoseParams()
params.bone_sensitivity = wrnchAI.Sensitivity.high
params.joint_sensitivity = wrnchAI.Sensitivity.high
params.enable_tracking = True

params.preferred_net_height = 194
params.preferred_net_width = 328

output_format = wrnchAI.JointDefinitionRegistry.get('j25')

print('Initializing networks...')
estimator = wrnchAI.PoseEstimator(
    models_path=sys.argv[1], params=params, gpu_id=0, output_format=output_format)
print('Initialization Done!')

options = wrnchAI.PoseEstimatorOptions()

print('Opening webcam...')
cap = cv2.VideoCapture(webcam_index)

joint_definition = estimator.human_2d_output_format()
bone_pairs = joint_definition.bone_pairs()
visualizer = Visualizer()

if not os.path.isfile(sys.argv[2]):
    print('Saved Actions File not found')

with open(sys.argv[2], 'rb') as f:
    saved_actions = pickle.load(f)
    print(saved_actions)

keyboard = Controller()

while True:
    ret, frame = cap.read()

    if frame is not None:
        estimator.process_frame(frame, options)
        humans2d = estimator.humans_2d()
        visualizer.draw_image(frame)

        # Check for main person
        for human in humans2d:
            joints = human.joints()
            visualizer.draw_points(joints)
            visualizer.draw_lines(joints, bone_pairs)

            joints = joints - np.tile(joints[REFERENCE_JOINTS], int(len(joints) / 2))

            for i in range(len(saved_actions)):
                key, indices, joints_pos = saved_actions[i]
                # print(key, indices, joints_pos)
                error = difference(joints_pos, joints, indices)
                print(error)
                if error < DIFFERENCE_THRESHOLD:
                    do_action(keyboard, key)
                    
        visualizer.show()
    key = cv2.waitKey(1)

    if key & 255 == 27:
        break

cap.release()
cv2.destroyAllWindows()
        




