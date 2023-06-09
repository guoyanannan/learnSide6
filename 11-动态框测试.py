import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox, QScrollArea, QCheckBox, QPushButton
from PySide6.QtCore import Qt

from Ui_折叠窗口哦吼 import Ui_Form



class MainWindow(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.groupBoxStateCls.setVisible(False)
        self.groupBoxStateSL.setVisible(False)
        self.checkBoxSteelType.stateChanged.connect(self.stateType)
        self.checkBoxClassName.stateChanged.connect(self.stateClass)
        self.radioButtonSLevel.clicked.connect(self.stateGrade)
        self.radioButtonSLevel_2.clicked.connect(self.stateGrade_2)
        self.radioButtonSLevel_3.clicked.connect(self.stateGrade_3)

        

        


    def stateType(self,state):
        self.groupBoxStateCls.setVisible(state)
        
    def stateClass(self,state):
        self.groupBoxStateSL.setVisible(state)
        
    def stateGrade(self,state):
        self.groupBoxSteelL1.setVisible(state)

    def stateGrade_2(self,state):
        self.groupBoxSteelL2.setVisible(state)
    
    def stateGrade_3(self,state):
        self.groupBoxSteelL3.setVisible(state)
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())