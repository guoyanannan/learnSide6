import sys
import yaml
from pathlib import Path
from typing import Optional
from PySide6.QtWidgets import (QApplication,
                               QWidget,
                               QVBoxLayout, 
                               QHBoxLayout,
                               QLabel, 
                               QLineEdit,
                               QGroupBox, 
                               QScrollArea, 
                               QCheckBox, 
                               QPushButton,
                               QMessageBox
                               )
from PySide6.QtCore import Qt

from utils.Ui_steel_level_window import Ui_FormMain

from utils.CommonFuc import SteelTpyeValidator,ParamValidator
from utils.RightConfigShowWidget import SteelClassWin,RightConfigWindow


class MainWindow(QWidget,Ui_FormMain):
    
    def __init__(self) :
        super().__init__()
        self.initUi()
        
        self.paramInit()
        
        self.bind()
    
    def initUi(self):
        self.setupUi(self)
        self.setInputDataTpye()
        # 添加类别列表
        self.getClassInfo()
        self.comboBoxCheckLeftClsName.addItems(self.totalClsName)
        
        self.display_layout = QVBoxLayout()
        self.display_layout.setAlignment(Qt.AlignTop)
        self.widgetScrollArea.setLayout(self.display_layout)
        
    
    def paramInit(self):
        self.steelID_obj = dict()

    
    def setInputDataTpye(self):
        validator_st = SteelTpyeValidator()
        self.lineEditLeftSteelType.setValidator(validator_st)
        validator_cls = ParamValidator()
        # 左：一等品
        # 左：等级一
        self.lineEditLeftOneOneTNum.setValidator(validator_cls)
        self.lineEditLeftOneOneEdgeNum.setValidator(validator_cls)
        self.lineEditLeftOneOneMin.setValidator(validator_cls)
        self.lineEditLeftOneOneMax.setValidator(validator_cls)
        self.lineEditLeftOneOneNo.setValidator(validator_cls)
        # 左：等级二
        self.lineEditLeftOneTwoTNum.setValidator(validator_cls)
        self.lineEditLeftOneTwoEdgeNum.setValidator(validator_cls)
        self.lineEditLeftOneTwoMin.setValidator(validator_cls)
        self.lineEditLeftOneTwoMax.setValidator(validator_cls)
        self.lineEditLeftOneTwoNo.setValidator(validator_cls)
        # 左：等级三
        self.lineEditLeftOneThTNum.setValidator(validator_cls)
        self.lineEditLeftOneThEdgeNum.setValidator(validator_cls)
        self.lineEditLeftOneThMin.setValidator(validator_cls)
        self.lineEditLeftOneThMax.setValidator(validator_cls)
        self.lineEditLeftOneThNo.setValidator(validator_cls)
        # 左：二等品
        # 左：等级一
        self.lineEditLeftTwoOneTNum.setValidator(validator_cls)
        self.lineEditLeftTwoOneEdgeNum.setValidator(validator_cls)
        self.lineEditLeftTwoOneMin.setValidator(validator_cls)
        self.lineEditLeftTwoOneMax.setValidator(validator_cls)
        self.lineEditLeftTwoOneNo.setValidator(validator_cls)
        # 左：等级二
        self.lineEditLeftTwoTwoTNum.setValidator(validator_cls)
        self.lineEditLeftTwoTwoEdgeNum.setValidator(validator_cls)
        self.lineEditLeftTwoTwoMin.setValidator(validator_cls)
        self.lineEditLeftTwoTwoMax.setValidator(validator_cls)
        self.lineEditLeftTwoTwoNo.setValidator(validator_cls)
        # 左：等级三
        self.lineEditLeftTwoThTNum.setValidator(validator_cls)
        self.lineEditLeftTwoThEdgeNum.setValidator(validator_cls)
        self.lineEditLeftTwoThMin.setValidator(validator_cls)
        self.lineEditLeftTwoThMax.setValidator(validator_cls)
        self.lineEditLeftTwoThNo.setValidator(validator_cls)
        # 左：三等品
        # 左：等级一
        self.lineEditLeftThOneTNum.setValidator(validator_cls)
        self.lineEditLeftThOneEdgeNum.setValidator(validator_cls)
        self.lineEditLeftThOneMin.setValidator(validator_cls)
        self.lineEditLeftThOneMax.setValidator(validator_cls)
        self.lineEditLeftThOneNo.setValidator(validator_cls)
        # 左：等级二
        self.lineEditLeftThTwoTNum.setValidator(validator_cls)
        self.lineEditLeftThTwoEdgeNum.setValidator(validator_cls)
        self.lineEditLeftThTwoMin.setValidator(validator_cls)
        self.lineEditLeftThTwoMax.setValidator(validator_cls)
        self.lineEditLeftThTwoNo.setValidator(validator_cls)
        # 左：等级三
        self.lineEditLeftThThTNum.setValidator(validator_cls)
        self.lineEditLeftThThEdgeNum.setValidator(validator_cls)
        self.lineEditLeftThThMin.setValidator(validator_cls)
        self.lineEditLeftThThMax.setValidator(validator_cls)
        self.lineEditLeftThThNo.setValidator(validator_cls)
        
    def bind(self):
        # 切换两个页面
        self.pushButtonParamConfig.clicked.connect(lambda :self.stackedWidget.setCurrentIndex(0))
        self.pushButtonSteelLevelInfo.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        
        # 推送按钮
        self.pushButtonToParamShow.clicked.connect(self.paramsPush)
        
    def paramsPush(self):
        self.getLeftEditValue()
        print('xixi:\n',self.left_params,'\n\n')
        if self.left_params['steel_id'] == '' and self.left_params['class_name'] == '':
            res = QMessageBox.warning(self,'提示','钢种和类别为空，请检查!',QMessageBox.StandardButton.Ok)
            return 
        # if all([v=='' for v in self.left_params.values()]):
        #     res = QMessageBox.critical(self,'提示','配置界面文本框中全为空,请确认操作是否失误!',QMessageBox.StandardButton.Ok)
        #     return
        # elif self.left_params['steel_id'] == '' and self.left_params['class_name'] == '':
        #     res = QMessageBox.warning(self,'提示','钢种和类别为空，请检查!',QMessageBox.StandardButton.Ok)
        #     return
        # elif any([v=='' for v in self.left_params.values()]):
        #     res = QMessageBox.warning(self,'提示','配置界面文本框中存在至少一处为空,请检查并填写!',QMessageBox.StandardButton.Ok)
        #     return
        else:
            if self.steelID_obj.get(self.left_params['steel_id'],0):
                steelIDset = self.steelID_obj[self.left_params['steel_id']]['classnames']
            else:
                steelIDset = []
            
            if self.left_params['steel_id'] not in self.steelID_obj:
                self.category_widget = RightConfigWindow(**self.left_params)
                self.category_widget.right_to_left.connect(self.update_value)
                self.display_layout.addWidget(self.category_widget)
                
                steelIDset.append(self.left_params['class_name'])
                self.steelID_obj[self.left_params['steel_id']] = {'object':self.category_widget,'classnames':steelIDset}

            else:

                if self.left_params['class_name'] in self.steelID_obj[self.left_params['steel_id']]['classnames']:
                    # self.steelID_obj[self.left_params['steel_id']]['object'].groupBoxClass.paramInit(**self.left_params)
                    # self.steelID_obj[self.left_params['steel_id']]['object'].groupBoxClass.setCurrentTextValue()
                    index = self.steelID_obj[self.left_params['steel_id']]['classnames'].index(self.left_params['class_name'])
                    # print(self.steelID_obj[self.left_params['steel_id']]['object'].layoutEveryCls.itemAt(index).widget())
                    self.steelID_obj[self.left_params['steel_id']]['object'].layoutEveryCls.itemAt(index).widget().paramInit(**self.left_params)
                    self.steelID_obj[self.left_params['steel_id']]['object'].layoutEveryCls.itemAt(index).widget().setCurrentTextValue()
                    

                else:
                    category_widget_src = SteelClassWin(**self.left_params)
                    category_widget_dst = self.steelID_obj[self.left_params['steel_id']]['object']
                    category_widget_src.push_current_classinfo.connect(self.update_value)
                    category_widget_dst.layoutEveryCls.addWidget(category_widget_src)
                    steelIDset.append(self.left_params['class_name'])
                    self.steelID_obj[self.left_params['steel_id']]['classnames']=steelIDset
                
            
    def update_value(self,value):
        print('waaa:\n',value)
        self.comboBoxCheckLeftClsName.setCurrentText(value['class_name'])
        self.lineEditLeftSteelType.setText(value['steel_id'])
        # 左：一等品
        # 左：等级一
        self.lineEditLeftOneOneTNum.setText(value['steel_LvOneClassOne_TNum'])
        self.lineEditLeftOneOneEdgeNum.setText(value['steel_LvOneClassOne_ENum'])
        self.lineEditLeftOneOneMin.setText(value['steel_LvOneClassOne_Min'])
        self.lineEditLeftOneOneMax.setText(value['steel_LvOneClassOne_Max'])
        self.lineEditLeftOneOneNo.setText(value['steel_LvOneClassOne_Ignore'])
        # 左：等级二
        self.lineEditLeftOneTwoTNum.setText(value['steel_LvOneClassTwo_TNum'])
        self.lineEditLeftOneTwoEdgeNum.setText(value['steel_LvOneClassTwo_ENum'])
        self.lineEditLeftOneTwoMin.setText(value['steel_LvOneClassTwo_Min'])
        self.lineEditLeftOneTwoMax.setText(value['steel_LvOneClassTwo_Max'])
        self.lineEditLeftOneTwoNo.setText(value['steel_LvOneClassTwo_Ignore'])
        # 左：等级三
        self.lineEditLeftOneThTNum.setText(value['steel_LvOneClassTh_TNum'])
        self.lineEditLeftOneThEdgeNum.setText(value['steel_LvOneClassTh_ENum'])
        self.lineEditLeftOneThMin.setText(value['steel_LvOneClassTh_Min'])
        self.lineEditLeftOneThMax.setText(value['steel_LvOneClassTh_Max'])
        self.lineEditLeftOneThNo.setText(value['steel_LvOneClassTh_Ignore'])
        # 左：二等品
        # 左：等级一
        self.lineEditLeftTwoOneTNum.setText(value['steel_LvTwoClassOne_TNum'])
        self.lineEditLeftTwoOneEdgeNum.setText(value['steel_LvTwoClassOne_ENum'])
        self.lineEditLeftTwoOneMin.setText(value['steel_LvTwoClassOne_Min'])
        self.lineEditLeftTwoOneMax.setText(value['steel_LvTwoClassOne_Max'])
        self.lineEditLeftTwoOneNo.setText(value['steel_LvTwoClassOne_Ignore'])
        # 左：等级二
        self.lineEditLeftTwoTwoTNum.setText(value['steel_LvTwoClassTwo_TNum'])
        self.lineEditLeftTwoTwoEdgeNum.setText(value['steel_LvTwoClassTwo_ENum'])
        self.lineEditLeftTwoTwoMin.setText(value['steel_LvTwoClassTwo_Min'])
        self.lineEditLeftTwoTwoMax.setText(value['steel_LvTwoClassTwo_Max'])
        self.lineEditLeftTwoTwoNo.setText(value['steel_LvTwoClassTwo_Ignore'])
        # 左：等级三
        self.lineEditLeftTwoThTNum.setText(value['steel_LvTwoClassTh_TNum'])
        self.lineEditLeftTwoThEdgeNum.setText(value['steel_LvTwoClassTh_ENum'])
        self.lineEditLeftTwoThMin.setText(value['steel_LvTwoClassTh_Min'])
        self.lineEditLeftTwoThMax.setText(value['steel_LvTwoClassTh_Max'])
        self.lineEditLeftTwoThNo.setText(value['steel_LvTwoClassTh_Ignore'])
        # 左：三等品
        # 左：等级一
        self.lineEditLeftThOneTNum.setText(value['steel_LvThClassOne_TNum'])
        self.lineEditLeftThOneEdgeNum.setText(value['steel_LvThClassOne_ENum'])
        self.lineEditLeftThOneMin.setText(value['steel_LvThClassOne_Min'])
        self.lineEditLeftThOneMax.setText(value['steel_LvThClassOne_Max'])
        self.lineEditLeftThOneNo.setText(value['steel_LvThClassOne_Ignore'])
        # 左：等级二
        self.lineEditLeftThTwoTNum.setText(value['steel_LvThClassTwo_TNum'])
        self.lineEditLeftThTwoEdgeNum.setText(value['steel_LvThClassTwo_ENum'])
        self.lineEditLeftThTwoMin.setText(value['steel_LvThClassTwo_Min'])
        self.lineEditLeftThTwoMax.setText(value['steel_LvThClassTwo_Max'])
        self.lineEditLeftThTwoNo.setText(value['steel_LvThClassTwo_Ignore'])
        # 左：等级三
        self.lineEditLeftThThTNum.setText(value['steel_LvThClassTh_TNum'])
        self.lineEditLeftThThEdgeNum.setText(value['steel_LvThClassTh_ENum'])
        self.lineEditLeftThThMin.setText(value['steel_LvThClassTh_Min'])
        self.lineEditLeftThThMax.setText(value['steel_LvThClassTh_Max'])
        self.lineEditLeftThThNo.setText(value['steel_LvThClassTh_Ignore'])
    
    def getLeftEditValue(self):
        left_steel_id = self.lineEditLeftSteelType.text()
        left_class_id = self.comboBoxCheckLeftClsName.currentText()
        
        # 左：一等品
        # 左：等级一
        left_level1_grade1_tnum = self.lineEditLeftOneOneTNum.text()
        left_level1_grade1_enum = self.lineEditLeftOneOneEdgeNum.text()
        left_level1_grade1_min = self.lineEditLeftOneOneMin.text()
        left_level1_grade1_max = self.lineEditLeftOneOneMax.text()
        left_level1_grade1_ignore = self.lineEditLeftOneOneNo.text()
        # 左：等级二
        left_level1_grade2_tnum = self.lineEditLeftOneTwoTNum.text()
        left_level1_grade2_enum = self.lineEditLeftOneTwoEdgeNum.text()
        left_level1_grade2_min = self.lineEditLeftOneTwoMin.text()
        left_level1_grade2_max = self.lineEditLeftOneTwoMax.text()
        left_level1_grade2_ignore = self.lineEditLeftOneTwoNo.text()
        # 左：等级三
        left_level1_grade3_tnum = self.lineEditLeftOneThTNum.text()
        left_level1_grade3_enum = self.lineEditLeftOneThEdgeNum.text()
        left_level1_grade3_min = self.lineEditLeftOneThMin.text()
        left_level1_grade3_max = self.lineEditLeftOneThMax.text()
        left_level1_grade3_ignore = self.lineEditLeftOneThNo.text()
        # 左：二等品
        # 左：等级一
        left_level2_grade1_tnum = self.lineEditLeftTwoOneTNum.text()
        left_level2_grade1_enum = self.lineEditLeftTwoOneEdgeNum.text()
        left_level2_grade1_min = self.lineEditLeftTwoOneMin.text()
        left_level2_grade1_max = self.lineEditLeftTwoOneMax.text()
        left_level2_grade1_ignore = self.lineEditLeftTwoOneNo.text()
        # 左：等级二
        left_level2_grade2_tnum = self.lineEditLeftTwoTwoTNum.text()
        left_level2_grade2_enum = self.lineEditLeftTwoTwoEdgeNum.text()
        left_level2_grade2_min = self.lineEditLeftTwoTwoMin.text()
        left_level2_grade2_max = self.lineEditLeftTwoTwoMax.text()
        left_level2_grade2_ignore = self.lineEditLeftTwoTwoNo.text()
        # 左：等级三
        left_level2_grade3_tnum = self.lineEditLeftTwoThTNum.text()
        left_level2_grade3_enum = self.lineEditLeftTwoThEdgeNum.text()
        left_level2_grade3_min = self.lineEditLeftTwoThMin.text()
        left_level2_grade3_max = self.lineEditLeftTwoThMax.text()
        left_level2_grade3_ignore = self.lineEditLeftTwoThNo.text()
        # 左：三等品
        # 左：等级一
        left_level3_grade1_tnum = self.lineEditLeftThOneTNum.text()
        left_level3_grade1_enum = self.lineEditLeftThOneEdgeNum.text()
        left_level3_grade1_min = self.lineEditLeftThOneMin.text()
        left_level3_grade1_max = self.lineEditLeftThOneMax.text()
        left_level3_grade1_ignore = self.lineEditLeftThOneNo.text()
        # 左：等级二
        left_level3_grade2_tnum = self.lineEditLeftThTwoTNum.text()
        left_level3_grade2_enum = self.lineEditLeftThTwoEdgeNum.text()
        left_level3_grade2_min = self.lineEditLeftThTwoMin.text()
        left_level3_grade2_max = self.lineEditLeftThTwoMax.text()
        left_level3_grade2_ignore = self.lineEditLeftThTwoNo.text()
        # 左：等级三
        left_level3_grade3_tnum = self.lineEditLeftThThTNum.text()
        left_level3_grade3_enum = self.lineEditLeftThThEdgeNum.text()
        left_level3_grade3_min = self.lineEditLeftThThMin.text()
        left_level3_grade3_max = self.lineEditLeftThThMax.text()
        left_level3_grade3_ignore = self.lineEditLeftThThNo.text()
        
        # 参数整合
        self.left_params = {'steel_id':left_steel_id,
              'class_name':left_class_id,
              'steel_LvOneClassOne_TNum':left_level1_grade1_tnum,
              'steel_LvOneClassOne_ENum':left_level1_grade1_enum,
              'steel_LvOneClassOne_Min':left_level1_grade1_min,
              'steel_LvOneClassOne_Max': left_level1_grade1_max,
              'steel_LvOneClassOne_Ignore': left_level1_grade1_ignore,
              'steel_LvOneClassTwo_TNum':left_level1_grade2_tnum,
              'steel_LvOneClassTwo_ENum':left_level1_grade2_enum,
              'steel_LvOneClassTwo_Min':left_level1_grade2_min,
              'steel_LvOneClassTwo_Max': left_level1_grade2_max,
              'steel_LvOneClassTwo_Ignore': left_level1_grade2_ignore,
              'steel_LvOneClassTh_TNum':left_level1_grade3_tnum,
              'steel_LvOneClassTh_ENum':left_level1_grade3_enum,
              'steel_LvOneClassTh_Min':left_level1_grade3_min,
              'steel_LvOneClassTh_Max': left_level1_grade3_max,
              'steel_LvOneClassTh_Ignore': left_level1_grade3_ignore,
              
              'steel_LvTwoClassOne_TNum': left_level2_grade1_tnum,
              'steel_LvTwoClassOne_ENum':left_level2_grade1_enum,
              'steel_LvTwoClassOne_Min':left_level2_grade1_min,
              'steel_LvTwoClassOne_Max': left_level2_grade1_max,
              'steel_LvTwoClassOne_Ignore': left_level2_grade1_ignore,
              'steel_LvTwoClassTwo_TNum':left_level2_grade2_tnum,
              'steel_LvTwoClassTwo_ENum':left_level2_grade2_enum,
              'steel_LvTwoClassTwo_Min':left_level2_grade2_min,
              'steel_LvTwoClassTwo_Max': left_level2_grade2_max,
              'steel_LvTwoClassTwo_Ignore': left_level2_grade2_ignore,
              'steel_LvTwoClassTh_TNum':left_level2_grade3_tnum,
              'steel_LvTwoClassTh_ENum':left_level2_grade3_enum,
              'steel_LvTwoClassTh_Min':left_level2_grade3_min,
              'steel_LvTwoClassTh_Max': left_level2_grade3_max,
              'steel_LvTwoClassTh_Ignore': left_level2_grade3_ignore,
              
              'steel_LvThClassOne_TNum':left_level3_grade1_tnum,
              'steel_LvThClassOne_ENum':left_level3_grade1_enum,
              'steel_LvThClassOne_Min':left_level3_grade1_min,
              'steel_LvThClassOne_Max': left_level3_grade1_max,
              'steel_LvThClassOne_Ignore': left_level3_grade1_ignore,
              'steel_LvThClassTwo_TNum':left_level3_grade2_tnum,
              'steel_LvThClassTwo_ENum':left_level3_grade2_enum,
              'steel_LvThClassTwo_Min':left_level3_grade2_min,
              'steel_LvThClassTwo_Max': left_level3_grade2_max,
              'steel_LvThClassTwo_Ignore': left_level3_grade2_ignore,
              'steel_LvThClassTh_TNum':left_level3_grade3_tnum,
              'steel_LvThClassTh_ENum':left_level3_grade3_enum,
              'steel_LvThClassTh_Min':left_level3_grade3_min,
              'steel_LvThClassTh_Max': left_level3_grade3_max,
              'steel_LvThClassTh_Ignore': left_level3_grade3_ignore,
              }
        # print(self.left_params)
        
    
    def getClassInfo(self):
        filepath = Path.cwd() / 'config/classnames.yaml'
        with open(filepath, 'r', encoding='utf-8') as f:
            cg = yaml.load(f.read(), Loader=yaml.FullLoader)
        self.totalClsName = cg['names']
        print(self.totalClsName)
        
    
    
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()

    