# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'threeable.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from check_part import Ui_Form_check
from classfication_part import Ui_Form_classfication
from downloadPicture import Ui_Form_downloadPicture
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 711, 141))
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(39, 200, 211, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")

        self.pushButton_2.clicked.connect(self.check_part)
        self.pushButton_3.clicked.connect(self.classfication_part)
        self.pushButton.clicked.connect(self.downloadPicture_part)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    #真假检验部分
    def check_part(self):
        self.form_check = QtWidgets.QWidget()
        self.ui2 = Ui_Form_check()
        self.ui2.setupUi(self.form_check)
        self.form_check.show()


    #奢侈品分类部分
    def classfication_part(self):
        self.from_classfication_part = QtWidgets.QWidget()
        self.ui3 = Ui_Form_classfication()
        self.ui3.setupUi(self.from_classfication_part)
        self.from_classfication_part.show()


    #批量下载图片部分
    def downloadPicture_part(self):
        self.form_downloadPicture = QtWidgets.QWidget()
        self.ui4 = Ui_Form_downloadPicture()
        self.ui4.setupUi(self.form_downloadPicture)
        self.form_downloadPicture.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "毕设  by王舸"))
        self.label.setText(_translate("MainWindow", "使用说明：\n"
"     功能一：添加奢侈品鉴定点放大图，进行鉴定，图片类型应为jpg,bmp等常用类型\n"
"     功能二：添加奢侈品图片，对奢侈品的品牌、系列进行辨识，可获得奢侈品的品牌及其系列（目前版本只适用于GUCCI包袋）\n"
"     功能三：输入关键字，可批量下载带有关键字的图片"))
        self.pushButton_2.setText(_translate("MainWindow", "功能一：奢侈品真假鉴定"))
        self.pushButton_3.setText(_translate("MainWindow", "功能二：奢侈品品牌、系列分类"))
        self.pushButton.setText(_translate("MainWindow", "功能三：图片批量下载"))
        self.action_2.setText(_translate("MainWindow", "下载指定图片"))

