from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *

class EasyTrigonometry3(QWidget):
    def __init__(self):
        super().__init__()
        self.easy_3_1 = QPushButton("Lesson 3.1")
        self.easy_3_2 = QPushButton("Lesson 3.2")
        self.easy_3_3 = QPushButton("Lesson 3.3")
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.easy_3_1)
        self.layout.addWidget(self.easy_3_2)
        self.layout.addWidget(self.easy_3_3)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.easy_3_1.clicked.connect(self.selected_easy_3_1)
        self.easy_3_2.clicked.connect(self.selected_easy_3_2)
        self.easy_3_3.clicked.connect(self.selected_easy_3_3)
        self.back.clicked.connect(self.selected_back)

    def selected_easy_3_1(self):
        print("Easy 3.1")

    def selected_easy_3_2(self):
        print("Easy 3.2")

    def selected_easy_3_3(self):
        print("Easy 3.3")

    def selected_back(self):
        print("Back")
