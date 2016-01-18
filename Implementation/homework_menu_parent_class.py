from PyQt4.QtGui import *
from PyQt4.QtCore import *

from login_screen_window import *
from derived_homework_menus import *
from student_account_home import *

class ParentHomeworkMenuClass(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        
        self.title = QLabel()
        
        self.button_1 = QPushButton()
        self.button_2 = QPushButton()
        self.button_3 = QPushButton()
        self.button_4 = QPushButton()
        self.button_5 = QPushButton()
        self.button_6 = QPushButton()
        self.button_7 = QPushButton()
        self.button_8 = QPushButton()
        self.button_9 = QPushButton()

        self.pic_1 = QLabel()
        self.pic_2 = QLabel()
        self.pic_3 = QLabel()
        self.pic_4 = QLabel()
        self.pic_5 = QLabel()
        self.pic_6 = QLabel()
        self.pic_7 = QLabel()
        self.pic_8 = QLabel()
        self.pic_9 = QLabel()

        self.pic_1.setAlignment(Qt.AlignCenter)
        self.pic_2.setAlignment(Qt.AlignCenter)
        self.pic_3.setAlignment(Qt.AlignCenter)
        self.pic_4.setAlignment(Qt.AlignCenter)
        self.pic_5.setAlignment(Qt.AlignCenter)
        self.pic_6.setAlignment(Qt.AlignCenter)
        self.pic_7.setAlignment(Qt.AlignCenter)
        self.pic_8.setAlignment(Qt.AlignCenter)
        self.pic_9.setAlignment(Qt.AlignCenter)

        self.button_1.setMinimumHeight(110)
        self.button_1.setMinimumWidth(60)
        self.button_1.setFont(QFont("Courier", 40))

        self.button_2.setMinimumHeight(110)
        self.button_2.setMinimumWidth(60)
        self.button_2.setFont(QFont("Courier", 40))

        self.button_3.setMinimumHeight(110)
        self.button_3.setMinimumWidth(60)
        self.button_3.setFont(QFont("Courier", 40))

        self.button_4.setMinimumHeight(110)
        self.button_4.setMinimumWidth(60)
        self.button_4.setFont(QFont("Courier", 40))

        self.button_5.setMinimumHeight(110)
        self.button_5.setMinimumWidth(60)
        self.button_5.setFont(QFont("Courier", 40))

        self.button_6.setMinimumHeight(110)
        self.button_6.setMinimumWidth(60)
        self.button_6.setFont(QFont("Courier", 40))

        self.button_7.setMinimumHeight(110)
        self.button_7.setMinimumWidth(60)
        self.button_7.setFont(QFont("Courier", 40))

        self.button_8.setMinimumHeight(110)
        self.button_8.setMinimumWidth(60)
        self.button_8.setFont(QFont("Courier", 40))

        self.button_9.setMinimumHeight(110)
        self.button_9.setMinimumWidth(60)
        self.button_9.setFont(QFont("Courier", 40))

        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")
        
        self.back = QPushButton("Return")
        self.back.setMinimumHeight(100)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 40))
        
        self.back.setStyleSheet("QPushButton {background-color: #D3E5FF; color: red;}")

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.back, 10, 0)

        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()
