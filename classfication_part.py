# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'classfication_part.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from bagclassfication_test import BegTestModel


class Ui_Form_classfication(object):


    absolute_path = ""
    result = ""
    classfication_list = ['Gucci 1955马衔扣链带钱包','Gucci Dionysus系肩背包','Gucci GG Marmont系列肩背包','Gucci GG Marmont系列斜挎包'
                          ,'Gucci Ophidia系列肩背包','Gucci Ophidia系列迷你包','Gucci Ophidia系列托特包','Gucci Ophidia系列斜挎包',
                          'Gucci Ophidia系列圆形肩背包','Gucci Sylvie 1969系列手提包','Gucci Zumi 系列手提包','Gucci 高级人造帆布邮差包']

    # 载入模型
    m = BegTestModel()
    m.load_model()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(935, 754)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 771, 111))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 371, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 871, 501))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(400, 140, 471, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.pushButton.clicked.connect(self.get_path)
        self.pushButton_2.clicked.connect(self.check)
        self.pushButton_3.clicked.connect(self.lineEdit.clear)
        self.pushButton_3.clicked.connect(self.label_2.clear)
        self.pushButton_3.clicked.connect(self.label_3.clear)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    #读取文件夹名称  保存成一个list  输出时按照结果写出编号list[result]
    def check(self):

        self.result = self.m.test_model(self.absolute_path[0])
        # if self.result == 0:
        #     self.label_2.setText("此为真品")
        # elif self.result == 1:
        #     self.label_2.setText("此为赝品")
        # else:
        #     self.label_2.setText("模型出错")
        print(self.result)
        self.label_3.setText(self.classfication_list[self.result])
        print(self.classfication_list[self.result])  # 此处改成ui中label中输出

    def get_path(self):

        self.absolute_path = QFileDialog.getOpenFileName(None, 'open file', './')
        print(self.absolute_path[0])
        self.lineEdit.setText(self.absolute_path[0])
        self.label_2.setPixmap(QPixmap(self.absolute_path[0]))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "奢侈品系列判别"))
        self.label.setText(_translate("Form", "功能二说明：1.点击选择按钮，选择要奢侈品图片的相对路径，图片类型应为jpg,bmp等常用图片类型（目前版本只适用于gucci包袋）\n"
"            2.选择好图片后，图片会显示在下方图片区域，确认无误后点击分辨，分辨结果会显示在结果区\n"
"            3.若要继续分辨其他图片，需点击清空将记录清除后重新进行步骤1"))
        self.pushButton.setText(_translate("Form", "选择.."))
        self.pushButton_3.setText(_translate("Form", "清空"))
        self.label_2.setText(_translate("Form", "此为图片区域"))
        self.pushButton_2.setText(_translate("Form", "分辨"))
        self.label_3.setText(_translate("Form", "此为分辨结果区域"))

