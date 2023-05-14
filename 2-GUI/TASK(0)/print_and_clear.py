# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'first.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 159)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(260, 40, 91, 31))
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 40, 121, 21))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 20, 61, 16))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 70, 91, 31))

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.lineEdit.clear)
        self.pushButton_2.clicked.connect(self.PrintFunc)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.lineEdit.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Enter Data", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Print", None))
    # retranslateUi
    
    
    def PrintFunc (self):
      print(self.lineEdit.text())

app = QApplication(sys.argv)
Widget = QWidget()
Form = Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())
#or app.exec_()
