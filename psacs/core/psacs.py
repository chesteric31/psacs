#!/usr/bin/python

import wx
from Clicking import Clicking

class psacs(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        leftButton = wx.Button(self, -1, label="Left click")
        sizer.Add(leftButton, (0, 0))
        
        self.label = wx.StaticText(self, -1, label=u'Hello !')
        self.label.SetBackgroundColour(wx.BLUE)
        self.label.SetForegroundColour(wx.WHITE)
        
        MyThread = Clicking(self.label)
        
        self.Bind(wx.EVT_BUTTON, lambda event: self.OnLeftClick(event, MyThread), leftButton)
        stopButton = wx.Button(self, -1, label="Stop")
        sizer.Add(stopButton, (0, 1))
        self.Bind(wx.EVT_BUTTON, lambda event: self.OnStopClick(event, MyThread), stopButton)

        sizer.Add(self.label, (1, 0), (1, 2), wx.EXPAND)

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1, self.GetSize().y, -1, self.GetSize().y);
        self.Show(True)

    def OnLeftClick(self, event, MyThread):
        self.label.SetLabel("Left Clicking")
        if MyThread.isAlive() == False:
            MyThread.start()
        
    def OnStopClick(self, event, MyThread):
        self.label.SetLabel("Stop Clicking")
        MyThread.stop()

if __name__ == "__main__":
    app = wx.App()
    frame = psacs(None, 'PSACS')
    app.MainLoop()
