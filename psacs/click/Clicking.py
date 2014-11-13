#!/usr/bin/python

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