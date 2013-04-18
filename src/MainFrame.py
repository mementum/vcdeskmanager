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

NAME = 'Visualchart Desktop Manager'
VERSION='1.02'

import copy
import xml.etree.ElementTree as ET

import wx

import MainGui

# Implementing HPPFrame
class MainFrame(MainGui.MainFrame):
    def __init__(self, parent):
	MainGui.MainFrame.__init__(self, parent)
        self.SetTitle('%s %s' % (NAME, VERSION))

        self.etree = dict()
        self.etree[1] = None
        self.etree[2] = None

        self.fname = dict()
        self.fname[1] = ''
        self.fname[2] = ''

        self.fpicker = dict()
        self.fpicker[1] = self.m_filePickerDesk1
        self.fpicker[2] = self.m_filePickerDesk2

        self.pages = dict()
        self.pages[1] = None
        self.pages[2] = None

        self.lbs = dict()
        self.lbs[1] = self.m_listBoxDesk1
        self.lbs[2] = self.m_listBoxDesk2

        self.label = dict()
        self.label[1] = self.m_staticTextDesk1
        self.label[2] = self.m_staticTextDesk2


    def OnFileChanged(self, index):
        self.lbs[index].Clear()

        self.fname[index] = self.fpicker[index].GetPath()
        self.etree[index] = ET.parse(self.fname[index])
        wksinfo = self.etree[index].find('WksInfo')
        deskname = wksinfo.find('Name')
        self.label[index].SetLabel(deskname.text)

        self.pages[index] = self.etree[index].find('Pages')

        for page in self.pages[index]:
            if 'Type' in page.attrib:
                # Skip special pages
                continue

            if 'Name' not in page.attrib:
                # Skip empty pages
                continue

            self.lbs[index].Append(page.attrib['Name'], page)


    def OnFileChangedDesk1(self, event):
        event.Skip()
        self.OnFileChanged(1)

    def OnFileChangedDesk2(self, event):
        event.Skip()
        self.OnFileChanged(2)


    def PagePositionFix(self, index):
        # Need to iterate source and change page number
        curpos = 0
        for page in self.pages[index]:
            if 'Name' not in page.attrib:
                continue # skip phantom pages

            pos = int(page.attrib['Position'])
            if curpos != pos:
                page.attrib['Position'] = str(curpos)
            curpos += 1


    def OnButtonClickR2LMoveAll(self, event):
        event.Skip()
        self.OnButtonClickMoveSelected(src=2, dst=1, moveall=True)

    def OnButtonClickL2RMoveAll(self, event):
        event.Skip()
        self.OnButtonClickMoveSelected(src=1, dst=2, moveall=True)

    def OnButtonClickL2RMoveSelected(self, event):
        event.Skip()
        self.OnButtonClickMoveSelected(src=1, dst=2)

    def OnButtonClickR2LMoveSelected(self, event):
        event.Skip()
        self.OnButtonClickMoveSelected(src=2, dst=1)


    def OnButtonClickMoveSelected(self, src, dst, moveall=False, move=True):
        # check if we loaded a file
        if self.pages[src] is None or self.pages[dst] is None:
            return

        lbsrc, lbdst = self.lbs[src], self.lbs[dst]

        if not moveall:
            selections = lbsrc.GetSelections()
        else:
            selections = range(0, lbsrc.GetCount())

        if not selections:
            return

        tomove = list()

        # Remove from source (listbox and pages node)
        for selection in reversed(selections):
            pagename = lbsrc.GetString(selection)
            clientdata = lbsrc.GetClientData(selection)
            if move:
                lbsrc.Delete(selection)
                self.pages[src].remove(clientdata)
            else:
                clientdata = tomove.append(copy.deepcopy(clientdata))

            tomove.append((pagename, clientdata)) # keep a copy

        # Append to destination (listbox and pages node)
        for pagename, clientdata in reversed(tomove):
            lbdst.Append(pagename, clientdata)
            self.pages[dst].append(clientdata)

        # Fix page positions
        self.PagePositionFix(src)
        self.PagePositionFix(dst)

        # Write to file
        if move:
            self.etree[src].write(self.fname[src], encoding='ISO-8859-1')
        self.etree[dst].write(self.fname[dst], encoding='ISO-8859-1')

        
specialpages = '''
<Page T="0" GUID="E122EB3E-1DC8-4BE3-A2F1-A0A563952B5C" Type="0" Position="0" Name="Market Monitor"/>
<Page T="0" GUID="5E9FDB4C-5848-4F08-BC23-A2A1C95CD456" Type="1" Position="1" Name="Broker Access"/>
<Page T="0" GUID="F9079FE2-1990-4C38-BCBC-56749A4ABBF1" Type="3" Position="2" Name="Portfolio"/>
<Page T="0" GUID="160B80E4-E340-4FDE-B7A3-461813E0C7CB" Type="4" Position="3" Name="iLive"/>
'''
