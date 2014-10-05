# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Documents and Settings\ebinard\Desktop\core.ui'
#
# Created: Tue Sep 16 14:21:59 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(396, 96)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.dragDropRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.dragDropRadioButton.setGeometry(QtCore.QRect(80, 60, 82, 18))
        self.dragDropRadioButton.setObjectName(_fromUtf8("dragDropRadioButton"))
        self.doubleClickRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.doubleClickRadioButton.setGeometry(QtCore.QRect(80, 40, 82, 18))
        self.doubleClickRadioButton.setObjectName(_fromUtf8("doubleClickRadioButton"))
        self.rightRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.rightRadioButton.setGeometry(QtCore.QRect(80, 20, 82, 18))
        self.rightRadioButton.setObjectName(_fromUtf8("rightRadioButton"))
        self.leftRadioButton = QtGui.QRadioButton(self.centralwidget)
        self.leftRadioButton.setGeometry(QtCore.QRect(80, 0, 82, 18))
        self.leftRadioButton.setObjectName(_fromUtf8("leftRadioButton"))
        self.quitButton = QtGui.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(0, 30, 75, 23))
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Simplified Automatization Click System", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.dragDropRadioButton.setText(_translate("MainWindow", "Drag & Drop", None))
        self.doubleClickRadioButton.setText(_translate("MainWindow", "Double Click", None))
        self.rightRadioButton.setText(_translate("MainWindow", "Right", None))
        self.leftRadioButton.setText(_translate("MainWindow", "Left", None))
        self.quitButton.setText(_translate("MainWindow", "Quit", None))

