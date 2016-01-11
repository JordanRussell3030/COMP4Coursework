from PyQt4.QtCore import *
from PyQt4.QtGui import *
#
from derived_lesson_menus import *

class ParentLessonMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.title = QLabel()
        
        self.button_1 = QPushButton()
        self.button_2 = QPushButton()
        self.button_3 = QPushButton()

        self.button_1.setMinimumHeight(110)
        self.button_1.setMinimumWidth(60)
        self.button_1.setFont(QFont("Courier", 40))

        self.button_2.setMinimumHeight(110)
        self.button_2.setMinimumWidth(60)
        self.button_2.setFont(QFont("Courier", 40))

        self.button_3.setMinimumHeight(110)
        self.button_3.setMinimumWidth(60)
        self.button_3.setFont(QFont("Courier", 40))

        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")
        
        self.back = QPushButton("Return")
        self.back.setMinimumHeight(100)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 40))
        self.back.setStyleSheet("QPushButton {background-color: #D3E5FF; color: red; font-size: 20;}")

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.back, 3, 0)

        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()


