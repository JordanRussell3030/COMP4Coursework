from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *

class TDTrigonometry1(QWidget):
    def __init__(self):
        super().__init__()
        self.td_trigonometry_1_1 = QPushButton("Lesson 1.1")
        self.td_trigonometry_1_2 = QPushButton("Lesson 1.2")
        self.td_trigonometry_1_3 = QPushButton("Lesson 1.3")
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.td_trigonometry_1_1)
        self.layout.addWidget(self.td_trigonometry_1_2)
        self.layout.addWidget(self.td_trigonometry_1_3)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.td_trigonometry_1_1.clicked.connect(self.selected_td_1_1)
        self.td_trigonometry_1_2.clicked.connect(self.selected_td_1_2)
        self.td_trigonometry_1_3.clicked.connect(self.selected_td_1_3)
        self.back.clicked.connect(self.selected_back)

    def selected_td_1_1(self):
        print("3D T 1.1")

    def selected_td_1_2(self):
        print("3D T 1.2")

    def selected_td_1_3(self):
        print("3D T 1.3")

    def selected_back(self):
        print("Back")
