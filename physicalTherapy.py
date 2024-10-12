from PyQt5 import QtWidgets;
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow,self).__init__()
        self.setGeometry(0,0,400,400)
        self.setWindowTitle("Physical Therapy")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("physical therapy")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)
    def clicked(self):
        self.label.setText("You Pressed the Button")
        self.update()
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = myWindow()

    win.show()
    sys.exit(app.exec_())
window()