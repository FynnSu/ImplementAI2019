from __future__ import print_function, division

import sys
import cv2 
import wrnchAI
from pynput.keyboard import Key, Controller

num_args = len(sys.argv)
if num_args < 2 or num_args > 3:
    sys.exit("Usage: python pos")

if num_args == 3:
    webcam_index = int(sys.argv[2])
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

print('Opening webcam...')
cap = cv2.VideoCapture(webcam_index)


joint_definition = estimator.human_2d_output_format()
bone_pairs = joint_definition.bone_pairs()

keyboard = Controller()

while True:
    ret, frame = cap.read()

    if frame is not None:
        estimator.process_frame(frame, options)
        humans2d = estimator.humans_2d()

        for human in humans2d:
            joints = human.joints()

            width = frame.shape[1]
            height = frame.shape[0]

            #print(joints[20:24])
            x_rh = joints[20] * width 
            y_rh = joints[21] * height
            x_re = joints[22] * width
            y_re = joints[23] * height            

            slope = (y_rh - y_re) / (x_rh - x_re)

            if abs(slope) < 0.5:
                if x_rh - x_re >= 0:
                    print(slope, "Arm Right")
                    keyboard.press(Key.left)
                elif x_rh - x_re < 0:
                    print(slope, "Arm Left")
                    keyboard.press(Key.right)
            elif y_rh - y_re <= 0:
                print(slope, "Arm Up")
                keyboard.press(Key.up)
            elif y_rh - y_re > 0:
                print(slope, "Arm Down")
                keyboard.press(Key.down)


    key = cv2.waitKey(1)
    print(key)

    if key & 255 == 27:
        break

cap.release()
cv2.destroyAllWindows()