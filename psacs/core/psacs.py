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
            time.sleep(0.5)
            x_dim, y_dim = mouse.position()
            if x_dim != old_x_dim or y_dim != old_y_dim:
                mouse.click(x_dim, y_dim, 1)
                self._stopevent.wait(1.0)
            old_x_dim = x_dim
            old_y_dim = y_dim
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
    def stop(self):
        self._stopevent.set()

class Psacs(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        leftButton = wx.Button(self, -1, label="Left click")
        sizer.Add(leftButton, (0, 0))
        
        self.label = wx.StaticText(self, -1, label=u'Hello !')
        
        MyThread = Clicking(self.label)
        
        stopButton = wx.Button(self, -1, label="Stop")
        stopButton.Enable(False)
        self.Bind(wx.EVT_BUTTON, lambda event: self.OnLeftClick(event, MyThread, stopButton), leftButton)
        sizer.Add(stopButton, (0, 1))
        self.Bind(wx.EVT_BUTTON, lambda event: self.OnStopClick(event, MyThread, stopButton), stopButton)

        sizer.Add(self.label, (1, 0), (1, 2), wx.EXPAND)

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1, self.GetSize().y, -1, self.GetSize().y);
        self.Show(True)

    def OnLeftClick(self, event, MyThread, stopButton):
        self.label.SetLabel("Left Clicking")
        if MyThread.isAlive() == False:
            MyThread.start()
            stopButton.Enable(True)
            
        
    def OnStopClick(self, event, MyThread, stopButton):
        self.label.SetLabel("Stop Clicking")
        MyThread.stop()
        stopButton.Enable(False)

if __name__ == "__main__":
    app = wx.App()
    frame = Psacs(None, 'PSACS')
    app.MainLoop()
