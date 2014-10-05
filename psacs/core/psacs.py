#!/usr/bin/python
 
from PyQt4 import QtGui, QtCore
import sys

from ui import psacsUI
 
class Psacs(QtGui.QMainWindow, psacsUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Psacs, self).__init__(parent)
        self.setupUi(self)
        
        self.quitButton.clicked.connect(quit)
        self.connect(self.startButton, QtCore.SIGNAL('clicked()'), self.sayHello)		
    def main(self):
        self.show()

    def sayHello(self):
        self.statusBar.showMessage(self.tr("Finished"))
        
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    core = Psacs()
    core.main()
    app.exec_()
