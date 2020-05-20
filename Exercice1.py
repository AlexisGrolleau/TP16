from PySide2.QtWidgets import *
from PySide2.QtGui import *
import random

class Windows(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Cycles ISEN")
        self.setFixedSize(500,300)
        self.cycle = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]
        self.layout = QVBoxLayout()
        self.text = QLabel("test")
        self.button = QPushButton("Changer de cycle")
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.choice())
        self.setLayout(self.layout)

    def choice(self):
        mytext = random.choice(self.cycle)
        self.text.setText(mytext)
        return

if __name__ == "__main__":
   app = QApplication([])
   win = Windows()
   win.show()
   app.exec_()
