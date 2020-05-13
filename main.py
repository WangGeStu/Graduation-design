import sys,os
import threeable

from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *



if __name__ == '__main__':


    app=QApplication(sys.argv)

    mainWindow=QMainWindow()

    ui = threeable.Ui_MainWindow()

    ui.setupUi(mainWindow)

    mainWindow.show()

    sys.exit(app.exec_())
