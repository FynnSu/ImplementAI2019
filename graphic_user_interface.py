# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:34:04 2019

@author: Alex Trottier
"""

import wx 
  
#import the newly created GUI file 
import gui_frame  

# About the window for new action
class startframe(gui_frame.frame_start): 
   def __init__(self,parent):
       gui_frame.frame_start.__init__(self,parent)  
		
   def getout(self,event):
       if 1 < 2: ##############LOOK IF FILES TO ERASE
           nextWindow = eraseframe(None)
       else:
           nextWindow = bodyframe(None)
       nextWindow.Show()
       self.Close()
       
class eraseframe(gui_frame.frame_erase):
    def __init__(self,parent):
       gui_frame.frame_erase.__init__(self,parent)
    
    def erasefiles(self, event):
        #############ADD ERASER!
        nextWindow = bodyframe(None)
        nextWindow.Show()
        self.Close()
        
    def keepfiles(self, event):
        nextWindow = bodyframe(None)
        nextWindow.Show()
        self.Close()

class bodyframe(gui_frame.frame_body):
    def __init__(self,parent):
       gui_frame.frame_body.__init__(self,parent)
       
    def runanalysis(self, event):
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
        
        print "Selected:", body_list
        #self.Close() ###### put back and remove the print
        ##### Add stuff to run the recording
        




app = wx.App(False) 
frame = startframe(None) 
frame.Show(True) 
#start the applications 
app.MainLoop() 