# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '自定义按钮.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(591, 550)
        Form.setMouseTracking(True)
        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(180, 170, 171, 101))
        self.checkBox.setStyleSheet(u"QCheckBox:indicator{\n"
                                    "	width: 0;\n"
                                    "}\n"
                                    "QCheckBox{\n"
                                    "	border: 1px solid red;\n"
                                    "}\n"
                                    "QCheckBox:pressed{\n"
                                    "	\n"
                                    "	color: rgba(255, 255, 255,0);\n"
                                    "}\n"
                                    "")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u81ea\u5b9a\u4e49\u9009\u62e9\u6309\u94ae", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"CheckBox", None))
    # retranslateUi

