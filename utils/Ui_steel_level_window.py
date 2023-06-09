# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'steel_level_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
from . import gradeIcon_rc

class Ui_FormMain(object):
    def setupUi(self, FormMain):
        if not FormMain.objectName():
            FormMain.setObjectName(u"FormMain")
        FormMain.resize(1205, 654)
        icon = QIcon()
        icon.addFile(u":/btns/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        FormMain.setWindowIcon(icon)
        self.horizontalLayout_11 = QHBoxLayout(FormMain)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButtonParamConfig = QPushButton(FormMain)
        self.pushButtonParamConfig.setObjectName(u"pushButtonParamConfig")
        self.pushButtonParamConfig.setMinimumSize(QSize(117, 0))
        self.pushButtonParamConfig.setStyleSheet(u"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;	\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.pushButtonParamConfig)

        self.pushButtonSteelLevelInfo = QPushButton(FormMain)
        self.pushButtonSteelLevelInfo.setObjectName(u"pushButtonSteelLevelInfo")
        self.pushButtonSteelLevelInfo.setStyleSheet(u"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;	\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.pushButtonSteelLevelInfo)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.stackedWidget = QStackedWidget(FormMain)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(800, 16777215))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEditLeftSteelType = QLineEdit(self.page)
        self.lineEditLeftSteelType.setObjectName(u"lineEditLeftSteelType")
        self.lineEditLeftSteelType.setMinimumSize(QSize(100, 0))
        self.lineEditLeftSteelType.setStyleSheet(u"QLineEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}")

        self.horizontalLayout_8.addWidget(self.lineEditLeftSteelType)

        self.comboBoxCheckLeftClsName = QComboBox(self.page)
        self.comboBoxCheckLeftClsName.setObjectName(u"comboBoxCheckLeftClsName")
        self.comboBoxCheckLeftClsName.setMinimumSize(QSize(116, 0))
        font = QFont()
        font.setPointSize(9)
        self.comboBoxCheckLeftClsName.setFont(font)
        self.comboBoxCheckLeftClsName.setStyleSheet(u"QComboBox:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}")

        self.horizontalLayout_8.addWidget(self.comboBoxCheckLeftClsName)

        self.horizontalSpacer_3 = QSpacerItem(940, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButtonLeftSteelLevel = QRadioButton(self.groupBox)
        self.radioButtonLeftSteelLevel.setObjectName(u"radioButtonLeftSteelLevel")
        self.radioButtonLeftSteelLevel.setCheckable(True)
        self.radioButtonLeftSteelLevel.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButtonLeftSteelLevel)

        self.groupBoxSteelL1 = QGroupBox(self.groupBox)
        self.groupBoxSteelL1.setObjectName(u"groupBoxSteelL1")
        self.groupBoxSteelL1.setStyleSheet(u"QLineEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBoxSteelL1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.lineEditLeftOneTwoTNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneTwoTNum.setObjectName(u"lineEditLeftOneTwoTNum")
        self.lineEditLeftOneTwoTNum.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneTwoTNum, 1, 2, 1, 1)

        self.label_3 = QLabel(self.groupBoxSteelL1)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 6, 1, 1)

        self.labelLevelNumber_3 = QLabel(self.groupBoxSteelL1)
        self.labelLevelNumber_3.setObjectName(u"labelLevelNumber_3")
        self.labelLevelNumber_3.setMargin(10)
        self.labelLevelNumber_3.setIndent(-1)

        self.gridLayout.addWidget(self.labelLevelNumber_3, 2, 0, 1, 1)

        self.labelLevelNumber = QLabel(self.groupBoxSteelL1)
        self.labelLevelNumber.setObjectName(u"labelLevelNumber")
        self.labelLevelNumber.setMargin(10)
        self.labelLevelNumber.setIndent(-1)

        self.gridLayout.addWidget(self.labelLevelNumber, 0, 0, 1, 1)

        self.label_13 = QLabel(self.groupBoxSteelL1)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 10, 1, 1)

        self.lineEditLeftOneOneEdgeNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneOneEdgeNum.setObjectName(u"lineEditLeftOneOneEdgeNum")
        self.lineEditLeftOneOneEdgeNum.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneOneEdgeNum, 0, 5, 1, 1)

        self.lineEditLeftOneThMin = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneThMin.setObjectName(u"lineEditLeftOneThMin")
        self.lineEditLeftOneThMin.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneThMin, 2, 7, 1, 1)

        self.label_2 = QLabel(self.groupBoxSteelL1)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.lineEditLeftOneThTNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneThTNum.setObjectName(u"lineEditLeftOneThTNum")
        self.lineEditLeftOneThTNum.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneThTNum, 2, 2, 1, 1)

        self.label_8 = QLabel(self.groupBoxSteelL1)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 3, 1, 1)

        self.label_12 = QLabel(self.groupBoxSteelL1)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 2, 3, 1, 1)

        self.label_10 = QLabel(self.groupBoxSteelL1)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 2, 8, 1, 1)

        self.lineEditLeftOneThNo = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneThNo.setObjectName(u"lineEditLeftOneThNo")
        self.lineEditLeftOneThNo.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneThNo, 2, 11, 1, 1)

        self.label_4 = QLabel(self.groupBoxSteelL1)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 8, 1, 1)

        self.label_6 = QLabel(self.groupBoxSteelL1)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 8, 1, 1)

        self.lineEditLeftOneOneMin = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneOneMin.setObjectName(u"lineEditLeftOneOneMin")
        self.lineEditLeftOneOneMin.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneOneMin, 0, 7, 1, 1)

        self.label_14 = QLabel(self.groupBoxSteelL1)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 1, 10, 1, 1)

        self.lineEditLeftOneOneTNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneOneTNum.setObjectName(u"lineEditLeftOneOneTNum")
        self.lineEditLeftOneOneTNum.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneOneTNum, 0, 2, 1, 1)

        self.lineEditLeftOneThMax = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneThMax.setObjectName(u"lineEditLeftOneThMax")
        self.lineEditLeftOneThMax.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneThMax, 2, 9, 1, 1)

        self.lineEditLeftOneTwoNo = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneTwoNo.setObjectName(u"lineEditLeftOneTwoNo")
        self.lineEditLeftOneTwoNo.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneTwoNo, 1, 11, 1, 1)

        self.label_15 = QLabel(self.groupBoxSteelL1)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 2, 10, 1, 1)

        self.label_9 = QLabel(self.groupBoxSteelL1)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 6, 1, 1)

        self.label_5 = QLabel(self.groupBoxSteelL1)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 6, 1, 1)

        self.lineEditLeftOneOneMax = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneOneMax.setObjectName(u"lineEditLeftOneOneMax")
        self.lineEditLeftOneOneMax.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneOneMax, 0, 9, 1, 1)

        self.labelLevelNumber_2 = QLabel(self.groupBoxSteelL1)
        self.labelLevelNumber_2.setObjectName(u"labelLevelNumber_2")
        self.labelLevelNumber_2.setMargin(10)
        self.labelLevelNumber_2.setIndent(-1)

        self.gridLayout.addWidget(self.labelLevelNumber_2, 1, 0, 1, 1)

        self.label = QLabel(self.groupBoxSteelL1)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.lineEditLeftOneTwoMax = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneTwoMax.setObjectName(u"lineEditLeftOneTwoMax")
        self.lineEditLeftOneTwoMax.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneTwoMax, 1, 9, 1, 1)

        self.lineEditLeftOneOneNo = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneOneNo.setObjectName(u"lineEditLeftOneOneNo")
        self.lineEditLeftOneOneNo.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneOneNo, 0, 11, 1, 1)

        self.label_16 = QLabel(self.groupBoxSteelL1)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBoxSteelL1)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)

        self.lineEditLeftOneTwoMin = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneTwoMin.setObjectName(u"lineEditLeftOneTwoMin")
        self.lineEditLeftOneTwoMin.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneTwoMin, 1, 7, 1, 1)

        self.lineEditLeftOneTwoEdgeNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneTwoEdgeNum.setObjectName(u"lineEditLeftOneTwoEdgeNum")
        self.lineEditLeftOneTwoEdgeNum.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneTwoEdgeNum, 1, 5, 1, 1)

        self.lineEditLeftOneThEdgeNum = QLineEdit(self.groupBoxSteelL1)
        self.lineEditLeftOneThEdgeNum.setObjectName(u"lineEditLeftOneThEdgeNum")
        self.lineEditLeftOneThEdgeNum.setReadOnly(False)

        self.gridLayout.addWidget(self.lineEditLeftOneThEdgeNum, 2, 5, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_3.addWidget(self.groupBoxSteelL1)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.groupBox_4 = QGroupBox(self.page)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButtonLeftSteelLevel_2 = QRadioButton(self.groupBox_4)
        self.radioButtonLeftSteelLevel_2.setObjectName(u"radioButtonLeftSteelLevel_2")
        self.radioButtonLeftSteelLevel_2.setChecked(True)

        self.verticalLayout_5.addWidget(self.radioButtonLeftSteelLevel_2)

        self.groupBoxSteelL2_2 = QGroupBox(self.groupBox_4)
        self.groupBoxSteelL2_2.setObjectName(u"groupBoxSteelL2_2")
        self.groupBoxSteelL2_2.setStyleSheet(u"QLineEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBoxSteelL2_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(3)
        self.gridLayout_4.setVerticalSpacing(0)
        self.label_46 = QLabel(self.groupBoxSteelL2_2)
        self.label_46.setObjectName(u"label_46")

        self.gridLayout_4.addWidget(self.label_46, 1, 1, 1, 1)

        self.label_47 = QLabel(self.groupBoxSteelL2_2)
        self.label_47.setObjectName(u"label_47")

        self.gridLayout_4.addWidget(self.label_47, 0, 3, 1, 1)

        self.lineEditLeftTwoThMax = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoThMax.setObjectName(u"lineEditLeftTwoThMax")
        self.lineEditLeftTwoThMax.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoThMax, 2, 8, 1, 1)

        self.label_48 = QLabel(self.groupBoxSteelL2_2)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_4.addWidget(self.label_48, 2, 1, 1, 1)

        self.lineEditLeftTwoTwoMax = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoTwoMax.setObjectName(u"lineEditLeftTwoTwoMax")
        self.lineEditLeftTwoTwoMax.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoTwoMax, 1, 8, 1, 1)

        self.label_49 = QLabel(self.groupBoxSteelL2_2)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout_4.addWidget(self.label_49, 0, 5, 1, 1)

        self.label_50 = QLabel(self.groupBoxSteelL2_2)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_4.addWidget(self.label_50, 1, 3, 1, 1)

        self.lineEditLeftTwoOneTNum = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoOneTNum.setObjectName(u"lineEditLeftTwoOneTNum")
        self.lineEditLeftTwoOneTNum.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoOneTNum, 0, 2, 1, 1)

        self.lineEditLeftTwoTwoNo = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoTwoNo.setObjectName(u"lineEditLeftTwoTwoNo")
        self.lineEditLeftTwoTwoNo.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoTwoNo, 1, 10, 1, 1)

        self.labelLevelNumber_10 = QLabel(self.groupBoxSteelL2_2)
        self.labelLevelNumber_10.setObjectName(u"labelLevelNumber_10")
        self.labelLevelNumber_10.setMargin(10)
        self.labelLevelNumber_10.setIndent(-1)

        self.gridLayout_4.addWidget(self.labelLevelNumber_10, 2, 0, 1, 1)

        self.label_51 = QLabel(self.groupBoxSteelL2_2)
        self.label_51.setObjectName(u"label_51")

        self.gridLayout_4.addWidget(self.label_51, 1, 7, 1, 1)

        self.label_52 = QLabel(self.groupBoxSteelL2_2)
        self.label_52.setObjectName(u"label_52")

        self.gridLayout_4.addWidget(self.label_52, 0, 1, 1, 1)

        self.lineEditLeftTwoThMin = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoThMin.setObjectName(u"lineEditLeftTwoThMin")
        self.lineEditLeftTwoThMin.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoThMin, 2, 6, 1, 1)

        self.label_53 = QLabel(self.groupBoxSteelL2_2)
        self.label_53.setObjectName(u"label_53")

        self.gridLayout_4.addWidget(self.label_53, 1, 5, 1, 1)

        self.label_54 = QLabel(self.groupBoxSteelL2_2)
        self.label_54.setObjectName(u"label_54")

        self.gridLayout_4.addWidget(self.label_54, 2, 9, 1, 1)

        self.label_55 = QLabel(self.groupBoxSteelL2_2)
        self.label_55.setObjectName(u"label_55")

        self.gridLayout_4.addWidget(self.label_55, 2, 7, 1, 1)

        self.label_56 = QLabel(self.groupBoxSteelL2_2)
        self.label_56.setObjectName(u"label_56")

        self.gridLayout_4.addWidget(self.label_56, 2, 3, 1, 1)

        self.lineEditLeftTwoThTNum = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoThTNum.setObjectName(u"lineEditLeftTwoThTNum")
        self.lineEditLeftTwoThTNum.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoThTNum, 2, 2, 1, 1)

        self.lineEditLeftTwoOneMax = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoOneMax.setObjectName(u"lineEditLeftTwoOneMax")
        self.lineEditLeftTwoOneMax.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoOneMax, 0, 8, 1, 1)

        self.lineEditLeftTwoThNo = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoThNo.setObjectName(u"lineEditLeftTwoThNo")
        self.lineEditLeftTwoThNo.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoThNo, 2, 10, 1, 1)

        self.lineEditLeftTwoTwoMin = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoTwoMin.setObjectName(u"lineEditLeftTwoTwoMin")
        self.lineEditLeftTwoTwoMin.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoTwoMin, 1, 6, 1, 1)

        self.label_57 = QLabel(self.groupBoxSteelL2_2)
        self.label_57.setObjectName(u"label_57")

        self.gridLayout_4.addWidget(self.label_57, 0, 7, 1, 1)

        self.lineEditLeftTwoTwoTNum = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoTwoTNum.setObjectName(u"lineEditLeftTwoTwoTNum")
        self.lineEditLeftTwoTwoTNum.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoTwoTNum, 1, 2, 1, 1)

        self.lineEditLeftTwoOneMin = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoOneMin.setObjectName(u"lineEditLeftTwoOneMin")
        self.lineEditLeftTwoOneMin.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoOneMin, 0, 6, 1, 1)

        self.lineEditLeftTwoOneNo = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoOneNo.setObjectName(u"lineEditLeftTwoOneNo")
        self.lineEditLeftTwoOneNo.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoOneNo, 0, 10, 1, 1)

        self.label_58 = QLabel(self.groupBoxSteelL2_2)
        self.label_58.setObjectName(u"label_58")

        self.gridLayout_4.addWidget(self.label_58, 0, 9, 1, 1)

        self.labelLevelNumber_11 = QLabel(self.groupBoxSteelL2_2)
        self.labelLevelNumber_11.setObjectName(u"labelLevelNumber_11")
        self.labelLevelNumber_11.setMargin(10)
        self.labelLevelNumber_11.setIndent(-1)

        self.gridLayout_4.addWidget(self.labelLevelNumber_11, 0, 0, 1, 1)

        self.label_59 = QLabel(self.groupBoxSteelL2_2)
        self.label_59.setObjectName(u"label_59")

        self.gridLayout_4.addWidget(self.label_59, 1, 9, 1, 1)

        self.label_60 = QLabel(self.groupBoxSteelL2_2)
        self.label_60.setObjectName(u"label_60")

        self.gridLayout_4.addWidget(self.label_60, 2, 5, 1, 1)

        self.labelLevelNumber_12 = QLabel(self.groupBoxSteelL2_2)
        self.labelLevelNumber_12.setObjectName(u"labelLevelNumber_12")
        self.labelLevelNumber_12.setMargin(10)
        self.labelLevelNumber_12.setIndent(-1)

        self.gridLayout_4.addWidget(self.labelLevelNumber_12, 1, 0, 1, 1)

        self.lineEditLeftTwoOneEdgeNum = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoOneEdgeNum.setObjectName(u"lineEditLeftTwoOneEdgeNum")
        self.lineEditLeftTwoOneEdgeNum.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoOneEdgeNum, 0, 4, 1, 1)

        self.lineEditLeftTwoTwoEdgeNum = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoTwoEdgeNum.setObjectName(u"lineEditLeftTwoTwoEdgeNum")
        self.lineEditLeftTwoTwoEdgeNum.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoTwoEdgeNum, 1, 4, 1, 1)

        self.lineEditLeftTwoThEdgeNum = QLineEdit(self.groupBoxSteelL2_2)
        self.lineEditLeftTwoThEdgeNum.setObjectName(u"lineEditLeftTwoThEdgeNum")
        self.lineEditLeftTwoThEdgeNum.setReadOnly(False)

        self.gridLayout_4.addWidget(self.lineEditLeftTwoThEdgeNum, 2, 4, 1, 1)


        self.horizontalLayout_6.addLayout(self.gridLayout_4)


        self.verticalLayout_5.addWidget(self.groupBoxSteelL2_2)


        self.verticalLayout_7.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.page)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(0, 0))
        self.groupBox_7.setMaximumSize(QSize(800, 16777215))
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.radioButtonLeftSteelLevel_3 = QRadioButton(self.groupBox_7)
        self.radioButtonLeftSteelLevel_3.setObjectName(u"radioButtonLeftSteelLevel_3")
        self.radioButtonLeftSteelLevel_3.setChecked(True)

        self.verticalLayout_6.addWidget(self.radioButtonLeftSteelLevel_3)

        self.groupBoxSteelL3 = QGroupBox(self.groupBox_7)
        self.groupBoxSteelL3.setObjectName(u"groupBoxSteelL3")
        self.groupBoxSteelL3.setStyleSheet(u"QLineEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBoxSteelL3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(3)
        self.gridLayout_5.setVerticalSpacing(0)
        self.label_61 = QLabel(self.groupBoxSteelL3)
        self.label_61.setObjectName(u"label_61")

        self.gridLayout_5.addWidget(self.label_61, 0, 9, 1, 1)

        self.label_62 = QLabel(self.groupBoxSteelL3)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_5.addWidget(self.label_62, 2, 1, 1, 1)

        self.lineEditLeftThOneTNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThOneTNum.setObjectName(u"lineEditLeftThOneTNum")
        self.lineEditLeftThOneTNum.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThOneTNum, 0, 2, 1, 1)

        self.label_63 = QLabel(self.groupBoxSteelL3)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_5.addWidget(self.label_63, 1, 3, 1, 1)

        self.lineEditLeftThOneMax = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThOneMax.setObjectName(u"lineEditLeftThOneMax")
        self.lineEditLeftThOneMax.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThOneMax, 0, 8, 1, 1)

        self.lineEditLeftThTwoTNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThTwoTNum.setObjectName(u"lineEditLeftThTwoTNum")
        self.lineEditLeftThTwoTNum.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThTwoTNum, 1, 2, 1, 1)

        self.label_64 = QLabel(self.groupBoxSteelL3)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_5.addWidget(self.label_64, 1, 7, 1, 1)

        self.lineEditLeftThThMax = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThThMax.setObjectName(u"lineEditLeftThThMax")
        self.lineEditLeftThThMax.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThThMax, 2, 8, 1, 1)

        self.label_65 = QLabel(self.groupBoxSteelL3)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_5.addWidget(self.label_65, 2, 3, 1, 1)

        self.labelLevelNumber_13 = QLabel(self.groupBoxSteelL3)
        self.labelLevelNumber_13.setObjectName(u"labelLevelNumber_13")
        self.labelLevelNumber_13.setMargin(10)
        self.labelLevelNumber_13.setIndent(-1)

        self.gridLayout_5.addWidget(self.labelLevelNumber_13, 1, 0, 1, 1)

        self.labelLevelNumber_14 = QLabel(self.groupBoxSteelL3)
        self.labelLevelNumber_14.setObjectName(u"labelLevelNumber_14")
        self.labelLevelNumber_14.setMargin(10)
        self.labelLevelNumber_14.setIndent(-1)

        self.gridLayout_5.addWidget(self.labelLevelNumber_14, 2, 0, 1, 1)

        self.labelLevelNumber_15 = QLabel(self.groupBoxSteelL3)
        self.labelLevelNumber_15.setObjectName(u"labelLevelNumber_15")
        self.labelLevelNumber_15.setMargin(10)
        self.labelLevelNumber_15.setIndent(-1)

        self.gridLayout_5.addWidget(self.labelLevelNumber_15, 0, 0, 1, 1)

        self.label_66 = QLabel(self.groupBoxSteelL3)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_5.addWidget(self.label_66, 0, 1, 1, 1)

        self.lineEditLeftThOneMin = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThOneMin.setObjectName(u"lineEditLeftThOneMin")
        self.lineEditLeftThOneMin.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThOneMin, 0, 6, 1, 1)

        self.lineEditLeftThTwoNo = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThTwoNo.setObjectName(u"lineEditLeftThTwoNo")
        self.lineEditLeftThTwoNo.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThTwoNo, 1, 10, 1, 1)

        self.lineEditLeftThOneNo = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThOneNo.setObjectName(u"lineEditLeftThOneNo")
        self.lineEditLeftThOneNo.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThOneNo, 0, 10, 1, 1)

        self.label_67 = QLabel(self.groupBoxSteelL3)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_5.addWidget(self.label_67, 1, 9, 1, 1)

        self.label_68 = QLabel(self.groupBoxSteelL3)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_5.addWidget(self.label_68, 2, 9, 1, 1)

        self.lineEditLeftThThNo = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThThNo.setObjectName(u"lineEditLeftThThNo")
        self.lineEditLeftThThNo.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThThNo, 2, 10, 1, 1)

        self.label_69 = QLabel(self.groupBoxSteelL3)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_5.addWidget(self.label_69, 1, 5, 1, 1)

        self.lineEditLeftThTwoMin = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThTwoMin.setObjectName(u"lineEditLeftThTwoMin")
        self.lineEditLeftThTwoMin.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThTwoMin, 1, 6, 1, 1)

        self.label_70 = QLabel(self.groupBoxSteelL3)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_5.addWidget(self.label_70, 2, 5, 1, 1)

        self.label_71 = QLabel(self.groupBoxSteelL3)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_5.addWidget(self.label_71, 0, 7, 1, 1)

        self.lineEditLeftThThTNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThThTNum.setObjectName(u"lineEditLeftThThTNum")
        self.lineEditLeftThThTNum.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThThTNum, 2, 2, 1, 1)

        self.label_72 = QLabel(self.groupBoxSteelL3)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_5.addWidget(self.label_72, 0, 3, 1, 1)

        self.lineEditLeftThThMin = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThThMin.setObjectName(u"lineEditLeftThThMin")
        self.lineEditLeftThThMin.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThThMin, 2, 6, 1, 1)

        self.label_73 = QLabel(self.groupBoxSteelL3)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_5.addWidget(self.label_73, 2, 7, 1, 1)

        self.label_74 = QLabel(self.groupBoxSteelL3)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_5.addWidget(self.label_74, 0, 5, 1, 1)

        self.lineEditLeftThTwoMax = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThTwoMax.setObjectName(u"lineEditLeftThTwoMax")
        self.lineEditLeftThTwoMax.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThTwoMax, 1, 8, 1, 1)

        self.label_75 = QLabel(self.groupBoxSteelL3)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_5.addWidget(self.label_75, 1, 1, 1, 1)

        self.lineEditLeftThOneEdgeNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThOneEdgeNum.setObjectName(u"lineEditLeftThOneEdgeNum")
        self.lineEditLeftThOneEdgeNum.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThOneEdgeNum, 0, 4, 1, 1)

        self.lineEditLeftThTwoEdgeNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThTwoEdgeNum.setObjectName(u"lineEditLeftThTwoEdgeNum")
        self.lineEditLeftThTwoEdgeNum.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThTwoEdgeNum, 1, 4, 1, 1)

        self.lineEditLeftThThEdgeNum = QLineEdit(self.groupBoxSteelL3)
        self.lineEditLeftThThEdgeNum.setObjectName(u"lineEditLeftThThEdgeNum")
        self.lineEditLeftThThEdgeNum.setReadOnly(False)

        self.gridLayout_5.addWidget(self.lineEditLeftThThEdgeNum, 2, 4, 1, 1)


        self.horizontalLayout_7.addLayout(self.gridLayout_5)


        self.verticalLayout_6.addWidget(self.groupBoxSteelL3)


        self.verticalLayout_7.addWidget(self.groupBox_7)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.pushButtonToParamShow = QPushButton(self.page)
        self.pushButtonToParamShow.setObjectName(u"pushButtonToParamShow")
        self.pushButtonToParamShow.setMinimumSize(QSize(116, 0))
        self.pushButtonToParamShow.setFocusPolicy(Qt.NoFocus)
        self.pushButtonToParamShow.setStyleSheet(u"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;	\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/btns/icon/\u53f3\u7bad\u5934.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonToParamShow.setIcon(icon1)
        self.pushButtonToParamShow.setCheckable(False)
        self.pushButtonToParamShow.setChecked(False)
        self.pushButtonToParamShow.setAutoDefault(False)
        self.pushButtonToParamShow.setFlat(False)

        self.horizontalLayout_9.addWidget(self.pushButtonToParamShow)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_8 = QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dateTimeEditStart = QDateTimeEdit(self.page_2)
        self.dateTimeEditStart.setObjectName(u"dateTimeEditStart")
        self.dateTimeEditStart.setStyleSheet(u"QDateTimeEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}")
        self.dateTimeEditStart.setWrapping(False)
        self.dateTimeEditStart.setAccelerated(False)
        self.dateTimeEditStart.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.dateTimeEditStart.setDate(QDate(2023, 1, 1))
        self.dateTimeEditStart.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateTimeEditStart.setCalendarPopup(True)
        self.dateTimeEditStart.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_3.addWidget(self.dateTimeEditStart)

        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_3.addWidget(self.label_11)

        self.dateTimeEditEnd = QDateTimeEdit(self.page_2)
        self.dateTimeEditEnd.setObjectName(u"dateTimeEditEnd")
        self.dateTimeEditEnd.setStyleSheet(u"QDateTimeEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}")
        self.dateTimeEditEnd.setWrapping(False)
        self.dateTimeEditEnd.setAccelerated(False)
        self.dateTimeEditEnd.setDateTime(QDateTime(QDate(2023, 1, 1), QTime(0, 0, 0)))
        self.dateTimeEditEnd.setDate(QDate(2023, 1, 1))
        self.dateTimeEditEnd.setCurrentSection(QDateTimeEdit.YearSection)
        self.dateTimeEditEnd.setCalendarPopup(True)
        self.dateTimeEditEnd.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_3.addWidget(self.dateTimeEditEnd)

        self.pushButtonSearch = QPushButton(self.page_2)
        self.pushButtonSearch.setObjectName(u"pushButtonSearch")
        self.pushButtonSearch.setFocusPolicy(Qt.NoFocus)
        self.pushButtonSearch.setStyleSheet(u"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;	\n"
"}\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/btns/icon/\u6570\u636e\u67e5\u8be2,\u6570\u636e\u5e93\u67e5\u8be2.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSearch.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.pushButtonSearch)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)

        self.plainTextEditSearch = QPlainTextEdit(self.page_2)
        self.plainTextEditSearch.setObjectName(u"plainTextEditSearch")
        self.plainTextEditSearch.setMinimumSize(QSize(0, 150))
        self.plainTextEditSearch.setStyleSheet(u"QPlainTextEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}")
        self.plainTextEditSearch.setReadOnly(True)

        self.verticalLayout_8.addWidget(self.plainTextEditSearch)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_6 = QPushButton(self.page_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgba(255, 255, 255,0);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/btns/icon/\u63d0\u793a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon3)
        self.pushButton_6.setCheckable(False)
        self.pushButton_6.setAutoDefault(False)
        self.pushButton_6.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.plainTextEditLog = QPlainTextEdit(self.page_2)
        self.plainTextEditLog.setObjectName(u"plainTextEditLog")
        self.plainTextEditLog.setMinimumSize(QSize(800, 300))
        self.plainTextEditLog.setStyleSheet(u"QPlainTextEdit:hover{\n"
"	border : 1px solid #ffaa00;\n"
"}")
        self.plainTextEditLog.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEditLog)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.page_2)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.horizontalLayout_11.addLayout(self.verticalLayout_9)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scrollArea = QScrollArea(FormMain)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(260, 300))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 375, 600))
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widgetScrollArea = QWidget(self.scrollAreaWidgetContents)
        self.widgetScrollArea.setObjectName(u"widgetScrollArea")

        self.verticalLayout_10.addWidget(self.widgetScrollArea)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonRun = QPushButton(FormMain)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        self.pushButtonRun.setFocusPolicy(Qt.NoFocus)
        self.pushButtonRun.setStyleSheet(u"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;	\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/btns/icon/\u8d5e\u505c.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonRun.setIcon(icon4)

        self.horizontalLayout.addWidget(self.pushButtonRun)

        self.pushButtonKill = QPushButton(FormMain)
        self.pushButtonKill.setObjectName(u"pushButtonKill")
        self.pushButtonKill.setFocusPolicy(Qt.NoFocus)
        self.pushButtonKill.setStyleSheet(u"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;	\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/btns/icon/\u505c\u6b62.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonKill.setIcon(icon5)

        self.horizontalLayout.addWidget(self.pushButtonKill)

        self.pushButtonSave = QPushButton(FormMain)
        self.pushButtonSave.setObjectName(u"pushButtonSave")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonSave.sizePolicy().hasHeightForWidth())
        self.pushButtonSave.setSizePolicy(sizePolicy1)
        self.pushButtonSave.setMinimumSize(QSize(0, 0))
        self.pushButtonSave.setFocusPolicy(Qt.NoFocus)
        self.pushButtonSave.setStyleSheet(u"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;	\n"
"}\n"
"\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/btns/icon/\u4fdd\u5b58.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButtonSave.setIcon(icon6)
        self.pushButtonSave.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.pushButtonSave)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_11.addLayout(self.verticalLayout)


        self.retranslateUi(FormMain)

        self.stackedWidget.setCurrentIndex(0)
        self.pushButtonToParamShow.setDefault(False)
        self.pushButton_6.setDefault(False)
        self.pushButtonSave.setDefault(False)


        QMetaObject.connectSlotsByName(FormMain)
    # setupUi

    def retranslateUi(self, FormMain):
        FormMain.setWindowTitle(QCoreApplication.translate("FormMain", u"\u8d28\u91cf\u5224\u5b9a", None))
#if QT_CONFIG(tooltip)
        FormMain.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pushButtonParamConfig.setToolTip(QCoreApplication.translate("FormMain", u"\u70b9\u51fb\u5207\u6362\u914d\u7f6e\u9875\u9762", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonParamConfig.setText(QCoreApplication.translate("FormMain", u"\u914d\u7f6e\u53c2\u6570", None))
#if QT_CONFIG(tooltip)
        self.pushButtonSteelLevelInfo.setToolTip(QCoreApplication.translate("FormMain", u"<html><head/><body><p>\u70b9\u51fb\u5207\u6362\u5224\u5b9a\u7ed3\u679c\u9875\u9762</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSteelLevelInfo.setText(QCoreApplication.translate("FormMain", u"\u94a2\u5377\u8d28\u91cf\u5224\u5b9a\u4fe1\u606f", None))
        self.lineEditLeftSteelType.setPlaceholderText(QCoreApplication.translate("FormMain", u"\u8bf7\u8f93\u5165\u94a2\u79cd\u4ee3\u7801", None))
        self.comboBoxCheckLeftClsName.setPlaceholderText(QCoreApplication.translate("FormMain", u"\u8bf7\u9009\u62e9\u7f3a\u9677\u7c7b\u578b", None))
        self.groupBox.setTitle("")
        self.radioButtonLeftSteelLevel.setText(QCoreApplication.translate("FormMain", u"\u4e00\u7b49\u54c1", None))
        self.groupBoxSteelL1.setTitle("")
        self.label_3.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.labelLevelNumber_3.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e09", None))
        self.labelLevelNumber.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e00:", None))
        self.label_13.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_2.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_8.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_12.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_10.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_4.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_6.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_14.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_15.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_9.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_5.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.labelLevelNumber_2.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e8c", None))
        self.label.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_16.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_7.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
        self.groupBox_4.setTitle("")
        self.radioButtonLeftSteelLevel_2.setText(QCoreApplication.translate("FormMain", u"\u4e8c\u7b49\u54c1", None))
        self.groupBoxSteelL2_2.setTitle("")
        self.label_46.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_47.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_48.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_49.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_50.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.labelLevelNumber_10.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e09", None))
        self.label_51.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_52.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_53.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_54.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_55.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_56.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_57.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_58.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.labelLevelNumber_11.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e00:", None))
        self.label_59.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_60.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.labelLevelNumber_12.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e8c", None))
        self.groupBox_7.setTitle("")
        self.radioButtonLeftSteelLevel_3.setText(QCoreApplication.translate("FormMain", u"\u4e09\u7b49\u54c1", None))
        self.groupBoxSteelL3.setTitle("")
        self.label_61.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_62.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_63.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_64.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_65.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.labelLevelNumber_13.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e8c", None))
        self.labelLevelNumber_14.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e09", None))
        self.labelLevelNumber_15.setText(QCoreApplication.translate("FormMain", u"\u7f3a\u9677\u7b49\u7ea7\u4e00:", None))
        self.label_66.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
        self.label_67.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_68.setText(QCoreApplication.translate("FormMain", u"\u5934\u5c3e\u5ffd\u7565mm", None))
        self.label_69.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_70.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_71.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_72.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u90e8\u6570\u91cf:", None))
        self.label_73.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
        self.label_74.setText(QCoreApplication.translate("FormMain", u"\u8fb9\u8ddd\u533a\u95f4mm:", None))
        self.label_75.setText(QCoreApplication.translate("FormMain", u"\u6574\u4f53\u6570\u91cf:", None))
#if QT_CONFIG(tooltip)
        self.pushButtonToParamShow.setToolTip(QCoreApplication.translate("FormMain", u"\u70b9\u51fb\u63a8\u9001\u5f53\u524d\u8bbe\u7f6e\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonToParamShow.setText("")
        self.label_11.setText(QCoreApplication.translate("FormMain", u"\u81f3", None))
#if QT_CONFIG(tooltip)
        self.pushButtonSearch.setToolTip(QCoreApplication.translate("FormMain", u"\u70b9\u51fb\u67e5\u8be2\u94a2\u5377\u5224\u7ea7\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSearch.setText("")
        self.pushButton_6.setText(QCoreApplication.translate("FormMain", u"\u94a2\u5377\u8d28\u91cf\u5224\u5b9a\u660e\u7ec6", None))
        self.plainTextEditLog.setPlainText("")
#if QT_CONFIG(tooltip)
        self.pushButtonRun.setToolTip(QCoreApplication.translate("FormMain", u"\u70b9\u51fb\u5f00\u59cb\u8fd0\u884c\u5224\u7ea7\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRun.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonKill.setToolTip(QCoreApplication.translate("FormMain", u"\u70b9\u51fb\u4e2d\u65ad\u5224\u7ea7\u7a0b\u5e8f", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonKill.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonSave.setToolTip(QCoreApplication.translate("FormMain", u"\u70b9\u51fb\u4fdd\u5b58\u5224\u7ea7\u914d\u7f6e\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSave.setText("")
    # retranslateUi

