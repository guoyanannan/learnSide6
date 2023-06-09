# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'steel_info.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLabel,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_FormLevel(object):
    def setupUi(self, FormLevel):
        if not FormLevel.objectName():
            FormLevel.setObjectName(u"FormLevel")
        FormLevel.resize(403, 689)
        self.verticalLayout = QVBoxLayout(FormLevel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBoxClsName = QCheckBox(FormLevel)
        self.checkBoxClsName.setObjectName(u"checkBoxClsName")

        self.verticalLayout.addWidget(self.checkBoxClsName)

        self.checkBoxSteelID = QCheckBox(FormLevel)
        self.checkBoxSteelID.setObjectName(u"checkBoxSteelID")
        self.checkBoxSteelID.setEnabled(True)
        self.checkBoxSteelID.setStyleSheet(u"QCheckBox{\n"
"	margin-left:15px;\n"
"}")

        self.verticalLayout.addWidget(self.checkBoxSteelID)

        self.groupBox_2 = QGroupBox(FormLevel)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setStyleSheet(u"QGroupBox{\n"
"	margin-left:30px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.radioButtonLevel = QRadioButton(self.groupBox_2)
        self.radioButtonLevel.setObjectName(u"radioButtonLevel")

        self.verticalLayout_3.addWidget(self.radioButtonLevel)

        self.labelLevelNumber = QLabel(self.groupBox_2)
        self.labelLevelNumber.setObjectName(u"labelLevelNumber")
        self.labelLevelNumber.setMargin(10)
        self.labelLevelNumber.setIndent(-1)

        self.verticalLayout_3.addWidget(self.labelLevelNumber)

        self.labelLevelMinEdge = QLabel(self.groupBox_2)
        self.labelLevelMinEdge.setObjectName(u"labelLevelMinEdge")
        self.labelLevelMinEdge.setMargin(10)
        self.labelLevelMinEdge.setIndent(-1)

        self.verticalLayout_3.addWidget(self.labelLevelMinEdge)

        self.labelLevelMaxEdge = QLabel(self.groupBox_2)
        self.labelLevelMaxEdge.setObjectName(u"labelLevelMaxEdge")
        self.labelLevelMaxEdge.setMargin(10)
        self.labelLevelMaxEdge.setIndent(-1)

        self.verticalLayout_3.addWidget(self.labelLevelMaxEdge)

        self.labelLevelEdgeNumber = QLabel(self.groupBox_2)
        self.labelLevelEdgeNumber.setObjectName(u"labelLevelEdgeNumber")
        self.labelLevelEdgeNumber.setMargin(10)

        self.verticalLayout_3.addWidget(self.labelLevelEdgeNumber)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(FormLevel)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"QGroupBox{\n"
"	margin-left:30px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.radioButtonLevel2 = QRadioButton(self.groupBox_3)
        self.radioButtonLevel2.setObjectName(u"radioButtonLevel2")

        self.verticalLayout_4.addWidget(self.radioButtonLevel2)

        self.labelLevel2Number = QLabel(self.groupBox_3)
        self.labelLevel2Number.setObjectName(u"labelLevel2Number")
        self.labelLevel2Number.setMargin(10)
        self.labelLevel2Number.setIndent(-1)

        self.verticalLayout_4.addWidget(self.labelLevel2Number)

        self.labelLevel2MinEdge = QLabel(self.groupBox_3)
        self.labelLevel2MinEdge.setObjectName(u"labelLevel2MinEdge")
        self.labelLevel2MinEdge.setMargin(10)
        self.labelLevel2MinEdge.setIndent(-1)

        self.verticalLayout_4.addWidget(self.labelLevel2MinEdge)

        self.labelLevel2MaxEdge = QLabel(self.groupBox_3)
        self.labelLevel2MaxEdge.setObjectName(u"labelLevel2MaxEdge")
        self.labelLevel2MaxEdge.setMargin(10)
        self.labelLevel2MaxEdge.setIndent(-1)

        self.verticalLayout_4.addWidget(self.labelLevel2MaxEdge)

        self.labelLevel2EdgeNumber = QLabel(self.groupBox_3)
        self.labelLevel2EdgeNumber.setObjectName(u"labelLevel2EdgeNumber")
        self.labelLevel2EdgeNumber.setMargin(10)

        self.verticalLayout_4.addWidget(self.labelLevel2EdgeNumber)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(FormLevel)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setStyleSheet(u"QGroupBox{\n"
"	margin-left:30px;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.radioButtonLevel3 = QRadioButton(self.groupBox_4)
        self.radioButtonLevel3.setObjectName(u"radioButtonLevel3")

        self.verticalLayout_5.addWidget(self.radioButtonLevel3)

        self.labelLevel3Number = QLabel(self.groupBox_4)
        self.labelLevel3Number.setObjectName(u"labelLevel3Number")
        self.labelLevel3Number.setMargin(10)
        self.labelLevel3Number.setIndent(-1)

        self.verticalLayout_5.addWidget(self.labelLevel3Number)

        self.labelLevel3MinEdge = QLabel(self.groupBox_4)
        self.labelLevel3MinEdge.setObjectName(u"labelLevel3MinEdge")
        self.labelLevel3MinEdge.setMargin(10)
        self.labelLevel3MinEdge.setIndent(-1)

        self.verticalLayout_5.addWidget(self.labelLevel3MinEdge)

        self.labelLevel3MaxEdge = QLabel(self.groupBox_4)
        self.labelLevel3MaxEdge.setObjectName(u"labelLevel3MaxEdge")
        self.labelLevel3MaxEdge.setMargin(10)
        self.labelLevel3MaxEdge.setIndent(-1)

        self.verticalLayout_5.addWidget(self.labelLevel3MaxEdge)

        self.labelLevel3EdgeNumber = QLabel(self.groupBox_4)
        self.labelLevel3EdgeNumber.setObjectName(u"labelLevel3EdgeNumber")
        self.labelLevel3EdgeNumber.setMargin(10)

        self.verticalLayout_5.addWidget(self.labelLevel3EdgeNumber)


        self.verticalLayout.addWidget(self.groupBox_4)


        self.retranslateUi(FormLevel)

        QMetaObject.connectSlotsByName(FormLevel)
    # setupUi

    def retranslateUi(self, FormLevel):
        FormLevel.setWindowTitle(QCoreApplication.translate("FormLevel", u"Form", None))
        self.checkBoxClsName.setText(QCoreApplication.translate("FormLevel", u"\u710a\u7f1d", None))
        self.checkBoxSteelID.setText(QCoreApplication.translate("FormLevel", u"Q123", None))
        self.groupBox_2.setTitle("")
        self.radioButtonLevel.setText(QCoreApplication.translate("FormLevel", u"\u4e00\u7b49\u54c1", None))
        self.labelLevelNumber.setText(QCoreApplication.translate("FormLevel", u"\u6700\u5927\u6570\u91cf:20", None))
        self.labelLevelMinEdge.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5c0f\u503cmm:20", None))
        self.labelLevelMaxEdge.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5927\u503cmm:20", None))
        self.labelLevelEdgeNumber.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5927\u6570\u91cf:30", None))
        self.groupBox_3.setTitle("")
        self.radioButtonLevel2.setText(QCoreApplication.translate("FormLevel", u"\u4e8c\u7b49\u54c1", None))
        self.labelLevel2Number.setText(QCoreApplication.translate("FormLevel", u"\u6700\u5927\u6570\u91cf:20", None))
        self.labelLevel2MinEdge.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5c0f\u503cmm:20", None))
        self.labelLevel2MaxEdge.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5927\u503cmm:20", None))
        self.labelLevel2EdgeNumber.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5927\u6570\u91cf:30", None))
        self.groupBox_4.setTitle("")
        self.radioButtonLevel3.setText(QCoreApplication.translate("FormLevel", u"\u4e09\u7b49\u54c1", None))
        self.labelLevel3Number.setText(QCoreApplication.translate("FormLevel", u"\u6700\u5927\u6570\u91cf:20", None))
        self.labelLevel3MinEdge.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5c0f\u503cmm:20", None))
        self.labelLevel3MaxEdge.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5927\u503cmm:20", None))
        self.labelLevel3EdgeNumber.setText(QCoreApplication.translate("FormLevel", u"\u8ddd\u8fb9\u6700\u5927\u6570\u91cf:30", None))
    # retranslateUi

