# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WebAppInstaller/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.toolButton_2 = QtWidgets.QToolButton(self.widget_4)
        icon = QtGui.QIcon.fromTheme("list-remove")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_3.addWidget(self.toolButton_2)
        self.toolButton = QtWidgets.QToolButton(self.widget_4)
        self.toolButton.setText("")
        icon = QtGui.QIcon.fromTheme("list-add")
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_3.addWidget(self.toolButton)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.listWidgetApps = QtWidgets.QListWidget(self.widget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetApps.sizePolicy().hasHeightForWidth())
        self.listWidgetApps.setSizePolicy(sizePolicy)
        self.listWidgetApps.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidgetApps.setObjectName("listWidgetApps")
        self.verticalLayout_2.addWidget(self.listWidgetApps)
        self.horizontalLayout.addWidget(self.widget_3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.editName = QtWidgets.QLineEdit(self.groupBox)
        self.editName.setObjectName("editName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.editName)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.editUrl = QtWidgets.QLineEdit(self.groupBox)
        self.editUrl.setObjectName("editUrl")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.editUrl)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editIcon = QtWidgets.QLineEdit(self.widget)
        self.editIcon.setObjectName("editIcon")
        self.horizontalLayout_2.addWidget(self.editIcon)
        self.btnChooseIcon = QtWidgets.QPushButton(self.widget)
        self.btnChooseIcon.setObjectName("btnChooseIcon")
        self.horizontalLayout_2.addWidget(self.btnChooseIcon)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnAddField = QtWidgets.QPushButton(self.widget_2)
        self.btnAddField.setText("")
        icon = QtGui.QIcon.fromTheme("list-add")
        self.btnAddField.setIcon(icon)
        self.btnAddField.setObjectName("btnAddField")
        self.verticalLayout.addWidget(self.btnAddField)
        self.layoutExtraFields = QtWidgets.QGridLayout()
        self.layoutExtraFields.setObjectName("layoutExtraFields")
        self.verticalLayout.addLayout(self.layoutExtraFields)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.widget_2)
        self.horizontalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_2.setText(_translate("MainWindow", "-"))
        self.groupBox.setTitle(_translate("MainWindow", "App Settings"))
        self.label.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Url"))
        self.label_2.setText(_translate("MainWindow", "Icon"))
        self.btnChooseIcon.setText(_translate("MainWindow", "Pick Icon"))
        self.label_4.setText(_translate("MainWindow", "Extra Fields"))