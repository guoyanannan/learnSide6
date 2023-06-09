import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QCheckBox,QComboBox,QWidget,QVBoxLayout
from PySide6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowTitle('勾选框')
        w = QWidget()
        layout = QVBoxLayout()
        self.cbb = QCheckBox('学校')
        self.cbb.setStyleSheet(u"QCheckBox:indicator{\n"
                                    "	width: 0;\n"
                                    "}\n"
                                    "QCheckBox:pressed{\n"
                                    "	\n"
                                    "	color: rgba(255, 255, 255,0);\n"
                                    "}\n"
                                    "")
        
        
        # self.cbb.stateChanged.connect(lambda: print(self.cbb.isChecked()))
        self.cbb.stateChanged.connect(self.printInd)
        
        
        layout.addWidget(self.cbb)
        w.setLayout(layout)
        
        self.setCentralWidget(w)
        
    def printInd(self,index):
        print(index)
        
        



if __name__ == '__main__':
    app = QApplication (sys.argv)
    window = MyWindow()
    window.show()

    app.exec()
    
    
    
  