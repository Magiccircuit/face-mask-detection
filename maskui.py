# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'maskui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1500)
        MainWindow.setMinimumSize(QtCore.QSize(750, 1600))
        MainWindow.setMaximumSize(QtCore.QSize(750, 1600))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("此处显示检测图片")
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:50px;font-weight:bold;font-family:黑体;}"
                                 )
        self.verticalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setText("此处显示原图片")
        self.label.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:50px;font-weight:bold;font-family:黑体;}"
                                 )
        self.verticalLayout.addWidget(self.label)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionpicture = QtWidgets.QAction(MainWindow)
        self.actionpicture.setObjectName("actionpicture")
        self.actionvedio = QtWidgets.QAction(MainWindow)
        self.actionvedio.setObjectName("actionvedio")
        self.actioncamera = QtWidgets.QAction(MainWindow)
        self.actioncamera.setObjectName("actioncamera")
        self.actionimg = QtWidgets.QAction(MainWindow)
        self.actionimg.setObjectName("actionimg")
        self.actionvedio_2 = QtWidgets.QAction(MainWindow)
        self.actionvedio_2.setObjectName("actionvedio_2")
        self.actioncamera_2 = QtWidgets.QAction(MainWindow)
        self.actioncamera_2.setObjectName("actioncamera_2")

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.openimage)
        self.pushButton_3.clicked.connect(MainWindow.opencamera)
        self.pushButton_2.clicked.connect(MainWindow.openvedio)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ml final project:口罩检测  作者---张乐"))
        #self.label.setText(_translate("MainWindow", "此处显示原图片"))
        self.pushButton_2.setText(_translate("MainWindow", "打开视频"))
        self.pushButton_3.setText(_translate("MainWindow", "打开摄像头"))
        self.pushButton.setText(_translate("MainWindow", "打开图片"))
        self.actionpicture.setText(_translate("MainWindow", "picture"))
        self.actionvedio.setText(_translate("MainWindow", "vedio"))
        self.actioncamera.setText(_translate("MainWindow", "camera"))
        self.actionimg.setText(_translate("MainWindow", "img"))
        self.actionvedio_2.setText(_translate("MainWindow", "vedio"))
        self.actioncamera_2.setText(_translate("MainWindow", "camera"))

