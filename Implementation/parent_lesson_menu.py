from PyQt4.QtCore import *
from PyQt4.QtGui import *
#
from derived_lesson_menus import *

class ParentLessonMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.buttons = []

        self.title = QLabel()
        self.title.setFont(QFont("Courier", 30))
        
        self.button_1 = QPushButton()
        self.button_2 = QPushButton()
        self.button_3 = QPushButton()

        self.buttons.append(self.button_1)
        self.buttons.append(self.button_2)
        self.buttons.append(self.button_3)

        self.button_1.setMinimumHeight(110)
        self.button_1.setMinimumWidth(60)
        self.button_1.setFont(QFont("Courier", 40))

        self.button_2.setMinimumHeight(110)
        self.button_2.setMinimumWidth(60)
        self.button_2.setFont(QFont("Courier", 40))

        self.button_3.setMinimumHeight(110)
        self.button_3.setMinimumWidth(60)
        self.button_3.setFont(QFont("Courier", 40))

        for button in self.buttons:
            self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")


##        self.button_1.setMinimumHeight(100)
##        self.button_1.setMinimumWidth(60)
##        self.button_1.setFont(QFont("Courier", 20))
##        self.button_1.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")
##
##        self.button_2.setMinimumHeight(100)
##        self.button_2.setMinimumWidth(60)
##        self.button_2.setFont(QFont("Courier", 20))
##        self.button_2.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")
##
##        self.button_3.setMinimumHeight(100)
##        self.button_3.setMinimumWidth(60)
##        self.button_3.setFont(QFont("Courier", 20))
##        self.button_3.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")
        
        self.back = QPushButton("Return")
        self.back.setMinimumHeight(100)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 20))
        self.back.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")
        
        self.label_1 = QLabel("Please select a lesson: ")
        self.label_1.setFont(QFont("Courier", 30))
        
        self.picture = QLabel("Shape")

##        default_button = QPushButton()
##        default_button.setMinimumHeight(60)
##        default_button.setMinimumWidth(100)
##        default_button.setFont(QFont("Courier", 40))
##        default_button.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.label_1, 1, 0)
        self.layout.addWidget(self.picture, 2, 0)
        self.layout.addWidget(self.back, 3, 0)

        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()


