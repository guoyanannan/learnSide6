import sys
from typing import Optional
from Ui_单位换算 import Ui_Form
from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtCore import QThread,Qt
import time



# class MyThread(QThread):
#     def __init__(self,*args) :
#         super().__init__()
#         self.oLabel = args[0]
#         self.tLabel = args[1]
#         self.cbxOne = args[2]
#         self.cbxTwo = args[3]
#         self.originData = args[4]
#         self.tansformData = args[5]
#         self.bigType = args[6]
#         self.dataLen = {'厘米':1,'分米':10,'米':100,'千米':100000}
#         self.dataWei = {'克':1,'斤':500,'公斤':1000}
#         self.dataTpye = {'长度':self.dataLen,'质量':self.dataWei}

#     def run(self):
#         oneKeys = list(self.dataTpye[self.bigType].keys())
#         print(oneKeys)
#         print(self.cbxOne.count())
#         for index in range(self.cbxOne.count()):
#             self.cbxOne.setItem(index,oneKeys[index])
#             self.cbxTwo.setItem(index,oneKeys[index])
#             print(index)
            
        
#         # self.comboBoxOneDtype.addItems(self.dataTpye[txt].keys())
#         # self.comboBoxTwoDtype.addItems(self.dataTpye[txt].keys())
        
#         # 改变原始数据和转换数据
#         # currentOriStr = self.labelOriginData.text().split(' ')[0]
#         currentOneUnit = self.cbxOne.currentText()
#         # currentTransStr = self.labelTransformData.text().split(' ')[0]
#         currentTwoUnit = self.cbxTwo.currentText()
#         print('切换type',currentOneUnit,currentTwoUnit)
#         self.oLabel.setText(f'{self.originData} {currentOneUnit}=')
#         self.tLabel.setText(f'{self.tansformData} {currentTwoUnit}')
# self.myTh = MyThread(self.labelOriginData,self.labelTransformData,self.comboBoxOneDtype,self.comboBoxTwoDtype,
#                         self.originNum,self.transNum,txt)
# self.myTh.start()

class MyWindow(QWidget,Ui_Form):
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.dataLen = {'厘米':1,'分米':10,'米':100,'千米':100000}
        self.dataWei = {'克':1,'斤':500,'公斤':1000,}
        self.dataTpye = {'长度':self.dataLen,'质量':self.dataWei}
        self.comboBoxDType.addItems(self.dataTpye.keys())
        self.comboBoxOneDtype.addItems(self.dataLen)
        self.comboBoxTwoDtype.addItems(self.dataLen)
        
        self.tpyeChangeFlag = False
        self.currentDtype = self.comboBoxDType.currentText()
        
        # 初始化单位
        self.currentOneUnit = self.comboBoxOneDtype.currentText()
        self.currentTwoUnit = self.comboBoxTwoDtype.currentText()
        self.originNum = 1
        self.transNum = 1
        self.bind()
        
    def bind(self):
        self.comboBoxDType.currentTextChanged.connect(self.tpyeChange)
        self.comboBoxOneDtype.currentTextChanged.connect(self.unitChangeOne)
        self.comboBoxTwoDtype.currentTextChanged.connect(self.unitChangeTwo)
        
        self.lineEditInputOne.textChanged.connect(self.inputOne)
        self.lineEditInputTwo.textChanged.connect(self.inputTwo)

    def tpyeChange(self,txt):
        self.tpyeChangeFlag = True
        self.currentDtype = txt
        
        self.comboBoxOneDtype.clear()
        self.comboBoxTwoDtype.clear()
        self.comboBoxOneDtype.addItems(self.dataTpye[txt].keys())
        self.comboBoxTwoDtype.addItems(self.dataTpye[txt].keys())
        # keyList =  list(self.dataTpye[txt].keys())
        # print(keyList)
        # for index,key in enumerate(keyList):
        #     self.comboBoxOneDtype.setItemData(index,key,role=Qt.DisplayRole)
        #     self.comboBoxTwoDtype.setItemData(index,key,role=Qt.DisplayRole)
            
        # 单位
        self.currentOneUnit = self.comboBoxOneDtype.currentText()
        self.currentTwoUnit = self.comboBoxTwoDtype.currentText()
        # print('切换类型:',self.currentOneUnit,self.currentTwoUnit)
        self.labelOriginData.setText(f'{self.originNum} {self.currentOneUnit}=')
        self.labelTransformData.setText(f'{self.transNum} {self.currentTwoUnit}')
    
    def inputOne(self,number):
       
        # if not bool(number):
        #     number = 1
        #     self.lineEditInputOne.setText(str(number))

        # else:
        try:
            number = eval(number)
        except:
            return

        self.originNum = number
        
        # currentOneUnit = self.comboBoxOneDtype.currentText()
        # currentTwoUnit = self.comboBoxTwoDtype.currentText()
        currentOneUnit = self.currentOneUnit
        currentTwoUnit = self.currentTwoUnit
        
        self.labelOriginData.setText(f'{number} {currentOneUnit}=')
        
        currentOneData = float(number) * self.dataTpye[self.currentDtype][currentOneUnit]
        self.transNum = currentOneData / self.dataTpye[self.currentDtype][currentTwoUnit]
        if self.transNum == int(self.transNum):
            self.transNum = int(self.transNum)
        
        self.lineEditInputTwo.setText(str(self.transNum))
        self.labelTransformData.setText(f'{self.transNum} {currentTwoUnit}')
        
    def inputTwo(self,number):
        
        # if not bool(number):
        #     number = 1
        #     self.lineEditInputTwo.setText(str(number))
        # else:
        try:
            number = eval(number)
        except:
            return
        self.transNum = number
        # currentOneUnit = self.comboBoxOneDtype.currentText()
        # currentTwoUnit = self.comboBoxTwoDtype.currentText()
        currentOneUnit = self.currentOneUnit
        currentTwoUnit = self.currentTwoUnit
        
        self.labelTransformData.setText(f'{self.transNum} {currentTwoUnit}')
        currentTwoData = float(number) * self.dataTpye[self.currentDtype][currentTwoUnit]
        self.originNum = currentTwoData / self.dataTpye[self.currentDtype][currentOneUnit]
        
        if self.originNum == int(self.originNum):
            self.originNum = int(self.originNum)
        
        self.lineEditInputOne.setText(str(self.originNum))
        self.labelOriginData.setText(f'{self.originNum} {currentOneUnit}=')
        
    def unitChangeOne(self,txt):
        print(txt)
        print(self.currentDtype)
        if not txt:
            return
        if self.tpyeChangeFlag:
            self.currentOneUnit = self.currentTwoUnit = txt
        else:
            self.currentOneUnit = txt
            self.currentTwoUnit = self.comboBoxTwoDtype.currentText()

        currentOneData = float(self.originNum) * self.dataTpye[self.currentDtype][self.currentOneUnit]
        self.transNum = currentOneData / self.dataTpye[self.currentDtype][self.currentTwoUnit]
        self.lineEditInputTwo.setText(str(self.transNum))

        self.tpyeChangeFlag = False
        
    def unitChangeTwo(self,txt):
        print('↓'*20)
        print(txt)
        print(self.currentDtype)
        if not txt:
                return
        if self.tpyeChangeFlag:
            self.currentOneUnit = self.currentTwoUnit = txt
        else:
            self.currentOneUnit = self.comboBoxOneDtype.currentText()  
            self.currentTwoUnit = txt
        print(self.currentOneUnit,self.currentTwoUnit)
        print('↑'*20)
        currentOneData = float(self.originNum) * self.dataTpye[self.currentDtype][self.currentOneUnit]
        self.transNum = currentOneData / self.dataTpye[self.currentDtype][self.currentTwoUnit]
        self.lineEditInputTwo.setText(str(self.transNum))

        self.tpyeChangeFlag = False
        


if __name__ == '__main__':
    app = QApplication (sys.argv)
    window = MyWindow()
    window.show()

    app.exec()
    
    
    
    '''
    总结：
    1,comboBox 通过clear的方式是清空子选项重新添加,当前索引会初始化为0
    2,comboBox 通过setItemText耗时严重,而setItemData就快很多
    3,对于这种联动组合,在QLineEdit中更新数值并设为类属性,这样在全局可以直接使用
      在QcomboBox中更新类型值并设为类属性,可以减少频繁的获取各组件的属性值
    4,考虑冷启动问题需要把将这些类属性设置初始值,比如：不设置初始输入值和转换值,
      在切换数据类型的时候,会引发ERROR,除非手动获取各组件属性,非最优
    5,冷启动问题二,因为涉及到切换数据类型时,会修改单位comboBox的显示文本,这是就会触发
      单位下拉框发送信号给槽,槽函数获取当前下拉框子选项时并行还在操作的时修改下拉框整个
      子选项的文本,会造成当前修改的下拉框获取的text为空,
      所以需要切换数据类型时,让这两个comboBox的当前文本都设为修改的第一个子选项值
    '''