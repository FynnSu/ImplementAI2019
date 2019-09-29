from __future__ import print_function, division

import sys
import cv2
import wrnchAI
import pickle
import os
from visualizer import Visualizer
from prettytable import from_csv
from matplotlib import pyplot as plt
from utils import get_joints, get_pose
import numpy as np

num_args = len(sys.argv)
if num_args < 3 or num_args > 4:
    sys.exit("Usage: python define_actions.py MODEL_DIR/ ACTION_FILE camera_index")

if num_args == 4:
    webcam_index = int(sys.argv[3])
else:
    webcam_index = 0

params = wrnchAI.PoseParams()
params.bone_sensitivity = wrnchAI.Sensitivity.high
params.joint_sensitivity = wrnchAI.Sensitivity.high
params.enable_tracking = True

# Default Model resolution
params.preferred_net_width = 328
params.preferred_net_height = 184

output_format = wrnchAI.JointDefinitionRegistry.get('j25')

print('Initializing networks...')
estimator = wrnchAI.PoseEstimator(
    models_path=sys.argv[1], params=params, gpu_id=0, output_format=output_format)
print('Initialization done!')

options = wrnchAI.PoseEstimatorOptions()

visualizer = Visualizer()

joint_definition = estimator.human_2d_output_format()
bone_pairs = joint_definition.bone_pairs()

actions = []

if os.path.isfile(sys.argv[2]):
    with open(sys.argv[2], 'rb') as f:
        # look into properties of picked later
        saved_actions = pickle.load(f)

    if input('Would you like to keep the ' + str(len(saved_actions)) + ' existing actions: (yes/y)') in ['yes', 'y']:
        actions = saved_actions

with open("joints_id.csv", 'r') as fp:
    body_table = from_csv(fp)

while True:
    print(body_table)
    bodyparts = input("Please enter the ID number of what you will move (separated by space):")
    bodyparts = list(map(int, bodyparts))

    redo = "yes"
    while redo in ['yes', 'y']:
        joints = get_pose(bodyparts, webcam_index, estimator, visualizer, bone_pairs, options)

        visualizer.draw_lines(joints, bone_pairs)
        visualizer.draw_points(get_joints(joints, bodyparts), colour=(127.0,255.0,0.0))
        visualizer.show()

        redo = input("Redo snapshot? (yes/y)")

    
    action = input('Enter a key or "left", "right", "up", "down", "space"')

    add = input("Would you like to add the action \""+ action + "\" with joints " + str(bodyparts) + " to the list of actions? (yes/y)")
    
    cv2.destroyAllWindows()

    if add in ['yes','y']:
        actions.append([action, bodyparts, joints])

    if input("Would you like to create a new action? (yes/y)") not in ['yes', 'y']:
        break

with open(sys.argv[2], 'wb') as fp:
    pickle.dump(actions, fp)





