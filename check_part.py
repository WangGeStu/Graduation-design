# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_part.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys,os
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from imageclassfication_test import TTestModel
class Ui_Form_check(object):
    absolute_path = ""
    result = ""

    # 载入模型
    m = TTestModel()
    m.load_model()



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(748, 593)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 691, 61))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 150, 281, 80))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(290, 150, 451, 321))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 260, 281, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)

        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.pushButton.clicked.connect(self.get_path)
        self.pushButton_2.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.label_2.clear)
        self.pushButton_2.clicked.connect(self.label_3.clear)
        self.pushButton_3.clicked.connect(self.check)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



    def check(self):



        self.result = self.m.test_model(self.absolute_path[0])
        if self.result == 0:
            self.label_3.setText("此为真品")
        elif self.result == 1:
            self.label_3.setText("此为赝品")
        else:
            self.label_3.setText("模型出错")
        print(self.result)#此处改成ui中label中输出


    def get_path(self):


        self.absolute_path = QFileDialog.getOpenFileName(None,'open file','./')
        print(self.absolute_path[0])
        self.lineEdit.setText(self.absolute_path[0])
        self.label_2.setPixmap(QPixmap(self.absolute_path[0]))
        # m = TTestModel()
        # m.load_model()
        # print(m.test_model(self.absolute_path[0]))#此处改成ui中label中输出
        # #self.lineEdit.show(absolute_path[0])

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "奢侈品真伪检验"))
        self.label.setText(_translate("Form", "功能一说明：1.选择需要鉴定的鉴定点图片，图片的相对地址会显示在文本栏中，此图片类型应为jpg,bmp等常用图片类型\n"
"            2.选择好图片后，图片会显示在右方供您确认，确认无误后点击检测，检测结果会显示在下方\n"
"            3.若需要再次鉴定其他图片，需点击清空，将之前的记录清空"))
        self.pushButton.setText(_translate("Form", "选择.."))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.label_2.setText(_translate("Form", " 图片显示区域"))
        self.pushButton_3.setText(_translate("Form", "检测"))
        self.label_3.setText(_translate("Form", "鉴定结果区域"))


# if __name__ == '__main__':
# #
# #
# #     app=QApplication(sys.argv)
# #
# #     mainWindow=QMainWindow()
# #
# #     ui = Ui_Form_check()
# #
# #     ui.setupUi(mainWindow)
# #
# #     mainWindow.show()
# #
# #     sys.exit(app.exec_())
