# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '折叠窗口哦吼.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(903, 730)
        self.verticalLayout_6 = QVBoxLayout(Form)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.checkBoxSteelType = QCheckBox(Form)
        self.checkBoxSteelType.setObjectName(u"checkBoxSteelType")
        self.checkBoxSteelType.setChecked(False)

        self.verticalLayout_6.addWidget(self.checkBoxSteelType)

        self.groupBoxStateCls = QGroupBox(Form)
        self.groupBoxStateCls.setObjectName(u"groupBoxStateCls")
        self.verticalLayout_3 = QVBoxLayout(self.groupBoxStateCls)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.checkBoxClassName = QCheckBox(self.groupBoxStateCls)
        self.checkBoxClassName.setObjectName(u"checkBoxClassName")
        self.checkBoxClassName.setEnabled(True)
        self.checkBoxClassName.setStyleSheet(u"QCheckBox{\n"
"	margin-left:15px;\n"
"}")
        self.checkBoxClassName.setChecked(False)

        self.verticalLayout_3.addWidget(self.checkBoxClassName)

        self.groupBoxStateSL = QGroupBox(self.groupBoxStateCls)
        self.groupBoxStateSL.setObjectName(u"groupBoxStateSL")
        self.verticalLayout_2 = QVBoxLayout(self.groupBoxStateSL)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(self.groupBoxStateSL)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButtonSLevel = QRadioButton(self.groupBox)
        self.radioButtonSLevel.setObjectName(u"radioButtonSLevel")
        self.radioButtonSLevel.setChecked(True)

        self.verticalLayout.addWidget(self.radioButtonSLevel)

        self.groupBoxSteelL1 = QGroupBox(self.groupBox)
        self.groupBoxSteelL1.setObjectName(u"groupBoxSteelL1")
        self.groupBoxSteelL1.setStyleSheet(u"QLineEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.groupBoxSteelL1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEditOneOneTNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneOneTNum.setObjectName(u"lineEditOneOneTNum")
        self.lineEditOneOneTNum.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneOneTNum, 0, 2, 1, 1)

        self.lineEditOneThMin = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneThMin.setObjectName(u"lineEditOneThMin")
        self.lineEditOneThMin.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneThMin, 2, 5, 1, 1)

        self.labelLevelNumber_3 = QLabel(self.groupBoxSteelL1)
        self.labelLevelNumber_3.setObjectName(u"labelLevelNumber_3")
        self.labelLevelNumber_3.setMargin(10)
        self.labelLevelNumber_3.setIndent(-1)

        self.gridLayout.addWidget(self.labelLevelNumber_3, 2, 0, 1, 1)

        self.label_11 = QLabel(self.groupBoxSteelL1)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 2, 1, 1, 1)

        self.lineEditOneTwoTNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneTwoTNum.setObjectName(u"lineEditOneTwoTNum")
        self.lineEditOneTwoTNum.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneTwoTNum, 1, 2, 1, 1)

        self.label_8 = QLabel(self.groupBoxSteelL1)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.labelLevelNumber_2 = QLabel(self.groupBoxSteelL1)
        self.labelLevelNumber_2.setObjectName(u"labelLevelNumber_2")
        self.labelLevelNumber_2.setMargin(10)
        self.labelLevelNumber_2.setIndent(-1)

        self.gridLayout.addWidget(self.labelLevelNumber_2, 1, 0, 1, 1)

        self.label_10 = QLabel(self.groupBoxSteelL1)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 6, 1, 1)

        self.label_12 = QLabel(self.groupBoxSteelL1)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 3, 1, 1)

        self.label_7 = QLabel(self.groupBoxSteelL1)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)

        self.lineEditOneOneMax = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneOneMax.setObjectName(u"lineEditOneOneMax")
        self.lineEditOneOneMax.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneOneMax, 0, 7, 1, 1)

        self.lineEditOneTwoMin = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneTwoMin.setObjectName(u"lineEditOneTwoMin")
        self.lineEditOneTwoMin.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneTwoMin, 1, 5, 1, 1)

        self.label_4 = QLabel(self.groupBoxSteelL1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)

        self.label_5 = QLabel(self.groupBoxSteelL1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 4, 1, 1)

        self.label_9 = QLabel(self.groupBoxSteelL1)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 4, 1, 1)

        self.label_6 = QLabel(self.groupBoxSteelL1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 6, 1, 1)

        self.lineEditOneThTNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneThTNum.setObjectName(u"lineEditOneThTNum")
        self.lineEditOneThTNum.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneThTNum, 2, 2, 1, 1)

        self.label = QLabel(self.groupBoxSteelL1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBoxSteelL1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_3 = QLabel(self.groupBoxSteelL1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.lineEditOneTwoMax = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneTwoMax.setObjectName(u"lineEditOneTwoMax")
        self.lineEditOneTwoMax.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneTwoMax, 1, 7, 1, 1)

        self.label_13 = QLabel(self.groupBoxSteelL1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 8, 1, 1)

        self.labelLevelNumber = QLabel(self.groupBoxSteelL1)
        self.labelLevelNumber.setObjectName(u"labelLevelNumber")
        self.labelLevelNumber.setMargin(10)
        self.labelLevelNumber.setIndent(-1)

        self.gridLayout.addWidget(self.labelLevelNumber, 0, 0, 1, 1)

        self.lineEditOneOneMin = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneOneMin.setObjectName(u"lineEditOneOneMin")
        self.lineEditOneOneMin.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneOneMin, 0, 5, 1, 1)

        self.lineEditOneThMax = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneThMax.setObjectName(u"lineEditOneThMax")
        self.lineEditOneThMax.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneThMax, 2, 7, 1, 1)

        self.lineEditOneOneNo = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneOneNo.setObjectName(u"lineEditOneOneNo")
        self.lineEditOneOneNo.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneOneNo, 0, 9, 1, 1)

        self.label_14 = QLabel(self.groupBoxSteelL1)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 8, 1, 1)

        self.label_15 = QLabel(self.groupBoxSteelL1)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 8, 1, 1)

        self.lineEditOneTwoNo = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneTwoNo.setObjectName(u"lineEditOneTwoNo")
        self.lineEditOneTwoNo.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneTwoNo, 1, 9, 1, 1)

        self.lineEditOneThNo = QLineEdit(self.groupBoxSteelL1)
        self.lineEditOneThNo.setObjectName(u"lineEditOneThNo")
        self.lineEditOneThNo.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEditOneThNo, 2, 9, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBoxSteelL1)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.groupBoxStateSL)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButtonSLevel_2 = QRadioButton(self.groupBox_4)
        self.radioButtonSLevel_2.setObjectName(u"radioButtonSLevel_2")
        self.radioButtonSLevel_2.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButtonSLevel_2)

        self.groupBoxSteelL2 = QGroupBox(self.groupBox_4)
        self.groupBoxSteelL2.setObjectName(u"groupBoxSteelL2")
        self.groupBoxSteelL2.setStyleSheet(u"QLineEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBoxSteelL2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEditTwoOneTNum = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoOneTNum.setObjectName(u"lineEditTwoOneTNum")
        self.lineEditTwoOneTNum.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoOneTNum, 0, 2, 1, 1)

        self.lineEditTwoThMin = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoThMin.setObjectName(u"lineEditTwoThMin")
        self.lineEditTwoThMin.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoThMin, 2, 5, 1, 1)

        self.labelLevelNumber_7 = QLabel(self.groupBoxSteelL2)
        self.labelLevelNumber_7.setObjectName(u"labelLevelNumber_7")
        self.labelLevelNumber_7.setMargin(10)
        self.labelLevelNumber_7.setIndent(-1)

        self.gridLayout_3.addWidget(self.labelLevelNumber_7, 2, 0, 1, 1)

        self.label_31 = QLabel(self.groupBoxSteelL2)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_3.addWidget(self.label_31, 2, 1, 1, 1)

        self.lineEditTwoTwoTNum = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoTwoTNum.setObjectName(u"lineEditTwoTwoTNum")
        self.lineEditTwoTwoTNum.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoTwoTNum, 1, 2, 1, 1)

        self.label_32 = QLabel(self.groupBoxSteelL2)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_3.addWidget(self.label_32, 1, 3, 1, 1)

        self.labelLevelNumber_8 = QLabel(self.groupBoxSteelL2)
        self.labelLevelNumber_8.setObjectName(u"labelLevelNumber_8")
        self.labelLevelNumber_8.setMargin(10)
        self.labelLevelNumber_8.setIndent(-1)

        self.gridLayout_3.addWidget(self.labelLevelNumber_8, 1, 0, 1, 1)

        self.label_33 = QLabel(self.groupBoxSteelL2)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_3.addWidget(self.label_33, 2, 6, 1, 1)

        self.label_34 = QLabel(self.groupBoxSteelL2)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_3.addWidget(self.label_34, 2, 3, 1, 1)

        self.label_35 = QLabel(self.groupBoxSteelL2)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_3.addWidget(self.label_35, 1, 1, 1, 1)

        self.lineEditTwoOneMax = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoOneMax.setObjectName(u"lineEditTwoOneMax")
        self.lineEditTwoOneMax.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoOneMax, 0, 7, 1, 1)

        self.lineEditTwoTwoMin = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoTwoMin.setObjectName(u"lineEditTwoTwoMin")
        self.lineEditTwoTwoMin.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoTwoMin, 1, 5, 1, 1)

        self.label_36 = QLabel(self.groupBoxSteelL2)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_3.addWidget(self.label_36, 0, 6, 1, 1)

        self.label_37 = QLabel(self.groupBoxSteelL2)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_3.addWidget(self.label_37, 1, 4, 1, 1)

        self.label_38 = QLabel(self.groupBoxSteelL2)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_3.addWidget(self.label_38, 2, 4, 1, 1)

        self.label_39 = QLabel(self.groupBoxSteelL2)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_3.addWidget(self.label_39, 1, 6, 1, 1)

        self.lineEditTwoThTNum = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoThTNum.setObjectName(u"lineEditTwoThTNum")
        self.lineEditTwoThTNum.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoThTNum, 2, 2, 1, 1)

        self.label_40 = QLabel(self.groupBoxSteelL2)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_3.addWidget(self.label_40, 0, 1, 1, 1)

        self.label_41 = QLabel(self.groupBoxSteelL2)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_3.addWidget(self.label_41, 0, 3, 1, 1)

        self.label_42 = QLabel(self.groupBoxSteelL2)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_3.addWidget(self.label_42, 0, 4, 1, 1)

        self.lineEditTwoTwoMax = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoTwoMax.setObjectName(u"lineEditTwoTwoMax")
        self.lineEditTwoTwoMax.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoTwoMax, 1, 7, 1, 1)

        self.label_43 = QLabel(self.groupBoxSteelL2)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_3.addWidget(self.label_43, 0, 8, 1, 1)

        self.labelLevelNumber_9 = QLabel(self.groupBoxSteelL2)
        self.labelLevelNumber_9.setObjectName(u"labelLevelNumber_9")
        self.labelLevelNumber_9.setMargin(10)
        self.labelLevelNumber_9.setIndent(-1)

        self.gridLayout_3.addWidget(self.labelLevelNumber_9, 0, 0, 1, 1)

        self.lineEditTwoOneMin = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoOneMin.setObjectName(u"lineEditTwoOneMin")
        self.lineEditTwoOneMin.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoOneMin, 0, 5, 1, 1)

        self.lineEditTwoThTMax = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoThTMax.setObjectName(u"lineEditTwoThTMax")
        self.lineEditTwoThTMax.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoThTMax, 2, 7, 1, 1)

        self.lineEditTwoOneNo = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoOneNo.setObjectName(u"lineEditTwoOneNo")
        self.lineEditTwoOneNo.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoOneNo, 0, 9, 1, 1)

        self.label_44 = QLabel(self.groupBoxSteelL2)
        self.label_44.setObjectName(u"label_44")

        self.gridLayout_3.addWidget(self.label_44, 1, 8, 1, 1)

        self.label_45 = QLabel(self.groupBoxSteelL2)
        self.label_45.setObjectName(u"label_45")

        self.gridLayout_3.addWidget(self.label_45, 2, 8, 1, 1)

        self.lineEditTwoTwoNo = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoTwoNo.setObjectName(u"lineEditTwoTwoNo")
        self.lineEditTwoTwoNo.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoTwoNo, 1, 9, 1, 1)

        self.lineEditTwoThNo = QLineEdit(self.groupBoxSteelL2)
        self.lineEditTwoThNo.setObjectName(u"lineEditTwoThNo")
        self.lineEditTwoThNo.setReadOnly(True)

        self.gridLayout_3.addWidget(self.lineEditTwoThNo, 2, 9, 1, 1)


        self.horizontalLayout_3.addLayout(self.gridLayout_3)


        self.verticalLayout_4.addWidget(self.groupBoxSteelL2)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.groupBoxStateSL)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButtonSLevel_3 = QRadioButton(self.groupBox_7)
        self.radioButtonSLevel_3.setObjectName(u"radioButtonSLevel_3")
        self.radioButtonSLevel_3.setChecked(True)

        self.verticalLayout_5.addWidget(self.radioButtonSLevel_3)

        self.groupBoxSteelL3 = QGroupBox(self.groupBox_7)
        self.groupBoxSteelL3.setObjectName(u"groupBoxSteelL3")
        self.groupBoxSteelL3.setStyleSheet(u"QLineEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBoxSteelL3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEditThOneTNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThOneTNum.setObjectName(u"lineEditThOneTNum")
        self.lineEditThOneTNum.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThOneTNum, 0, 2, 1, 1)

        self.lineEditThThMin = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThThMin.setObjectName(u"lineEditThThMin")
        self.lineEditThThMin.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThThMin, 2, 5, 1, 1)

        self.labelLevelNumber_10 = QLabel(self.groupBoxSteelL3)
        self.labelLevelNumber_10.setObjectName(u"labelLevelNumber_10")
        self.labelLevelNumber_10.setMargin(10)
        self.labelLevelNumber_10.setIndent(-1)

        self.gridLayout_4.addWidget(self.labelLevelNumber_10, 2, 0, 1, 1)

        self.label_46 = QLabel(self.groupBoxSteelL3)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_4.addWidget(self.label_46, 2, 1, 1, 1)

        self.lineEditThTwoTNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThTwoTNum.setObjectName(u"lineEditThTwoTNum")
        self.lineEditThTwoTNum.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThTwoTNum, 1, 2, 1, 1)

        self.label_47 = QLabel(self.groupBoxSteelL3)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_4.addWidget(self.label_47, 1, 3, 1, 1)

        self.labelLevelNumber_11 = QLabel(self.groupBoxSteelL3)
        self.labelLevelNumber_11.setObjectName(u"labelLevelNumber_11")
        self.labelLevelNumber_11.setMargin(10)
        self.labelLevelNumber_11.setIndent(-1)

        self.gridLayout_4.addWidget(self.labelLevelNumber_11, 1, 0, 1, 1)

        self.label_48 = QLabel(self.groupBoxSteelL3)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_4.addWidget(self.label_48, 2, 6, 1, 1)

        self.label_49 = QLabel(self.groupBoxSteelL3)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_4.addWidget(self.label_49, 2, 3, 1, 1)

        self.label_50 = QLabel(self.groupBoxSteelL3)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_4.addWidget(self.label_50, 1, 1, 1, 1)

        self.lineEditThOneMax = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThOneMax.setObjectName(u"lineEditThOneMax")
        self.lineEditThOneMax.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThOneMax, 0, 7, 1, 1)

        self.lineEditThTwoMin = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThTwoMin.setObjectName(u"lineEditThTwoMin")
        self.lineEditThTwoMin.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThTwoMin, 1, 5, 1, 1)

        self.label_51 = QLabel(self.groupBoxSteelL3)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_4.addWidget(self.label_51, 0, 6, 1, 1)

        self.label_52 = QLabel(self.groupBoxSteelL3)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_4.addWidget(self.label_52, 1, 4, 1, 1)

        self.label_53 = QLabel(self.groupBoxSteelL3)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_4.addWidget(self.label_53, 2, 4, 1, 1)

        self.label_54 = QLabel(self.groupBoxSteelL3)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_4.addWidget(self.label_54, 1, 6, 1, 1)

        self.lineEditThThTNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThThTNum.setObjectName(u"lineEditThThTNum")
        self.lineEditThThTNum.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThThTNum, 2, 2, 1, 1)

        self.label_55 = QLabel(self.groupBoxSteelL3)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_4.addWidget(self.label_55, 0, 1, 1, 1)

        self.label_56 = QLabel(self.groupBoxSteelL3)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_4.addWidget(self.label_56, 0, 3, 1, 1)

        self.label_57 = QLabel(self.groupBoxSteelL3)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_4.addWidget(self.label_57, 0, 4, 1, 1)

        self.lineEditThTwoMax = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThTwoMax.setObjectName(u"lineEditThTwoMax")
        self.lineEditThTwoMax.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThTwoMax, 1, 7, 1, 1)

        self.label_58 = QLabel(self.groupBoxSteelL3)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_4.addWidget(self.label_58, 0, 8, 1, 1)

        self.labelLevelNumber_12 = QLabel(self.groupBoxSteelL3)
        self.labelLevelNumber_12.setObjectName(u"labelLevelNumber_12")
        self.labelLevelNumber_12.setMargin(10)
        self.labelLevelNumber_12.setIndent(-1)

        self.gridLayout_4.addWidget(self.labelLevelNumber_12, 0, 0, 1, 1)

        self.lineEditThOneMin = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThOneMin.setObjectName(u"lineEditThOneMin")
        self.lineEditThOneMin.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThOneMin, 0, 5, 1, 1)

        self.lineEditThThMax = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThThMax.setObjectName(u"lineEditThThMax")
        self.lineEditThThMax.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThThMax, 2, 7, 1, 1)

        self.lineEditThOneNo = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThOneNo.setObjectName(u"lineEditThOneNo")
        self.lineEditThOneNo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThOneNo, 0, 9, 1, 1)

        self.label_59 = QLabel(self.groupBoxSteelL3)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_4.addWidget(self.label_59, 1, 8, 1, 1)

        self.label_60 = QLabel(self.groupBoxSteelL3)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_4.addWidget(self.label_60, 2, 8, 1, 1)

        self.lineEditThTwoNo = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThTwoNo.setObjectName(u"lineEditThTwoNo")
        self.lineEditThTwoNo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThTwoNo, 1, 9, 1, 1)

        self.lineEditThThNo = QLineEdit(self.groupBoxSteelL3)
        self.lineEditThThNo.setObjectName(u"lineEditThThNo")
        self.lineEditThThNo.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEditThThNo, 2, 9, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout_4)


        self.verticalLayout_5.addWidget(self.groupBoxSteelL3)


        self.verticalLayout_2.addWidget(self.groupBox_7)


        self.verticalLayout_3.addWidget(self.groupBoxStateSL)


        self.verticalLayout_6.addWidget(self.groupBoxStateCls)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBoxSteelType.setText(QCoreApplication.translate("Form", u"Q123", None))
        self.groupBoxStateCls.setTitle("")
        self.checkBoxClassName.setText(QCoreApplication.translate("Form", u"\u5212\u4f24", None))
        self.groupBoxStateSL.setTitle("")
        self.groupBox.setTitle("")
        self.radioButtonSLevel.setText(QCoreApplication.translate("Form", u"\u4e00\u7b49\u54c1", None))
        self.groupBoxSteelL1.setTitle("")
        self.labelLevelNumber_3.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e09", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.labelLevelNumber_2.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e8c", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.labelLevelNumber.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e00:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.groupBox_4.setTitle("")
        self.radioButtonSLevel_2.setText(QCoreApplication.translate("Form", u"\u4e8c\u7b49\u54c1", None))
        self.groupBoxSteelL2.setTitle("")
        self.labelLevelNumber_7.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e09", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.labelLevelNumber_8.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e8c", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label_40.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.labelLevelNumber_9.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e00:", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.groupBox_7.setTitle("")
        self.radioButtonSLevel_3.setText(QCoreApplication.translate("Form", u"\u4e09\u7b49\u54c1", None))
        self.groupBoxSteelL3.setTitle("")
        self.labelLevelNumber_10.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e09", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.labelLevelNumber_11.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e8c", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"\u81f3", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.labelLevelNumber_12.setText(QCoreApplication.translate("Form", u"\u7f3a\u9677\u7b49\u7ea7\u4e00:", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"\u5934\u5c3e\u5ffd\u7565mm", None))
    # retranslateUi

