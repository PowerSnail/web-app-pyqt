# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebAppInstaller/webwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WebWindow(object):
    def setupUi(self, WebWindow):
        WebWindow.setObjectName("WebWindow")
        WebWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(WebWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        WebWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WebWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        WebWindow.setMenuBar(self.menubar)

        self.retranslateUi(WebWindow)
        QtCore.QMetaObject.connectSlotsByName(WebWindow)

    def retranslateUi(self, WebWindow):
        _translate = QtCore.QCoreApplication.translate
        WebWindow.setWindowTitle(_translate("WebWindow", "MainWindow"))
