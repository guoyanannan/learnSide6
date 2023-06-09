import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit,QComboBox,QWidget,QVBoxLayout
from PySide6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('下拉框')
        w = QWidget()
        layout = QVBoxLayout()
        self.cbb = QComboBox()
        self.cbb.addItem('1')
        self.cbb.addItem('2')
        self.cbb.addItem('3')
        
        self.cbb.activated.connect(self.printInd)
        
        layout.addWidget(self.cbb)
        w.setLayout(layout)
        
        self.setCentralWidget(w)
        
    def printInd(self,index):
        print(index)
        # self.cbb.setCurrentIndex(2)
        self.cbb.setCurrentText('1')
        print(self.cbb.currentIndex())
        
        



if __name__ == '__main__':
    app = QApplication (sys.argv)
    window = MyWindow()
    window.show()

    app.exec()