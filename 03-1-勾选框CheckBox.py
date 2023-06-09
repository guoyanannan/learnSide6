import sys
from Ui_自定义按钮 import Ui_Form
from PySide6.QtWidgets import QApplication,QMainWindow,QCheckBox,QComboBox,QWidget,QVBoxLayout
from PySide6.QtCore import Qt


class MyWindow(QMainWindow,Ui_Form):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        



if __name__ == '__main__':
    app = QApplication (sys.argv)
    window = MyWindow()
    window.show()

    app.exec()