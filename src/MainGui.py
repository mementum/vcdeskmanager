# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Apr 10 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Visualchart Desktop Manager", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer19 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer16 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Desktop 1" ), wx.VERTICAL )
		
		self.m_filePickerDesk1 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.vcw", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		sbSizer9.Add( self.m_filePickerDesk1, 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 5 )
		
		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText7 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer21.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_staticTextDesk1 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextDesk1.Wrap( -1 )
		bSizer21.Add( self.m_staticTextDesk1, 1, wx.ALL, 5 )
		
		
		sbSizer9.Add( bSizer21, 0, wx.EXPAND, 5 )
		
		m_listBoxDesk1Choices = []
		self.m_listBoxDesk1 = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,300 ), m_listBoxDesk1Choices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED )
		sbSizer9.Add( self.m_listBoxDesk1, 1, wx.EXPAND, 5 )
		
		bSizer25 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button15 = wx.Button( self.m_panel1, wx.ID_ANY, u"Delete", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button15, 0, wx.ALL, 5 )
		
		self.m_button33 = wx.Button( self.m_panel1, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer25.Add( self.m_button33, 0, wx.ALL, 5 )
		
		
		sbSizer9.Add( bSizer25, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBoxShowSpecialPages1 = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Show Special Pages", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer9.Add( self.m_checkBoxShowSpecialPages1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer16.Add( sbSizer9, 1, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer16, 1, wx.EXPAND, 5 )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button14 = wx.Button( self.m_panel1, wx.ID_ANY, u"About", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button14, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		bSizer17.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_button91 = wx.Button( self.m_panel1, wx.ID_ANY, u"Copy selected ->", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button91, 0, wx.ALL, 5 )
		
		self.m_button911 = wx.Button( self.m_panel1, wx.ID_ANY, u"Copy all ->>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button911, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button9 = wx.Button( self.m_panel1, wx.ID_ANY, u"Move selected ->", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button9, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button11 = wx.Button( self.m_panel1, wx.ID_ANY, u"Move all ->>", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticline10 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer17.Add( self.m_staticline10, 0, wx.EXPAND|wx.RIGHT|wx.LEFT, 5 )
		
		self.m_button10 = wx.Button( self.m_panel1, wx.ID_ANY, u"<- Move selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button10, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button12 = wx.Button( self.m_panel1, wx.ID_ANY, u"<<- Move all", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button12, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button101 = wx.Button( self.m_panel1, wx.ID_ANY, u"<- Copy selected", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button101, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_button1011 = wx.Button( self.m_panel1, wx.ID_ANY, u"<<- Copy all", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer17.Add( self.m_button1011, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer17.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer17, 0, wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer18 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer91 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Desktop 2" ), wx.VERTICAL )
		
		self.m_filePickerDesk2 = wx.FilePickerCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.vcw", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL )
		sbSizer91.Add( self.m_filePickerDesk2, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 5 )
		
		bSizer211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText71 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		bSizer211.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		self.m_staticTextDesk2 = wx.StaticText( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT|wx.ST_NO_AUTORESIZE )
		self.m_staticTextDesk2.Wrap( -1 )
		bSizer211.Add( self.m_staticTextDesk2, 1, wx.ALL, 5 )
		
		
		sbSizer91.Add( bSizer211, 0, wx.EXPAND, 5 )
		
		m_listBoxDesk2Choices = []
		self.m_listBoxDesk2 = wx.ListBox( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,300 ), m_listBoxDesk2Choices, wx.LB_ALWAYS_SB|wx.LB_EXTENDED )
		sbSizer91.Add( self.m_listBoxDesk2, 1, wx.EXPAND, 5 )
		
		bSizer251 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button151 = wx.Button( self.m_panel1, wx.ID_ANY, u"Edit ...", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button151.Enable( False )
		
		bSizer251.Add( self.m_button151, 0, wx.ALL, 5 )
		
		
		sbSizer91.Add( bSizer251, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer18.Add( sbSizer91, 1, wx.EXPAND, 5 )
		
		
		bSizer19.Add( bSizer18, 1, wx.EXPAND, 5 )
		
		
		bSizer15.Add( bSizer19, 1, wx.EXPAND, 5 )
		
		self.m_staticline11 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer15.Add( self.m_staticline11, 0, wx.EXPAND|wx.TOP|wx.RIGHT|wx.LEFT, 5 )
		
		bSizer20 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_button13 = wx.Button( self.m_panel1, wx.ID_ANY, u"Exit", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer15.Add( bSizer20, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer15 )
		self.m_panel1.Layout()
		bSizer15.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		bSizer1.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePickerDesk1.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChangedDesk1 )
		self.m_button15.Bind( wx.EVT_BUTTON, self.OnButtonClickDesk1Edit )
		self.m_checkBoxShowSpecialPages1.Bind( wx.EVT_CHECKBOX, self.OnCheckBoxShowSpecialPages1 )
		self.m_button14.Bind( wx.EVT_BUTTON, self.OnButtonClickAbout )
		self.m_button91.Bind( wx.EVT_BUTTON, self.OnButtonClickL2RCopySelected )
		self.m_button911.Bind( wx.EVT_BUTTON, self.OnButtonClickL2RCopyAll )
		self.m_button9.Bind( wx.EVT_BUTTON, self.OnButtonClickL2RMoveSelected )
		self.m_button11.Bind( wx.EVT_BUTTON, self.OnButtonClickL2RMoveAll )
		self.m_button10.Bind( wx.EVT_BUTTON, self.OnButtonClickR2LMoveSelected )
		self.m_button12.Bind( wx.EVT_BUTTON, self.OnButtonClickR2LMoveAll )
		self.m_button101.Bind( wx.EVT_BUTTON, self.OnButtonClickR2LCopySelected )
		self.m_button1011.Bind( wx.EVT_BUTTON, self.OnButtonClickR2LCopyAll )
		self.m_filePickerDesk2.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChangedDesk2 )
		self.m_button151.Bind( wx.EVT_BUTTON, self.OnButtonClickDesk2MoveUp )
		self.m_button13.Bind( wx.EVT_BUTTON, self.OnButtonClickExit )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFileChangedDesk1( self, event ):
		event.Skip()
	
	def OnButtonClickDesk1Edit( self, event ):
		event.Skip()
	
	def OnCheckBoxShowSpecialPages1( self, event ):
		event.Skip()
	
	def OnButtonClickAbout( self, event ):
		event.Skip()
	
	def OnButtonClickL2RCopySelected( self, event ):
		event.Skip()
	
	def OnButtonClickL2RCopyAll( self, event ):
		event.Skip()
	
	def OnButtonClickL2RMoveSelected( self, event ):
		event.Skip()
	
	def OnButtonClickL2RMoveAll( self, event ):
		event.Skip()
	
	def OnButtonClickR2LMoveSelected( self, event ):
		event.Skip()
	
	def OnButtonClickR2LMoveAll( self, event ):
		event.Skip()
	
	def OnButtonClickR2LCopySelected( self, event ):
		event.Skip()
	
	def OnButtonClickR2LCopyAll( self, event ):
		event.Skip()
	
	def OnFileChangedDesk2( self, event ):
		event.Skip()
	
	def OnButtonClickDesk2MoveUp( self, event ):
		event.Skip()
	
	def OnButtonClickExit( self, event ):
		event.Skip()
	

###########################################################################
## Class AboutDialog
###########################################################################

class AboutDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About Visualchart Desktop Manager", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer14 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Easily move pages amongst Visualchart Desktops.\n\nVisualchart is a resource intensive application and having less\ndesktops hugely improves the performance.\n\nOur you may want to sometimes see the EUR.USD page and your\nanalysis along the S&P 500, whilst other times you want to keep close \nto the Eurostoxx50 page.\n\nYou choose", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
		self.m_staticText5.Wrap( -1 )
		sbSizer7.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer7.Add( self.m_staticline8, 0, wx.EXPAND, 5 )
		
		self.m_hyperlink1 = wx.HyperlinkCtrl( self, wx.ID_ANY, u"http://code.google.com/p/vcdeskmanager", u"http://code.google.com/p/vcdeskmanager", wx.DefaultPosition, wx.DefaultSize, wx.HL_DEFAULT_STYLE )
		sbSizer7.Add( self.m_hyperlink1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_staticline10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		sbSizer7.Add( self.m_staticline10, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self, wx.ID_ANY, u"(C) 2012 Sensible Odds Ltd.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		sbSizer7.Add( self.m_staticText51, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		bSizer14.Add( sbSizer7, 1, wx.EXPAND|wx.ALL, 5 )
		
		self.m_button7 = wx.Button( self, wx.ID_OK, u"Ok", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer14.Add( self.m_button7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.SetSizer( bSizer14 )
		self.Layout()
		bSizer14.Fit( self )
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

