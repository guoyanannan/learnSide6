import sys
from typing import Optional
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox, QScrollArea, QCheckBox, QPushButton
from PySide6.QtCore import Qt,Signal
from .Ui_everyClassDetail import Ui_FormCreateEachCls



class SteelClassWin(QWidget):
    push_current_classinfo = Signal(dict)
    def __init__(self,**kwargs):
        super().__init__()
        self.paramInit(**kwargs)
        self.initUI()
        self.setCurrentTextValue()

        self.bind()
    
    def initUI(self):
        # 各类的组
        self.groupBoxEveryCls = QGroupBox()
        self.groupBoxEveryCls.setVisible(False)
        self.layoutEveryCls = QVBoxLayout()
        self.groupBoxEveryCls.setLayout(self.layoutEveryCls)
       
        self.classInfoBox = Ui_FormCreateEachCls()
        self.classInfoBox.setupUi(self)
        self.classInfoBox.groupBoxStateSL.setVisible(False)
        
        self.layoutEveryCls.addWidget(self.classInfoBox.checkBoxClassName)
        self.layoutEveryCls.addWidget(self.classInfoBox.groupBoxStateSL)
        
        self.setLayout(self.layoutEveryCls)
    
    def setCurrentTextValue(self):
        self.classInfoBox.checkBoxClassName.setText(str(self.className))
        ## 一等品
        # 缺陷等级一
        self.classInfoBox.lineEditOneOneTNum.setText(str(self.steelLvOneClassOneTotalNum))
        self.classInfoBox.lineEditOneOneEdgeNum.setText(str(self.steelLvOneClassOneEdgeNum))
        self.classInfoBox.lineEditOneOneMin.setText(str(self.steelLvOneClassOneMin))
        self.classInfoBox.lineEditOneOneMax.setText(str(self.steelLvOneClassOneMax))
        self.classInfoBox.lineEditOneOneNo.setText(str(self.steelLvOneClassOneIgnore))
        # 缺陷等级二
        self.classInfoBox.lineEditOneTwoTNum.setText(str(self.steelLvOneClassTwoTotalNum))
        self.classInfoBox.lineEditOneTwoEdgeNum.setText(str(self.steelLvOneClassTwoEdgeNum))
        self.classInfoBox.lineEditOneTwoMin.setText(str(self.steelLvOneClassTwoMin))
        self.classInfoBox.lineEditOneTwoMax.setText(str(self.steelLvOneClassTwoMax))
        self.classInfoBox.lineEditOneTwoNo.setText(str(self.steelLvOneClassTwoIgnore))
        # 缺陷等级三
        self.classInfoBox.lineEditOneThTNum.setText(str(self.steelLvOneClassThTotalNum))
        self.classInfoBox.lineEditOneThEdgeNum.setText(str(self.steelLvOneClassThEdgeNum))
        self.classInfoBox.lineEditOneThMin.setText(str(self.steelLvOneClassThMin))
        self.classInfoBox.lineEditOneThMax.setText(str(self.steelLvOneClassThMax))
        self.classInfoBox.lineEditOneThNo.setText(str(self.steelLvOneClassThIgnore))
        ## 二等品
        # 缺陷等级一
        self.classInfoBox.lineEditTwoOneTNum.setText(str(self.steelLvTwoClassOneTotalNum))
        self.classInfoBox.lineEditTwoOneEdgeNum.setText(str(self.steelLvTwoClassOneEdgeNum))
        self.classInfoBox.lineEditTwoOneMin.setText(str(self.steelLvTwoClassOneMin))
        self.classInfoBox.lineEditTwoOneMax.setText(str(self.steelLvTwoClassOneMax))
        self.classInfoBox.lineEditTwoOneNo.setText(str(self.steelLvTwoClassOneIgnore))
        # 缺陷等级二
        self.classInfoBox.lineEditTwoTwoTNum.setText(str(self.steelLvTwoClassTwoTotalNum))
        self.classInfoBox.lineEditTwoTwoEdgeNum.setText(str(self.steelLvTwoClassTwoEdgeNum))
        self.classInfoBox.lineEditTwoTwoMin.setText(str(self.steelLvTwoClassTwoMin))
        self.classInfoBox.lineEditTwoTwoMax.setText(str(self.steelLvTwoClassTwoMax))
        self.classInfoBox.lineEditTwoTwoNo.setText(str(self.steelLvTwoClassTwoIgnore))
        # 缺陷等级三
        self.classInfoBox.lineEditTwoThTNum.setText(str(self.steelLvTwoClassThTotalNum))
        self.classInfoBox.lineEditTwoThEdgeNum.setText(str(self.steelLvTwoClassThEdgeNum))
        self.classInfoBox.lineEditTwoThMin.setText(str(self.steelLvTwoClassThMin))
        self.classInfoBox.lineEditTwoThMax.setText(str(self.steelLvTwoClassThMax))
        self.classInfoBox.lineEditTwoThNo.setText(str(self.steelLvTwoClassThIgnore))
        ## 三等品
        # 缺陷等级一
        self.classInfoBox.lineEditThOneTNum.setText(str(self.steelLvThClassOneTotalNum))
        self.classInfoBox.lineEditThOneEdgeNum.setText(str(self.steelLvThClassOneEdgeNum))
        self.classInfoBox.lineEditThOneMin.setText(str(self.steelLvThClassOneMin))
        self.classInfoBox.lineEditThOneMax.setText(str(self.steelLvThClassOneMax))
        self.classInfoBox.lineEditThOneNo.setText(str(self.steelLvThClassOneIgnore))
        # 缺陷等级二
        self.classInfoBox.lineEditThTwoTNum.setText(str(self.steelLvThClassTwoTotalNum))
        self.classInfoBox.lineEditThTwoEdgeNum.setText(str(self.steelLvThClassTwoEdgeNum))
        self.classInfoBox.lineEditThTwoMin.setText(str(self.steelLvThClassTwoMin))
        self.classInfoBox.lineEditThTwoMax.setText(str(self.steelLvThClassTwoMax))
        self.classInfoBox.lineEditThTwoNo.setText(str(self.steelLvThClassTwoIgnore))
        # 缺陷等级三
        self.classInfoBox.lineEditThThTNum.setText(str(self.steelLvThClassThTotalNum))
        self.classInfoBox.lineEditThThEdgeNum.setText(str(self.steelLvThClassThEdgeNum))
        self.classInfoBox.lineEditThThMin.setText(str(self.steelLvThClassThMin))
        self.classInfoBox.lineEditThThMax.setText(str(self.steelLvThClassThMax))
        self.classInfoBox.lineEditThThNo.setText(str(self.steelLvThClassThIgnore))
        
    
    
    
    def paramInit(self,**kwargs):
        print('rightclassinfo:\n',kwargs)
        self.currentInfo = kwargs
        # 钢种类型和类别名
        self.steelID = kwargs['steel_id']
        self.className = kwargs['class_name']
        # 一等品
        # 缺陷等级一
        self.steelLvOneClassOneTotalNum = kwargs['steel_LvOneClassOne_TNum']
        self.steelLvOneClassOneEdgeNum = kwargs['steel_LvOneClassOne_ENum']
        self.steelLvOneClassOneMin = kwargs['steel_LvOneClassOne_Min']
        self.steelLvOneClassOneMax = kwargs['steel_LvOneClassOne_Max']
        self.steelLvOneClassOneIgnore = kwargs['steel_LvOneClassOne_Ignore']
        # 缺陷等级二
        self.steelLvOneClassTwoTotalNum = kwargs['steel_LvOneClassTwo_TNum']
        self.steelLvOneClassTwoEdgeNum = kwargs['steel_LvOneClassTwo_ENum']
        self.steelLvOneClassTwoMin = kwargs['steel_LvOneClassTwo_Min']
        self.steelLvOneClassTwoMax = kwargs['steel_LvOneClassTwo_Max']
        self.steelLvOneClassTwoIgnore = kwargs['steel_LvOneClassTwo_Ignore']
        # 缺陷等级三
        self.steelLvOneClassThTotalNum = kwargs['steel_LvOneClassTh_TNum']
        self.steelLvOneClassThEdgeNum = kwargs['steel_LvOneClassTh_ENum']
        self.steelLvOneClassThMin = kwargs['steel_LvOneClassTh_Min']
        self.steelLvOneClassThMax = kwargs['steel_LvOneClassTh_Max']
        self.steelLvOneClassThIgnore = kwargs['steel_LvOneClassTh_Ignore']
        # 二等品
        # 缺陷等级一
        self.steelLvTwoClassOneTotalNum = kwargs['steel_LvTwoClassOne_TNum']
        self.steelLvTwoClassOneEdgeNum = kwargs['steel_LvTwoClassOne_ENum']
        self.steelLvTwoClassOneMin = kwargs['steel_LvTwoClassOne_Min']
        self.steelLvTwoClassOneMax = kwargs['steel_LvTwoClassOne_Max']
        self.steelLvTwoClassOneIgnore = kwargs['steel_LvTwoClassOne_Ignore']
        # 缺陷等级二
        self.steelLvTwoClassTwoTotalNum = kwargs['steel_LvTwoClassTwo_TNum']
        self.steelLvTwoClassTwoEdgeNum = kwargs['steel_LvTwoClassTwo_ENum']
        self.steelLvTwoClassTwoMin = kwargs['steel_LvTwoClassTwo_Min']
        self.steelLvTwoClassTwoMax = kwargs['steel_LvTwoClassTwo_Max']
        self.steelLvTwoClassTwoIgnore = kwargs['steel_LvTwoClassTwo_Ignore']
        # 缺陷等级三
        self.steelLvTwoClassThTotalNum = kwargs['steel_LvTwoClassTh_TNum']
        self.steelLvTwoClassThEdgeNum = kwargs['steel_LvTwoClassTh_ENum']
        self.steelLvTwoClassThMin = kwargs['steel_LvTwoClassTh_Min']
        self.steelLvTwoClassThMax = kwargs['steel_LvTwoClassTh_Max']
        self.steelLvTwoClassThIgnore = kwargs['steel_LvTwoClassTh_Ignore']
         # 三等品
        # 缺陷等级一
        self.steelLvThClassOneTotalNum = kwargs['steel_LvThClassOne_TNum']
        self.steelLvThClassOneEdgeNum = kwargs['steel_LvThClassOne_ENum']
        self.steelLvThClassOneMin = kwargs['steel_LvThClassOne_Min']
        self.steelLvThClassOneMax = kwargs['steel_LvThClassOne_Max']
        self.steelLvThClassOneIgnore = kwargs['steel_LvThClassOne_Ignore']
        # 缺陷等级二
        self.steelLvThClassTwoTotalNum = kwargs['steel_LvThClassTwo_TNum']
        self.steelLvThClassTwoEdgeNum = kwargs['steel_LvThClassTwo_ENum']
        self.steelLvThClassTwoMin = kwargs['steel_LvThClassTwo_Min']
        self.steelLvThClassTwoMax = kwargs['steel_LvThClassTwo_Max']
        self.steelLvThClassTwoIgnore = kwargs['steel_LvThClassTwo_Ignore']
        # 缺陷等级三
        self.steelLvThClassThTotalNum = kwargs['steel_LvThClassTh_TNum']
        self.steelLvThClassThEdgeNum = kwargs['steel_LvThClassTh_ENum']
        self.steelLvThClassThMin = kwargs['steel_LvThClassTh_Min']
        self.steelLvThClassThMax = kwargs['steel_LvThClassTh_Max']
        self.steelLvThClassThIgnore = kwargs['steel_LvThClassTh_Ignore']
        

    def bind(self):
        self.classInfoBox.checkBoxClassName.stateChanged.connect(self.stateClass)    
        self.classInfoBox.radioButtonSLevel.clicked.connect(self.stateLevel)
        self.classInfoBox.radioButtonSLevel_2.clicked.connect(self.stateLevel_2)
        self.classInfoBox.radioButtonSLevel_3.clicked.connect(self.stateLevel_3)
    
    def stateClass(self,state):
        self.classInfoBox.groupBoxStateSL.setVisible(state)
        if state == 2:
            self.push_current_classinfo.emit(self.currentInfo)
          
    def stateLevel(self,state):
        self.classInfoBox.groupBoxSteelL1.setVisible(state)
        
    def stateLevel_2(self,state):
        self.classInfoBox.groupBoxSteelL2.setVisible(state)
    
    def stateLevel_3(self,state):
        self.classInfoBox.groupBoxSteelL3.setVisible(state)


    
class RightConfigWindow(QWidget):
    right_to_left = Signal(dict)
    def __init__(self,**kwargs):
        super().__init__()
        self.paramInit(**kwargs)
        
        # 钢种按钮
        self.checkBoxType = QCheckBox(self.steelID)
        self.checkBoxType.setChecked(False)
        
        # 总布局
        self.verticalLayoutTotal = QVBoxLayout()
        
        #  # 各类的组
        self.groupBoxEveryCls = QGroupBox()
        self.groupBoxEveryCls.setVisible(False)
        self.layoutEveryCls = QVBoxLayout()
        self.groupBoxEveryCls.setLayout(self.layoutEveryCls)
       
        self.groupBoxClass = SteelClassWin(**kwargs)
        self.layoutEveryCls.addWidget(self.groupBoxClass)
        self.verticalLayoutTotal.addWidget(self.checkBoxType)
        self.verticalLayoutTotal.addWidget(self.groupBoxEveryCls)
        self.setLayout(self.verticalLayoutTotal)
        
        self.bind()
        
    def bind(self):
        self.checkBoxType.stateChanged.connect(self.stateType)
        self.groupBoxClass.push_current_classinfo.connect(self.getCurrClsInfo)
        '''
        self.classInfoBox.checkBoxClassName.stateChanged.connect(self.stateClass)    
        self.classInfoBox.radioButtonSLevel.clicked.connect(self.stateLevel)
        self.classInfoBox.radioButtonSLevel_2.clicked.connect(self.stateLevel_2)
        self.classInfoBox.radioButtonSLevel_3.clicked.connect(self.stateLevel_3)
        '''
    def paramInit(self,**kwargs):
        print('rightsteelconfig:\n',kwargs)
        # 钢种类型和类别名
        self.steelID = kwargs['steel_id']
        self.className = kwargs['class_name']
        
        # 一等品
        # 缺陷等级一
        self.steelLvOneClassOneTotalNum = kwargs['steel_LvOneClassOne_TNum']
        self.steelLvOneClassOneEdgeNum = kwargs['steel_LvOneClassOne_ENum']
        self.steelLvOneClassOneMin = kwargs['steel_LvOneClassOne_Min']
        self.steelLvOneClassOneMax = kwargs['steel_LvOneClassOne_Max']
        self.steelLvOneClassOneIgnore = kwargs['steel_LvOneClassOne_Ignore']
        # 缺陷等级二
        self.steelLvOneClassTwoTotalNum = kwargs['steel_LvOneClassTwo_TNum']
        self.steelLvOneClassTwoEdgeNum = kwargs['steel_LvOneClassTwo_ENum']
        self.steelLvOneClassTwoMin = kwargs['steel_LvOneClassTwo_Min']
        self.steelLvOneClassTwoMax = kwargs['steel_LvOneClassTwo_Max']
        self.steelLvOneClassTwoIgnore = kwargs['steel_LvOneClassTwo_Ignore']
        # 缺陷等级三
        self.steelLvOneClassThTotalNum = kwargs['steel_LvOneClassTh_TNum']
        self.steelLvOneClassThEdgeNum = kwargs['steel_LvOneClassTh_ENum']
        self.steelLvOneClassThMin = kwargs['steel_LvOneClassTh_Min']
        self.steelLvOneClassThMax = kwargs['steel_LvOneClassTh_Max']
        self.steelLvOneClassThIgnore = kwargs['steel_LvOneClassTh_Ignore']
        # 二等品
        # 缺陷等级一
        self.steelLvTwoClassOneTotalNum = kwargs['steel_LvTwoClassOne_TNum']
        self.steelLvTwoClassOneEdgeNum = kwargs['steel_LvTwoClassOne_ENum']
        self.steelLvTwoClassOneMin = kwargs['steel_LvTwoClassOne_Min']
        self.steelLvTwoClassOneMax = kwargs['steel_LvTwoClassOne_Max']
        self.steelLvTwoClassOneIgnore = kwargs['steel_LvTwoClassOne_Ignore']
        # 缺陷等级二
        self.steelLvTwoClassTwoTotalNum = kwargs['steel_LvTwoClassTwo_TNum']
        self.steelLvTwoClassTwoEdgeNum = kwargs['steel_LvTwoClassTwo_ENum']
        self.steelLvTwoClassTwoMin = kwargs['steel_LvTwoClassTwo_Min']
        self.steelLvTwoClassTwoMax = kwargs['steel_LvTwoClassTwo_Max']
        self.steelLvTwoClassTwoIgnore = kwargs['steel_LvTwoClassTwo_Ignore']
        # 缺陷等级三
        self.steelLvTwoClassThTotalNum = kwargs['steel_LvTwoClassTh_TNum']
        self.steelLvTwoClassThEdgeNum = kwargs['steel_LvTwoClassTh_ENum']
        self.steelLvTwoClassThMin = kwargs['steel_LvTwoClassTh_Min']
        self.steelLvTwoClassThMax = kwargs['steel_LvTwoClassTh_Max']
        self.steelLvTwoClassThIgnore = kwargs['steel_LvTwoClassTh_Ignore']
         # 三等品
        # 缺陷等级一
        self.steelLvThClassOneTotalNum = kwargs['steel_LvThClassOne_TNum']
        self.steelLvThClassOneEdgeNum = kwargs['steel_LvThClassOne_ENum']
        self.steelLvThClassOneMin = kwargs['steel_LvThClassOne_Min']
        self.steelLvThClassOneMax = kwargs['steel_LvThClassOne_Max']
        self.steelLvThClassOneIgnore = kwargs['steel_LvThClassOne_Ignore']
        # 缺陷等级二
        self.steelLvThClassTwoTotalNum = kwargs['steel_LvThClassTwo_TNum']
        self.steelLvThClassTwoEdgeNum = kwargs['steel_LvThClassTwo_ENum']
        self.steelLvThClassTwoMin = kwargs['steel_LvThClassTwo_Min']
        self.steelLvThClassTwoMax = kwargs['steel_LvThClassTwo_Max']
        self.steelLvThClassTwoIgnore = kwargs['steel_LvThClassTwo_Ignore']
        # 缺陷等级三
        self.steelLvThClassThTotalNum = kwargs['steel_LvThClassTh_TNum']
        self.steelLvThClassThEdgeNum = kwargs['steel_LvThClassTh_ENum']
        self.steelLvThClassThMin = kwargs['steel_LvThClassTh_Min']
        self.steelLvThClassThMax = kwargs['steel_LvThClassTh_Max']
        self.steelLvThClassThIgnore = kwargs['steel_LvThClassTh_Ignore']
        
    def stateType(self,state):
        self.groupBoxEveryCls.setVisible(state)
    
    def getCurrClsInfo(self,value):

        self.right_to_left.emit(value)

    
class ConfigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.steelType = set()
        self.categories = []
        self.categories_cp = []
        self.flag =True
        self.initUI()

    def initUI(self):
    
        # 创建添加按钮
        self.add_button = QPushButton("添加")

        # 创建右侧实时显示区域的组件
        self.display_area = QScrollArea()

        self.display_area.setWidgetResizable(True)
        self.display_layout = QVBoxLayout()
        self.display_layout.setAlignment(Qt.AlignTop)

        self.display_widget = QWidget()
        self.display_widget.setLayout(self.display_layout)
        self.display_area.setWidget(self.display_widget)


        # 创建主布局，并将左侧、添加按钮和右侧的组件添加到布局中
        layout = QHBoxLayout()
        left_layout = QVBoxLayout()
       
        left_layout.addWidget(self.add_button)
        layout.addLayout(left_layout)
        layout.addWidget(self.display_area)

        # 设置主布局
        self.setLayout(layout)

        # 连接添加按钮的点击事件，以添加或更新类别配置信息到显示区域
        self.add_button.clicked.connect(self.addOrUpdateCategory)

    def addOrUpdateCategory(self):
        
        if self.flag:
            params = {'steel_id':'Q456Q',
                'class_name':'裂纹',
                'steel_LvOneClassOne_TNum':50,
                'steel_LvOneClassOne_ENum':0,
                'steel_LvOneClassOne_Min':10,
                'steel_LvOneClassOne_Max': 20,
                'steel_LvOneClassOne_Ignore': 5000,
                'steel_LvOneClassTwo_TNum':100,
                'steel_LvOneClassTwo_ENum':0,
                'steel_LvOneClassTwo_Min':20,
                'steel_LvOneClassTwo_Max': 40,
                'steel_LvOneClassTwo_Ignore': 5000,
                'steel_LvOneClassTh_TNum':200,
                'steel_LvOneClassTh_ENum':0,
                'steel_LvOneClassTh_Min':40,
                'steel_LvOneClassTh_Max': 80,
                'steel_LvOneClassTh_Ignore': 5000,
                
                'steel_LvTwoClassOne_TNum':250,
                'steel_LvTwoClassOne_ENum':20,
                'steel_LvTwoClassOne_Min':210,
                'steel_LvTwoClassOne_Max': 220,
                'steel_LvTwoClassOne_Ignore': 25000,
                'steel_LvTwoClassTwo_TNum':2100,
                'steel_LvTwoClassTwo_ENum':20,
                'steel_LvTwoClassTwo_Min':220,
                'steel_LvTwoClassTwo_Max': 240,
                'steel_LvTwoClassTwo_Ignore': 25000,
                'steel_LvTwoClassTh_TNum':2200,
                'steel_LvTwoClassTh_ENum':20,
                'steel_LvTwoClassTh_Min':240,
                'steel_LvTwoClassTh_Max': 280,
                'steel_LvTwoClassTh_Ignore': 25000,
                
                'steel_LvThClassOne_TNum':350,
                'steel_LvThClassOne_ENum':30,
                'steel_LvThClassOne_Min':310,
                'steel_LvThClassOne_Max': 320,
                'steel_LvThClassOne_Ignore': 35000,
                'steel_LvThClassTwo_TNum':3100,
                'steel_LvThClassTwo_ENum':30,
                'steel_LvThClassTwo_Min':320,
                'steel_LvThClassTwo_Max': 340,
                'steel_LvThClassTwo_Ignore': 35000,
                'steel_LvThClassTh_TNum':3200,
                'steel_LvThClassTh_ENum':30,
                'steel_LvThClassTh_Min':340,
                'steel_LvThClassTh_Max': 380,
                'steel_LvThClassTh_Ignore': 35000,
                }
        
            category_widget = RightConfigWindow(**params)
            self.display_layout.addWidget(category_widget)
            self.categories.append(category_widget)
            self.flag = False
        else:
            params = {
                'steel_id':'Q456Q',
                'class_name':'裂纹',
                'steel_LvOneClassOne_TNum':50,
                'steel_LvOneClassOne_ENum':0,
                'steel_LvOneClassOne_Min':10,
                'steel_LvOneClassOne_Max': 20,
                'steel_LvOneClassOne_Ignore': 5000,
                'steel_LvOneClassTwo_TNum':100,
                'steel_LvOneClassTwo_ENum':0,
                'steel_LvOneClassTwo_Min':20,
                'steel_LvOneClassTwo_Max': 40,
                'steel_LvOneClassTwo_Ignore': 5000,
                'steel_LvOneClassTh_TNum':200,
                'steel_LvOneClassTh_ENum':0,
                'steel_LvOneClassTh_Min':40,
                'steel_LvOneClassTh_Max': 80,
                'steel_LvOneClassTh_Ignore': 5000,
                
                'steel_LvTwoClassOne_TNum':250,
                'steel_LvTwoClassOne_ENum':20,
                'steel_LvTwoClassOne_Min':210,
                'steel_LvTwoClassOne_Max': 220,
                'steel_LvTwoClassOne_Ignore': 25000,
                'steel_LvTwoClassTwo_TNum':2100,
                'steel_LvTwoClassTwo_ENum':20,
                'steel_LvTwoClassTwo_Min':220,
                'steel_LvTwoClassTwo_Max': 240,
                'steel_LvTwoClassTwo_Ignore': 25000,
                'steel_LvTwoClassTh_TNum':2200,
                'steel_LvTwoClassTh_ENum':20,
                'steel_LvTwoClassTh_Min':240,
                'steel_LvTwoClassTh_Max': 280,
                'steel_LvTwoClassTh_Ignore': 25000,
                
                'steel_LvThClassOne_TNum':350,
                'steel_LvThClassOne_ENum':30,
                'steel_LvThClassOne_Min':310,
                'steel_LvThClassOne_Max': 320,
                'steel_LvThClassOne_Ignore': 35000,
                'steel_LvThClassTwo_TNum':3100,
                'steel_LvThClassTwo_ENum':30,
                'steel_LvThClassTwo_Min':320,
                'steel_LvThClassTwo_Max': 340,
                'steel_LvThClassTwo_Ignore': 35000,
                'steel_LvThClassTh_TNum':3200,
                'steel_LvThClassTh_ENum':30,
                'steel_LvThClassTh_Min':340,
                'steel_LvThClassTh_Max': 380,
                'steel_LvThClassTh_Ignore': 35000,
                }
        
            category_widget_src = SteelClassWin(**params)
            
            category_widget_dst = self.categories[0]
            category_widget_dst.layoutEveryCls.addWidget(category_widget_src)
            # category_widget_dst.layoutEveryCls.addWidget(info_group_src)
            # self.categories[-1] = category_widget_dst
            # print(category_widget_dst.layoutEveryCls.itemAt(-2).widget())
            # print(category_widget_dst.layoutEveryCls.itemAt(-1).widget())



