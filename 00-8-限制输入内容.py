import re
from PySide6.QtGui import QValidator
from PySide6.QtCore import Qt

class CustomValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input_text, pos):
        if re.match(r'^[+-]?(\d+(\.\d{0,3})?|\.\d{0,3})?$', input_text):
            return QValidator.Acceptable
        elif input_text == '' or input_text[pos-1] in '+-':
            return QValidator.Intermediate
        else:
            return QValidator.Invalid

    def fixup(self, input_text):
        filtered_text = re.sub(r'[^+-\d.]', '', input_text)
        return filtered_text


from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Restriction Example")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter text:")
        self.line_edit = QLineEdit()

        # 创建自定义验证器对象
        validator = CustomValidator()
        # 将验证器应用到 QLineEdit
        self.line_edit.setValidator(validator)

        # 设置输入法策略为只允许纯英文输入
        self.line_edit.setInputMethodHints(Qt.ImhLatinOnly)

        layout.addWidget(self.label)
        layout.addWidget(self.line_edit)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.line_edit.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, text):
        self.label.setText("Entered value: " + text)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
