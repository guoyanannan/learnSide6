
import sys
from typing import Optional
from PySide6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QPushButton,QLineEdit,QMessageBox
from PySide6.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.hlayout = QHBoxLayout()
        self.ptn = QPushButton('按钮')
        self.textInfo = QLineEdit()
        self.hlayout.addWidget(self.ptn)
        self.hlayout.addWidget(self.textInfo)
        
        self.setLayout(self.hlayout)
        self.bind()
    def bind(self):
        self.ptn.clicked.connect(self.messTip)
    
    
    def messTip(self):
        res = QMessageBox.warning(self,'标题','内容',QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Save |
                          QMessageBox.StandardButton.Apply,QMessageBox.StandardButton.Ok)
        
        if res == QMessageBox.StandardButton.Ok:
            print('ok')
        elif res == QMessageBox.StandardButton.No:
            print('No')
        elif res ==QMessageBox.StandardButton.Save:
            print('Save')
        elif res == QMessageBox.StandardButton.Apply:
            print('Apply')
        else:
            print('错误')
            
        self.textInfo.setText('哈哈哈')


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox Example")
        # self.setGeometry(300, 300, 400, 200)
        self.show()
        self.show_message_box()

    def show_message_box(self):
        message_box = QMessageBox()
        message_box.setWindowTitle("Message Box")
        message_box.setText("This is the main message.")
        message_box.setDetailedText("This is the detailed information.")

        message_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message_box.setDefaultButton(QMessageBox.Ok)

        result = message_box.exec()

        if result == QMessageBox.Ok:
            print("Ok button clicked.")
        elif result == QMessageBox.Cancel:
            print("Cancel button clicked.")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    ww = MainWindow()
    app.exec()
