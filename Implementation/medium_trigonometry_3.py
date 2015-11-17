from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *

class MediumTrigonometry3(QWidget):
    def __init__(self):
        super().__init__()
        self.medium_3_1 = QPushButton("Lesson 3.1")
        self.medium_3_2 = QPushButton("Lesson 3.2")
        self.medium_3_3 = QPushButton("Lesson 3.3")
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.medium_3_1)
        self.layout.addWidget(self.medium_3_2)
        self.layout.addWidget(self.medium_3_3)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.medium_3_1.clicked.connect(self.selected_medium_3_1)
        self.medium_3_2.clicked.connect(self.selected_medium_3_2)
        self.medium_3_3.clicked.connect(self.selected_medium_3_3)
        self.back.clicked.connect(self.selected_back)

    def selected_medium_3_1(self):
        print("Medium 3.1")

    def selected_medium_3_2(self):
        print("Medium 3.2")

    def selected_medium_3_3(self):
        print("Medium 3.3")

    def selected_back(self):
        print("Back")
