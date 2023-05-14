# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'second.ui'
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
        Form.resize(400, 300)
        self.InputGroup = QGroupBox(Form)
        self.InputGroup.setObjectName(u"InputGroup")
        self.InputGroup.setGeometry(QRect(20, 40, 120, 181))
        self.Output = QRadioButton(self.InputGroup)
        self.Output.setObjectName(u"Output")
        self.Output.setEnabled(True)
        self.Output.setGeometry(QRect(20, 40, 82, 17))
        self.Output.setChecked(True)
        self.Input = QRadioButton(self.InputGroup)
        self.Input.setObjectName(u"Input")
        self.Input.setGeometry(QRect(20, 110, 82, 17))
        self.OutputConfigGroup = QGroupBox(Form)
        self.OutputConfigGroup.setObjectName(u"OutputConfigGroup")
        self.OutputConfigGroup.setGeometry(QRect(180, 40, 171, 80))
        self.High = QRadioButton(self.OutputConfigGroup)
        self.High.setObjectName(u"High")
        self.High.setGeometry(QRect(10, 20, 82, 17))
        self.High.setChecked(True)
        self.Low = QRadioButton(self.OutputConfigGroup)
        self.Low.setObjectName(u"Low")
        self.Low.setGeometry(QRect(10, 50, 82, 17))
        self.OutputInputGroup = QGroupBox(Form)
        self.OutputInputGroup.setObjectName(u"OutputInputGroup")
        self.OutputInputGroup.setEnabled(False)
        self.OutputInputGroup.setGeometry(QRect(180, 130, 171, 80))
        self.PullUp = QRadioButton(self.OutputInputGroup)
        self.PullUp.setObjectName(u"PullUp")
        self.PullUp.setGeometry(QRect(10, 30, 82, 17))
        self.PullUp.setChecked(True)
        self.HighImp = QRadioButton(self.OutputInputGroup)
        self.HighImp.setObjectName(u"HighImp")
        self.HighImp.setGeometry(QRect(10, 60, 82, 17))
        self.Output_Path = QLineEdit(Form)
        self.Output_Path.setObjectName(u"Output_Path")
        self.Output_Path.setGeometry(QRect(20, 260, 271, 20))
        self.GenerateButton = QPushButton(Form)
        self.GenerateButton.setObjectName(u"GenerateButton")
        self.GenerateButton.setGeometry(QRect(310, 260, 75, 23))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 240, 131, 16))

        self.retranslateUi(Form)
        
        QObject.connect(self.Output,SIGNAL("clicked(bool)"),self.OutputInputGroup.setDisabled)
        QObject.connect(self.Output,SIGNAL("clicked(bool)"),self.OutputConfigGroup.setEnabled)
        QObject.connect(self.Input,SIGNAL("clicked(bool)"),self.OutputConfigGroup.setDisabled)
        QObject.connect(self.Input,SIGNAL("clicked(bool)"),self.OutputInputGroup.setEnabled)
        
        self.GenerateButton.clicked.connect(self.GenerateFunction)

        QMetaObject.connectSlotsByName(Form)
        
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.InputGroup.setTitle(QCoreApplication.translate("Form", u"Pin0 Direction", None))
        self.Output.setText(QCoreApplication.translate("Form", u"Output", None))
        self.Input.setText(QCoreApplication.translate("Form", u"Input", None))
        self.OutputConfigGroup.setTitle(QCoreApplication.translate("Form", u"Output Config", None))
        self.High.setText(QCoreApplication.translate("Form", u"Hugh", None))
        self.Low.setText(QCoreApplication.translate("Form", u"Low", None))
        self.OutputInputGroup.setTitle(QCoreApplication.translate("Form", u"Input Config", None))
        self.PullUp.setText(QCoreApplication.translate("Form", u"Pull-Up", None))
        self.HighImp.setText(QCoreApplication.translate("Form", u"High Imp", None))
        self.Output_Path.setText(QCoreApplication.translate("Form", u"Enter Path to Generate Configuration", None))
        self.GenerateButton.setText(QCoreApplication.translate("Form", u"Generate", None))
        self.label.setText(QCoreApplication.translate("Form", u"Output Path", None))
    # retranslateUi

    def GenerateFunction(self):
  
      Path = self.Output_Path.text() + r'\DIO_CONFIG.h'
      File_Handler = open(Path ,'w')
      
      File_Handler.write("#ifndef _DIO_CONFIG_H\n")
      File_Handler.write("#define _DIO_CONFIG_H\n")
      File_Handler.write("\n")
      File_Handler.write("\n")
      File_Handler.write("\n")
      File_Handler.write("\n")
      File_Handler.write("\n")
      
      if self.Output.isChecked() :
        if self.High.isChecked():
          File_Handler.write("#define   DIO_PIN_0_MODE  DIO_OUTPUT_HIGH\n")
        else :
         File_Handler.write("#define   DIO_PIN_0_MODE  DIO_OUTPUT_LOW\n")
      else : 
        if self.PullUp.isChecked():
          File_Handler.write("#define   DIO_PIN_0_MODE  DIO_INPUT_PULLED_UP\n")
        else :
          File_Handler.write("#define   DIO_PIN_0_MODE  DIO_INPUT_HIGH_IMP\n")
      File_Handler.write("#endif /*_DIO_CONFIG_H*/\n")
      
      
app = QApplication(sys.argv)
Widget = QWidget()
Form=Ui_Form()
Form.setupUi(Widget)
Widget.show()
sys.exit(app.exec_())