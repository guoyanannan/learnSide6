# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/2 14:18
@Auth ： 郭亚男
@comp ：北京科技大学工程技术研究院
"""

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGroupBox, QScrollArea, QCheckBox, QPushButton
from PySide6.QtCore import Qt


class CategoryWidget(QWidget):
    def __init__(self, name, steel_dtype,length, width):
        super().__init__()
        self.name = name
        self.steel_dtype = steel_dtype
        self.length = length
        self.width = width
        self.initUI()

    def initUI(self):
        # 创建展示类别名字和展开/收起按钮的布局
        # self.header_layout = QHBoxLayout()
        # self.header_layout.setContentsMargins(0, 0, 0, 0)
        # self.header_layout.setSpacing(0)

        # self.name_label = QLabel(self.name)
        # self.name_label.setStyleSheet("font-weight: bold; font-size: 16px")

        self.button_class_name = QCheckBox(self.name)
        # 包含钢种和对应信息得组件
        self.steel_total_groupbox = QGroupBox()
        self.steel_total_layout = QVBoxLayout()
        self.steel_total_layout.setSpacing(5)
        
        self.button_steel_dtype = QCheckBox(self.steel_dtype)
        # self.button_steel_dtype.setStyleSheet("margin-left: 10px")
        
        # self.toggle_button.setStyleSheet("margin-left: 5px")

        # self.header_layout.addWidget(self.toggle_button)
        # self.header_layout.addWidget(self.name_label)
        # self.header_layout.addStretch()

        # 创建展示具体信息的布局
        self.details_layout = QVBoxLayout()
        self.details_layout.setContentsMargins(20, 0, 0, 0)
        self.details_layout.setSpacing(5)
        
        # 信息组合
        self.label_lenght =  QLabel(f"长度mm: {self.length}")
        self.label_width =  QLabel(f"宽度mm: {self.width}")
        self.details_layout.addWidget(self.label_lenght)
        self.details_layout.addWidget(self.label_width)

        # 创建包含展示具体信息布局的组件
        self.details_groupbox = QGroupBox()
        self.details_groupbox.setLayout(self.details_layout)
        
        # 钢种和详细内容垂直组合
        self.steel_total_layout.addWidget(self.button_steel_dtype)
        self.steel_total_layout.addWidget(self.details_groupbox)
        self.steel_total_groupbox.setLayout(self.steel_total_layout)
        
        

        # 创建主布局，并将展示类别名字和展示具体信息的组件添加到布局中
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        # self.layout.addLayout(self.header_layout)
        self.layout.addWidget(self.button_class_name)
        self.layout.addWidget(self.steel_total_groupbox)
        self.layout.addSpacing(10)

        # 设置为不可见状态，通过点击展开/收起按钮来显示/隐藏具体信息
        self.button_steel_dtype.setVisible(False)
        self.steel_total_groupbox.setVisible(False)

        # 设置整个组件的布局
        self.setLayout(self.layout)

        # 连接展开/收起按钮的状态更改事件
        self.button_class_name.stateChanged.connect(self.toggleDetails)
        self.button_steel_dtype.stateChanged.connect(self.toggleDetailsInfo)
    

    def toggleDetails(self, state):
        # 根据展开/收起按钮的状态，显示/隐藏具体信息
        # print(state)
        self.steel_total_groupbox.setVisible(state)
        # self.details_groupbox.setVisible(state)
        
    def toggleDetailsInfo(self,state):
        self.details_groupbox.setVisible(state)
        
    
        

class ConfigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.steelType = set()
        self.categories = {}
        self.initUI()

    def initUI(self):
        # 创建左侧输入区域的组件
        steel_type_label = QLabel("钢种代号:")
        self.steel_type_input = QLineEdit()
        category_label = QLabel("类别名字:")
        self.category_input = QLineEdit()
        length_label = QLabel("长度:")
        self.length_input = QLineEdit()
        width_label = QLabel("宽度:")
        self.width_input = QLineEdit()
        

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
        left_layout.addWidget(steel_type_label)
        left_layout.addWidget(self.steel_type_input)
        left_layout.addWidget(category_label)
        left_layout.addWidget(self.category_input)
        left_layout.addWidget(length_label)
        left_layout.addWidget(self.length_input)
        left_layout.addWidget(width_label)
        left_layout.addWidget(self.width_input)
        left_layout.addWidget(self.add_button)
        layout.addLayout(left_layout)
        layout.addWidget(self.display_area)

        # 设置主布局
        self.setLayout(layout)

        # 连接添加按钮的点击事件，以添加或更新类别配置信息到显示区域
        self.add_button.clicked.connect(self.addOrUpdateCategory)

    def addOrUpdateCategory(self):
        # 获取输入框的内容
        steeltype = self.steel_type_input.text()
        category = self.category_input.text()
        length = self.length_input.text()
        width = self.width_input.text()

        if category and length and width and steeltype:
            if category in self.categories:
                if steeltype in self.steelType:
                    # 更新已存在的类别配置信息
                    category_widget = self.categories[category]['object']
                    category_widget.button_steel_dtype.setText(steeltype)
                    category_widget.details_layout.itemAt(0).widget().setText(f"长度: {length}")
                    category_widget.details_layout.itemAt(1).widget().setText(f"宽度: {width}")
                else:
                    pass
            else:
                # 创建新的类别配置信息
                self.steelType.add(steeltype)
                category_widget = CategoryWidget(category, steeltype,length, width)
                self.display_layout.addWidget(category_widget)
                self.categories[category] = {'object':category_widget,'type':self.steelType}

            # 清空输入框的内容
            self.category_input.clear()
            self.length_input.clear()
            self.width_input.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # w = CategoryWidget('李文','Q123',10,20)
    window = ConfigWidget()
    window.show()
    # w.show()
    app.exec()
