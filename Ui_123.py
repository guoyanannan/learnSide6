# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '123.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(451, 433)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setMinimumSize(QSize(0, 100))
        self.lineEdit.setSizeIncrement(QSize(0, 0))
        self.lineEdit.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(40)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setFrame(True)
        self.lineEdit.setCursorPosition(1)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.pushButton_dot = QPushButton(Form)
        self.pushButton_dot.setObjectName(u"pushButton_dot")

        self.gridLayout.addWidget(self.pushButton_dot, 2, 3, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 2, 0, 1, 1)

        self.pushButton_0 = QPushButton(Form)
        self.pushButton_0.setObjectName(u"pushButton_0")

        self.gridLayout.addWidget(self.pushButton_0, 4, 0, 1, 1)

        self.pushButton_div = QPushButton(Form)
        self.pushButton_div.setObjectName(u"pushButton_div")

        self.gridLayout.addWidget(self.pushButton_div, 3, 3, 1, 1)

        self.pushButton_res = QPushButton(Form)
        self.pushButton_res.setObjectName(u"pushButton_res")

        self.gridLayout.addWidget(self.pushButton_res, 4, 3, 1, 1)

        self.pushButton_9 = QPushButton(Form)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 1, 2, 1, 1)

        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 2, 2, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_8 = QPushButton(Form)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_sub = QPushButton(Form)
        self.pushButton_sub.setObjectName(u"pushButton_sub")

        self.gridLayout.addWidget(self.pushButton_sub, 4, 1, 1, 1)

        self.pushButton_back = QPushButton(Form)
        self.pushButton_back.setObjectName(u"pushButton_back")

        self.gridLayout.addWidget(self.pushButton_back, 1, 3, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.pushButton_add = QPushButton(Form)
        self.pushButton_add.setObjectName(u"pushButton_add")

        self.gridLayout.addWidget(self.pushButton_add, 4, 2, 1, 1)

        self.pushButton_7 = QPushButton(Form)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_cls = QPushButton(Form)
        self.pushButton_cls.setObjectName(u"pushButton_cls")

        self.gridLayout.addWidget(self.pushButton_cls, 0, 1, 1, 3)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u5668", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_dot.setText(QCoreApplication.translate("Form", u"x", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_div.setText(QCoreApplication.translate("Form", u"\u2797", None))
        self.pushButton_res.setText(QCoreApplication.translate("Form", u"=", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.pushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.pushButton_back.setText(QCoreApplication.translate("Form", u"\u56de\u9000", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.pushButton_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.pushButton_cls.setText(QCoreApplication.translate("Form", u"\u6e05\u7a7a", None))
    # retranslateUi

