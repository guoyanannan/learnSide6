import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit,QWidget,QVBoxLayout,QPushButton
from PySide6.QtGui import QKeyEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.conut = 1
        my_w = QWidget()
        self.info_list = []
        self.setWindowTitle("QPlainTextEdit Example")
        # self.setGeometry(300, 300, 400, 200)
        layout = QVBoxLayout()
        self.plain_text_edit = QPlainTextEdit(self)
        self.plain_text_edit.setMaximumBlockCount(50)  # 设置最大块数
        # self.plain_text_edit.installEventFilter(self)  # 安装事件过滤器
        
        push_ = QPushButton('测试按钮')
        push_.clicked.connect(self.addtext)
        layout.addWidget(self.plain_text_edit)
        layout.addWidget(push_)
        
        my_w.setLayout(layout)
        self.setCentralWidget(my_w)
        self.show()

    # def eventFilter(self, obj, event):
    #     if obj == self.plain_text_edit and event.type() == QKeyEvent.KeyPress:
    #         # 在此处添加对键盘输入的处理逻辑
    #         if len(self.plain_text_edit.toPlainText()) >= 1000:  # 设置最大字符数
    #             return True  # 阻止事件传递

    #     return super().eventFilter(obj, event)
        

    def addtext(self):
        # print(self.plain_text_edit.toPlainText())
        # print(type(self.plain_text_edit.toPlainText()))
        # str = f'这是内容 {self.conut}\n' + self.plain_text_edit.toPlainText()
        self.plain_text_edit.appendPlainText(f'这是内容 {self.conut}')
        # # self.plain_text_edit.insertPlainText(f'这是内容 {self.conut} \n',0)
        # self.plain_text_edit.clear()
        # self.plain_text_edit.setPlainText(str)
        # if len(self.info_list)>50:
        #     _ = self.info_list.pop()
        # self.info_list.insert(0,f'这是内容 {self.conut}\n')
        # self.plain_text_edit.setPlainText(''.join(self.info_list))

        self.conut += 1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()


'''
在上述示例中，我们通过setMaximumBlockCount方法设置了QPlainTextEdit的最大块数为100。每次追加文本时，QPlainTextEdit会根据最大块数限制自动删除最旧的块。

此外，我们还通过安装事件过滤器installEventFilter来处理键盘输入事件。在示例中，我们检查QPlainTextEdit中的字符数是否超过了1000个字符，并阻止进一步输入。

您可以根据实际需求和限制来调整代码中的最大字符数限制。
'''