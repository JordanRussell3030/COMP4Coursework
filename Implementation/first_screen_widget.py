from PyQt4.QtGui import *
from PyQt4.QtCore import *

#This widget is attached to the 
class FirstScreen(QWidget):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.message = QLabel("Welcome to the Triangle Geometry Education Program")
        self.setWindowTitle("Triangle Maths")

        self.cont = QPushButton("Continue")
        
        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("powered_by_python"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.message.setFont(QFont("Courier", 40))
        self.message.setAlignment(Qt.AlignCenter)

        self.cont.setMinimumHeight(110)
        self.cont.setMinimumWidth(60)
        self.cont.setFont(QFont("Courier", 40))

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.cont.clicked.connect(self.enter)

        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.message, 1, 0)
        self.layout.addWidget(self.cont, 2, 0)
        self.layout.addWidget(self.pic, 0, 0)

    def enter(self):
        self.NameEntered.emit()
