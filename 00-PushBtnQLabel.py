import sys
import random
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit
from PySide6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        btn = QPushButton('一个点击按钮',self)
        btn.setGeometry(0,0,100,20)
        btn.setToolTip('点我干嘛') 
        btn.setText('重新设置按钮命名')
        btn.clicked.connect(self.hide_some)
        
        self.bl = QLabel('一个文本视图',self)
        self.bl.move(30,30)
        self.bl.setText('你是谁啊')
        self.bl.setToolTip('我是一个标签,不能点击')
        # self.bl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.b2 = QLineEdit(self)
        self.b2.move(60,60)
        
        
        
        
        # le = QLineEdit(self)
        # le.move(100,30)
    def hide_some(self):
        flag = random.choice([0,1])
        self.bl.setHidden(flag)
        print(self.b2.text())
        # self.bl.setHidden(flag)
        
        



if __name__ == '__main__':
    app = QApplication (sys.argv)
    window = MyWindow()
    window.show()

    app.exec()