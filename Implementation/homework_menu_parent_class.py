from PyQt4.QtGui import *
from PyQt4.QtCore import *
#
from login_screen_window import *
from derived_homework_menus import *
from student_account_home import *

class ParentHomeworkMenuClass(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.buttons = []
        
        self.title = QLabel()
        self.label_1 = QLabel("Please select a homework: ")
        self.picture = QLabel("Shape")
        
        self.button_1 = QPushButton()
        self.button_2 = QPushButton()
        self.button_3 = QPushButton()
        self.button_4 = QPushButton()
        self.button_5 = QPushButton()
        self.button_6 = QPushButton()
        self.button_7 = QPushButton()
        self.button_8 = QPushButton()
        self.button_9 = QPushButton()

        self.buttons.append(self.button_1)
        self.buttons.append(self.button_2)
        self.buttons.append(self.button_3)
        self.buttons.append(self.button_4)
        self.buttons.append(self.button_5)
        self.buttons.append(self.button_6)
        self.buttons.append(self.button_7)
        self.buttons.append(self.button_8)
        self.buttons.append(self.button_9)

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

        for button in self.buttons:
            self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")
        
        self.back = QPushButton("Return")
        self.back.setMinimumHeight(100)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 20))
        self.back.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.title.setFont(QFont("Courier", 30))
        self.label_1.setFont(QFont("Courier", 30))
        self.picture.setFont(QFont("Courier", 30))

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.label_1, 1, 0)
        self.layout.addWidget(self.picture, 2, 0)
        self.layout.addWidget(self.back, 10, 0)

        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()
