from PySide2.QtWidgets import *
from PySide2.QtGui import *
import random

class Windows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles ISEN")
        self.setFixedSize(500,300)
        self.layout = QHBoxLayout()
        self.bar = QProgressBar()
        self.slide = QSlider()
        self.layout.addWidget(self.bar)
        self.layout.addWidget(self.slide)
        self.setLayout(self.layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Windows()
   win.show()
   app.exec_()
