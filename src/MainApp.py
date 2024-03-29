#!/usr/bin/env python
# -*- coding: latin-1; py-indent-offset:4 -*-
################################################################################
# 
# This file is part of VCDeskManager
#
# VCDeskManager is a graphical interface to manipulate Visualchart (R)
# desktop pages to ease the memory requirements of a desktop
#
# Copyright (C) 2012 Sensible Odds Ltd.
#
# You can learn more and contact the author at:
#
#    http://code.google.com/p/vcdeskmanager/
#
# VCDeskManager is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# VCDeskManager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with VCDeskManager. If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import wx

import MainFrame

def Run():
    app = MainApp(0)
    app.MainLoop()


class MainApp(wx.App):
    def OnInit(self):
        wx.Log_SetActiveTarget(wx.LogStderr())
        # wx.Log_SetActiveTarget(wx.LogBuffer())

        frame = MainFrame.MainFrame(None)
        self.SetTopWindow(frame)
        frame.Show(True)

        return True

