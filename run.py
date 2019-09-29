from __future__ import print_function, division

import sys
import cv2
import wrnchAI
import pickle
from visualizer import Visualizer
from pynput.keyboard import Key, Controller
import numpy as np
import os
from utils import do_action, find_largest, get_joints, normalize, difference

DIFFERENCE_THRESHOLD = 0.75

print('Start')
num_args = len(sys.argv)
if num_args < 4 or num_args > 5:
    sys.exit("Usage: python run.py MODEL_DIR/ ACTION_FILE camera_index")

if num_args == 5:
    webcam_index = int(sys.argv[4])
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

run_last = [False] * len(saved_actions)

while True:
    ret, frame = cap.read()

    if frame is not None:
        estimator.process_frame(frame, options)
        humans2d = estimator.humans_2d()
        visualizer.draw_image(frame)

        # Check for main person
        if len(humans2d) > 0:
            human = humans2d[find_largest(humans2d)]
            joints = human.joints()
            visualizer.draw_points(joints)
            visualizer.draw_lines(joints, bone_pairs)

            norm_joints = normalize(joints)

            for i in range(len(saved_actions)):
                key, indices, joints_pos = saved_actions[i]
                # print(key, indices, joints_pos)
                error = difference(joints_pos, norm_joints, indices)
                print(key, error)
                if abs(error) < DIFFERENCE_THRESHOLD:
                    if (sys.argv[3] in ["-r", "-R"]) or (not run_last[i]):
                        do_action(keyboard, key)
                        run_last[i] = True
                else:
                    run_last[i] = False

            visualizer.show()
    key = cv2.waitKey(1)

    if key & 255 == 27:
        break

cap.release()
cv2.destroyAllWindows()
