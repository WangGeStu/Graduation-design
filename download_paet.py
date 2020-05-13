# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadPicture_part.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from crawler import crawler

class Ui_Form_downloadPicture(object):


    absolute_savePath = " "
    keyword = ""

    #创建实例对象
    downLoad = crawler()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(881, 741)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 761, 141))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 280, 401, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(180, 200, 401, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_2.clicked.connect(self.getSavePath)
        self.pushButton.clicked.connect(self.getkeyword)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def getSavePath(self):
        self.absolute_savePath = QFileDialog.getExistingDirectory(None, 'open file', './')
        self.lineEdit_2.setText(self.absolute_savePath)
        print(self.absolute_savePath)


    def getkeyword(self):
        self.keyword = self.lineEdit.text()
        print( self.keyword )
        self.downLoad.run(self.absolute_savePath,self.keyword)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图片批量下载"))
        self.label.setText(_translate("Form", "功能三提示：1.选择要下载的相对路径，默认为本地文件夹\n"
"            2.输入需要下载的图片关键字，点击下载"))
        self.label_2.setText(_translate("Form", "搜索的关键字："))
        self.pushButton.setText(_translate("Form", "下载"))
        self.label_3.setText(_translate("Form", "图片存储文件夹："))
        self.pushButton_2.setText(_translate("Form", "选择.."))

