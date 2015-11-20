from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *

class HardTrigonometry2(QWidget):
    def __init__(self):
        super().__init__()
        self.hard_2_1 = QPushButton("Lesson 2.1")
        self.hard_2_2 = QPushButton("Lesson 2.2")
        self.hard_2_3 = QPushButton("Lesson 2.3")
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.hard_2_1)
        self.layout.addWidget(self.hard_2_2)
        self.layout.addWidget(self.hard_2_3)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.hard_2_1.clicked.connect(self.selected_hard_2_1)
        self.hard_2_2.clicked.connect(self.selected_hard_2_2)
        self.hard_2_3.clicked.connect(self.selected_hard_2_3)
        self.back.clicked.connect(self.selected_back)

    def selected_hard_2_1(self):
        print("Hard 2.1")

    def selected_hard_2_2(self):
        print("Hard 2.2")

    def selected_hard_2_3(self):
        print("Hard 2.3")

    def selected_back(self):
        print("Back")
