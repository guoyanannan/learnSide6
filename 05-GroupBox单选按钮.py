from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QRadioButton
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GroupBox and RadioButton Example")
        self.setGeometry(300, 300, 300, 200)

        # 创建分组框
        group_box = QGroupBox("Options")

        # 创建单选按钮
        radio_button1 = QRadioButton("Option 1")
        radio_button2 = QRadioButton("Option 2")

        # 将单选按钮组合为互斥按钮组
        # radio_button1.setAutoExclusive(True)
        # radio_button2.setAutoExclusive(True)

        # 创建布局，并将单选按钮添加到分组框中
        layout = QVBoxLayout()
        layout.addWidget(radio_button1)
        layout.addWidget(radio_button2)



        # 设置分组框的布局
        group_box.setLayout(layout)
        

        # 创建主布局，并将分组框添加到主窗口中
        main_layout = QVBoxLayout()
        main_layout.addWidget(group_box)
        self.setLayout(main_layout)

        # 连接信号槽
        radio_button1.clicked.connect(self.handle_radio_button_clicked)
        radio_button2.clicked.connect(self.handle_radio_button_clicked)

    def handle_radio_button_clicked(self):
        sender = self.sender()
        if sender.text() == "Option 1":
            print("Option 1 selected")
        elif sender.text() == "Option 2":
            print("Option 2 selected")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
