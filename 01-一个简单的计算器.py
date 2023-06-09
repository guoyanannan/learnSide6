import sys 
from Ui_123 import Ui_Form
from PySide6.QtWidgets import QApplication,QWidget


class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.event_init()
        self.curr_num = '0'
        
    def event_init(self):
        self.result = '0'
        self.flag = True
        self.pushButton_0.clicked.connect(lambda x: self.addElement('0'))
        self.pushButton_1.clicked.connect(lambda x: self.addElement('1'))
        self.pushButton_2.clicked.connect(lambda x: self.addElement('2'))
        self.pushButton_3.clicked.connect(lambda x: self.addElement('3'))
        self.pushButton_4.clicked.connect(lambda x: self.addElement('4'))
        self.pushButton_5.clicked.connect(lambda x: self.addElement('5'))
        self.pushButton_6.clicked.connect(lambda x: self.addElement('6'))
        self.pushButton_7.clicked.connect(lambda x: self.addElement('7'))
        self.pushButton_8.clicked.connect(lambda x: self.addElement('8'))
        self.pushButton_9.clicked.connect(lambda x: self.addElement('9'))
        self.pushButton_sub.clicked.connect(lambda x: self.opEle('-'))
        self.pushButton_add.clicked.connect(lambda x: self.opEle('+'))
        self.pushButton_res.clicked.connect(self.resTotal)
        self.pushButton_div.clicked.connect(lambda x: self.opEle('/'))
        self.pushButton_dot.clicked.connect(lambda x: self.opEle('*'))
        
        self.pushButton_back.clicked.connect(self.backOne)
        self.pushButton_cls.clicked.connect(self.clearCurr)
        
    def clearCurr(self):
        self.result = '0'
        self.curr_num = '0'
        self.lineEdit.setText(self.result)    
     
        
    def backOne(self):
        self.result = self.result[:-1]
        if not self.result:
            self.result = '0'
        self.lineEdit.setText(self.result)
        
    
    def addElement(self, number_str):
        
        if self.flag:
            self.result += number_str
            
            if not any(i in self.result for i in ['+','-','*','/']):
                self.result = str(int(float(self.result)))
            self.lineEdit.setText(self.result)
            
        else:
            self.lineEdit.setText(number_str)
            self.result += number_str
        self.curr_num  = number_str
    
    def resTotal(self):
        try:
            self.result = str(eval(self.result))
            self.curr_num = self.result
        except:
            self.result = self.curr_num
        finally:
            self.lineEdit.setText(self.result)
            self.flag=True

    def opEle(self,op_arith):
        self.lineEdit.clear()
        self.result += op_arith
        self.flag = False



if __name__ == '__main__':
    app = QApplication (sys.argv)
    window = MyWindow()
    window.show()

    app.exec()
    