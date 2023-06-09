from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QStackedWidget,QVBoxLayout,QWidget
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stacked Widget Example")

        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.button1 = QPushButton("Page 1", self)
        self.button1.clicked.connect(self.show_page1)

        self.button2 = QPushButton("Page 2", self)
        self.button2.clicked.connect(self.show_page2)

        layout = QVBoxLayout()
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

        self.page1 = QWidget()
        self.page1.setStyleSheet("background-color: #FFC0CB")
        self.stacked_widget.addWidget(self.page1)

        self.page2 = QWidget()
        self.page2.setStyleSheet("background-color: #87CEEB")
        self.stacked_widget.addWidget(self.page2)

    def show_page1(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_page2(self):
        self.stacked_widget.setCurrentIndex(1)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
