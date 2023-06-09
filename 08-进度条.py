from typing import Optional
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QProgressBar, QPushButton, QMainWindow, QLabel,QWidget,QLineEdit


class ProgressDialog(QDialog):
    
    progress_stop = Signal(int)
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Progress Dialog")
        self.setGeometry(300, 300, 300, 100)

        layout = QVBoxLayout()

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)

        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

    def set_progress(self, value):
        self.progress_bar.setValue(value)
        
    def closeEvent(self, event):
        self.progress_stop.emit(0)
        event.accept()

        


class WorkerThread(QThread):
    progress_updated = Signal(int)
    def __init__(self):
        super().__init__()
        self.flag = True
    
    def run(self):
        for i in range(101):
            if self.flag:
                self.progress_updated.emit(i)
                self.msleep(100)  # 模拟耗时操作
            else:
                break
        self.quit()
    def my_stop(self,value):
        print(value)
        if value == 0:
            self.flag = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(300, 300, 300, 200)

        self.label = QLabel("Click the button to start the progress")
        self.button = QPushButton("Start Progress")
        self.linetxt = QLineEdit()
        self.button.clicked.connect(self.start_progress)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        layout.addWidget(self.linetxt)
        

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.progress_dialog = None
        self.worker_thread = None

    def start_progress(self):
        self.label.setText("Progress started")
        self.button.setEnabled(False)

        self.progress_dialog = ProgressDialog()
        self.progress_dialog.show()
        

        self.worker_thread = WorkerThread()
        self.worker_thread.progress_updated.connect(self.update_progress)
        self.worker_thread.finished.connect(self.progress_finished)
        self.worker_thread.start()
        
        self.progress_dialog.progress_stop.connect(self.worker_thread.my_stop)

    def update_progress(self, value):
        self.progress_dialog.set_progress(value)
        self.linetxt.setText(str(value))

    def progress_finished(self):
        self.label.setText("Progress finished")
        self.button.setEnabled(True)
        self.progress_dialog.close()

    def closeEvent(self, event):
        if self.worker_thread and self.worker_thread.isRunning():
            self.worker_thread.quit()
            # self.worker_thread.wait()

        event.accept()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
