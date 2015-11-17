from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *

class ExtendedTrigonometry2(QWidget):
    def __init__(self):
        super().__init__()
        self.extended_2_1 = QPushButton("Lesson 2.1")
        self.extended_2_2 = QPushButton("Lesson 2.2")
        self.extended_2_3 = QPushButton("Lesson 2.3")
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.extended_2_1)
        self.layout.addWidget(self.extended_2_2)
        self.layout.addWidget(self.extended_2_3)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.extended_2_1.clicked.connect(self.selected_extended_2_1)
        self.extended_2_2.clicked.connect(self.selected_extended_2_2)
        self.extended_2_3.clicked.connect(self.selected_extended_2_3)
        self.back.clicked.connect(self.selected_back)

    def selected_extended_2_1(self):
        print("Extended 2.1")

    def selected_extended_2_2(self):
        print("Extended 2.2")

    def selected_extended_2_3(self):
        print("Extended 2.3")

    def selected_back(self):
        print("Back")
