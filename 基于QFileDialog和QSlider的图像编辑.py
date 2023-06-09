
import sys
from PySide6.QtWidgets import QApplication, QWidget,QVBoxLayout,QFileDialog,QSlider,QPushButton,QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from PIL import Image,ImageQt,ImageFilter


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.labelImg = QLabel()
        self.layout = QVBoxLayout()
        self.btn = QPushButton('选择一张图片')
        # 滚动条
        self.Myslider = QSlider(Qt.Orientation.Horizontal)
        self.Myslider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.Myslider.setRange(0,20)
        self.Myslider.setTickInterval(1)
        
        
        self.layout.addWidget(self.labelImg)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.Myslider)
        
        self.setLayout(self.layout)
        self.bind()

    def bind(self):
        self.btn.clicked.connect(self.getImage)
        self.Myslider.valueChanged.connect(self.imgT)
        
    
    def getImage(self):
        self.img = Image.open(QFileDialog.getOpenFileName(self,'选择一张图像','./','图片文件(*.jpg *bmp *.png)')[0])
        self.labelImg.setPixmap(self.img.toqpixmap())
        
    def imgT(self,number):
        self.img_transform = self.img.filter(ImageFilter.GaussianBlur(number))
        self.labelImg.setPixmap(self.img_transform.toqpixmap())
        
        
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
