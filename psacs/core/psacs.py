#!/usr/bin/python

import wx
from pymouse import PyMouse
import time
import threading

class Clicking(threading.Thread): 

    def __init__(self, label):
        threading.Thread.__init__(self) 
        self._stopevent = threading.Event()
        self.label = label
    def run(self): 
        mouse = PyMouse()
        old_x_dim = None
        old_y_dim = None
        while not self._stopevent.isSet():
            time.sleep(2)
            x_dim, y_dim = mouse.position()
            if x_dim != old_x_dim or y_dim != old_y_dim:
                mouse.click(x_dim, y_dim, 1)
                self._stopevent.wait(1.0)
            old_x_dim = x_dim
            old_y_dim = y_dim
        self.label.SetLabel("The thread is done")
    def stop(self): 
        self._stopevent.set()

class psacs(wx.Frame):

    #MyThread = None
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
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
        MyThread.start()
        
    def OnStopClick(self, event, MyThread):
        self.label.SetLabel("Stop Clicking")
        MyThread.stop()

if __name__ == "__main__":
    app = wx.App()
    frame = psacs(None, -1, 'PSACS')
    app.MainLoop()
