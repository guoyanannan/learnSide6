# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '单位换算.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(354, 203)
        Form.setStyleSheet(u"QComboBox{\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"QLineEdit:hover{\n"
"    \n"
"    background-color: rgb(85, 170, 255);\n"
"}")
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBoxOneDtype = QComboBox(Form)
        self.comboBoxOneDtype.setObjectName(u"comboBoxOneDtype")
        self.comboBoxOneDtype.setMinimumSize(QSize(170, 40))

        self.gridLayout.addWidget(self.comboBoxOneDtype, 3, 1, 1, 1)

        self.labelOriginData = QLabel(Form)
        self.labelOriginData.setObjectName(u"labelOriginData")
        self.labelOriginData.setMinimumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(15)
        self.labelOriginData.setFont(font)
        self.labelOriginData.setCursor(QCursor(Qt.IBeamCursor))

        self.gridLayout.addWidget(self.labelOriginData, 0, 0, 1, 1)

        self.lineEditInputOne = QLineEdit(Form)
        self.lineEditInputOne.setObjectName(u"lineEditInputOne")
        self.lineEditInputOne.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.lineEditInputOne, 3, 0, 1, 1)

        self.comboBoxTwoDtype = QComboBox(Form)
        self.comboBoxTwoDtype.setObjectName(u"comboBoxTwoDtype")
        self.comboBoxTwoDtype.setMinimumSize(QSize(0, 40))

        self.gridLayout.addWidget(self.comboBoxTwoDtype, 4, 1, 1, 1)

        self.labelTransformData = QLabel(Form)
        self.labelTransformData.setObjectName(u"labelTransformData")
        self.labelTransformData.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.labelTransformData.setFont(font1)
        self.labelTransformData.setCursor(QCursor(Qt.IBeamCursor))

        self.gridLayout.addWidget(self.labelTransformData, 1, 0, 1, 1)

        self.lineEditInputTwo = QLineEdit(Form)
        self.lineEditInputTwo.setObjectName(u"lineEditInputTwo")
        self.lineEditInputTwo.setMinimumSize(QSize(0, 40))
        self.lineEditInputTwo.setSizeIncrement(QSize(0, 0))

        self.gridLayout.addWidget(self.lineEditInputTwo, 4, 0, 1, 1)

        self.comboBoxDType = QComboBox(Form)
        self.comboBoxDType.setObjectName(u"comboBoxDType")
        self.comboBoxDType.setStyleSheet(u"#ComboBoxDtype{\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"#ComboBoxDtype:hover{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.comboBoxDType, 2, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8f6c\u6362\u5668", None))
        self.labelOriginData.setText(QCoreApplication.translate("Form", u"1 \u7c73=", None))
        self.labelTransformData.setText(QCoreApplication.translate("Form", u"1 \u7c73", None))
    # retranslateUi

