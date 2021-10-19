import sys
from PyQt5.QtWidgets import  QApplication,QMainWindow
from maskui import Ui_MainWindow
import os
import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
    def opencamera(self):
        os.system('python detect.py --source 0 --weights weights/best.pt --conf-thres 0.6')
    def openimage(self):
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        #print(imgName,imgType)
        os.system('python detect.py --source %s --weights weights/best.pt --conf-thres 0.6'%imgName)
        path='D:/mlfinal_pj/inference'
        folder_name=os.listdir(path)[-1]
        img_name=os.listdir(path+'/'+folder_name)[0]
        img_path=path+'/'+folder_name+'/'+img_name
        print(img_path)
        jpg = QtGui.QPixmap(imgName).scaled(self.label.width(), self.label.height())
        jpg_detect=QtGui.QPixmap(img_path).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(jpg)
        self.label_2.setPixmap(jpg_detect)
    def openvedio(self):
        vedioName, vedioType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        print(vedioName)
        os.system('python detect.py --source %s --weights weights/best.pt --conf-thres 0.60'%vedioName)

if __name__ == "__main__":
    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainWindow()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())