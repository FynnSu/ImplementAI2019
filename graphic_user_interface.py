# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:34:04 2019

@author: Alex Trottier
"""

from __future__ import print_function, division

import wx 
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
  
#import the newly created GUI file 
import gui_frame  

# About the window for new action
class startframe(gui_frame.frame_start): 
   def __init__(self,parent):
       gui_frame.frame_start.__init__(self,parent)  
		
   def getout(self,event):
       if os.path.isfile(sys.argv[2]):
           nextWindow = eraseframe(None)
       else:
           nextWindow = bodyframe(None)
       nextWindow.Show()
       self.Close()
       
class eraseframe(gui_frame.frame_erase):
    def __init__(self,parent):
       gui_frame.frame_erase.__init__(self,parent)
    
    def erasefiles(self, event):
        nextWindow = bodyframe(None)
        nextWindow.Show()
        global actions
        actions = []
        self.Close()
        
    def keepfiles(self, event):
        with open(sys.argv[2], 'rb') as f:
            global actions
            actions = pickle.load(f)
        nextWindow = bodyframe(None)
        nextWindow.Show()
        self.Close()

class bodyframe(gui_frame.frame_body):
    def __init__(self,parent):
        with open("joints_id.csv", 'r') as fp:
            body_table = from_csv(fp)
            print(body_table)
        gui_frame.frame_body.__init__(self,parent)
       
    def runanalysis(self, event):
        global body_list
        body_list =[]
        if self.b0.GetValue():
            body_list.append(0)
        if self.b1.GetValue():
            body_list.append(1)
        if self.b2.GetValue():
            body_list.append(2)
        if self.b3.GetValue():
            body_list.append(3)
        if self.b4.GetValue():
            body_list.append(4)
        if self.b5.GetValue():
            body_list.append(5)
        if self.b6.GetValue():
            body_list.append(6)
        if self.b7.GetValue():
            body_list.append(7)
        if self.b8.GetValue():
            body_list.append(8)
        if self.b9.GetValue():
            body_list.append(9)
        if self.b10.GetValue():
            body_list.append(10)
        if self.b11.GetValue():
            body_list.append(11)
        if self.b12.GetValue():
            body_list.append(12)
        if self.b13.GetValue():
            body_list.append(13)
        if self.b14.GetValue():
            body_list.append(14)
        if self.b15.GetValue():
            body_list.append(15)
        
        print ("Selected:", body_list)

        global joints
        joints = get_pose(body_list, webcam_index, estimator, visualizer, bone_pairs, options)

        visualizer.draw_lines(joints, bone_pairs)
        visualizer.draw_points(get_joints(joints, body_list), colour=(127.0,255.0,0.0))
        visualizer.show()
        #self.Close() ###### put back and remove the print
        ##### Add stuff to run the recording
        nextWindow = keyframe(None)
        nextWindow.Show()
        self.Close()


class keyframe(gui_frame.frame_key):

    def __init__(self,parent):
       gui_frame.frame_key.__init__(self,parent)
    
    def recordKey(self, event):
        global key_value
        key_value = self.key_input.GetValue()
        print ("print that:", key_value)
        
        nextWindow = confirmframe(None)
        nextWindow.Show()
        self.Close()


class confirmframe(gui_frame.frame_confirm):
    def __init__(self,parent):
       gui_frame.frame_confirm.__init__(self,parent)
    
    def confirmYes(self, event):
        
        # DO whatever if want recording
        actions.append([key_value, body_list, joints])
        
        with open(sys.argv[2], 'wb') as fp:
            pickle.dump(actions, fp)
        cv2.destroyAllWindows()
        nextWindow = startframe(None)
        nextWindow.Show()
        self.Close()
        
    def confirmNo(self, event):
        
        # do stuff if you DONT want recording
        
        with open(sys.argv[2], 'wb') as fp:
            pickle.dump(actions, fp)
        cv2.destroyAllWindows()
        nextWindow = startframe(None)
        nextWindow.Show()
        self.Close()
        


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

while(True):
    app = wx.App(False) 
    frame = startframe(None) 
    frame.Show(True) 
    #start the applications 
    app.MainLoop()