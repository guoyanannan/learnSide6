from PySide6.QtWidgets import QApplication, QWidget, QCommandLinkButton
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CommandLinkButton Example")
        self.setGeometry(300, 300, 1000, 200)

        command_link_button = QCommandLinkButton("Open File", "Click here to open a file.", self)
        command_link_button.setGeometry(20,20,300,100)
        command_link_button.clicked.connect(self.open_file)
        command_link_button.move(20, 20)

    def open_file(self):
        print("Open File button clicked!")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
