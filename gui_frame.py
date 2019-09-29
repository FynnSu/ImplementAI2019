# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frame_start
###########################################################################

class frame_start ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"starting_box" ), wx.VERTICAL )
		
		sbSizer3.SetMinSize( wx.Size( 200,200 ) ) 
		self.starting_text = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Do you want to record an action?", wx.Point( 100,-1 ), wx.DefaultSize, wx.ALIGN_CENTRE )
		self.starting_text.Wrap( -1 )
		sbSizer3.Add( self.starting_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_start = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Yes", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.button_start, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_start.Bind( wx.EVT_BUTTON, self.getout )
		self.button_start.Bind( wx.EVT_LEAVE_WINDOW, self.button_startOnLeaveWindow )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def getout( self, event ):
		event.Skip()
	
	def button_startOnLeaveWindow( self, event ):
		event.Skip()
	

###########################################################################
## Class frame_erase
###########################################################################

class frame_erase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"starting_box" ), wx.VERTICAL )
		
		sbSizer3.SetMinSize( wx.Size( 200,200 ) ) 
		self.erase_text = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"There are already files recorded, do you want to delete these?", wx.Point( 100,-1 ), wx.DefaultSize, wx.ALIGN_CENTRE )
		self.erase_text.Wrap( -1 )
		sbSizer3.Add( self.erase_text, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.button_erase = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Yes, erase these", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.button_erase, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )
		
		self.button_pass = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"No, keep everything", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.button_pass, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( sbSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.button_erase.Bind( wx.EVT_BUTTON, self.erasefiles )
		self.button_erase.Bind( wx.EVT_LEAVE_WINDOW, self.button_startOnLeaveWindow )
		self.button_pass.Bind( wx.EVT_BUTTON, self.keepfiles )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def erasefiles( self, event ):
		event.Skip()
	
	def button_startOnLeaveWindow( self, event ):
		event.Skip()
	
	def keepfiles( self, event ):
		event.Skip()
	

###########################################################################
## Class frame_body
###########################################################################

class frame_body ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 673,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer3 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Select body parts you will move (at least 2)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer3.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer3.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.b0 = wx.CheckBox( self, wx.ID_ANY, u"Right Ankle", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b0, 0, wx.ALL, 5 )
		
		self.b1 = wx.CheckBox( self, wx.ID_ANY, u"Right Knee", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b1, 0, wx.ALL, 5 )
		
		self.b2 = wx.CheckBox( self, wx.ID_ANY, u"Right Hip", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b2, 0, wx.ALL, 5 )
		
		self.b3 = wx.CheckBox( self, wx.ID_ANY, u"Left Hip", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b3, 0, wx.ALL, 5 )
		
		self.b4 = wx.CheckBox( self, wx.ID_ANY, u"Left Knee", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b4, 0, wx.ALL, 5 )
		
		self.b5 = wx.CheckBox( self, wx.ID_ANY, u"Left Ankle", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b5, 0, wx.ALL, 5 )
		
		self.b6 = wx.CheckBox( self, wx.ID_ANY, u"Pelvis", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b6, 0, wx.ALL, 5 )
		
		self.b7 = wx.CheckBox( self, wx.ID_ANY, u"Thorax", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b7, 0, wx.ALL, 5 )
		
		self.b8 = wx.CheckBox( self, wx.ID_ANY, u"Neck", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b8, 0, wx.ALL, 5 )
		
		self.b9 = wx.CheckBox( self, wx.ID_ANY, u"Head", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b9, 0, wx.ALL, 5 )
		
		self.b10 = wx.CheckBox( self, wx.ID_ANY, u"Right Wrist", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b10, 0, wx.ALL, 5 )
		
		self.b11 = wx.CheckBox( self, wx.ID_ANY, u"Right Elbow", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b11, 0, wx.ALL, 5 )
		
		self.b12 = wx.CheckBox( self, wx.ID_ANY, u"Right Shoulder", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b12, 0, wx.ALL, 5 )
		
		self.b13 = wx.CheckBox( self, wx.ID_ANY, u"Left Shoulder", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b13, 0, wx.ALL, 5 )
		
		self.b14 = wx.CheckBox( self, wx.ID_ANY, u"Left Elbow", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b14, 0, wx.ALL, 5 )
		
		self.b15 = wx.CheckBox( self, wx.ID_ANY, u"Left Wrist", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.b15, 0, wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer3.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.runButton = wx.Button( self, wx.ID_ANY, u"Ready to take the pose", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer3.Add( self.runButton, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.runButton.Bind( wx.EVT_BUTTON, self.runanalysis )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def runanalysis( self, event ):
		event.Skip()
	

