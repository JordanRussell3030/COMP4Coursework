from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from homework_menu_widget import *

class ParentHomework(QWidget):
    def __init__(self):
        super().__init__()
        self.homework_1 = QPushButton("Homework 1")
        self.homework_2 = QPushButton("Homework 2")
        self.homework_3 = QPushButton("Homework 3")
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.homework_1)
        self.layout.addWidget(self.homework_2)
        self.layout.addWidget(self.homework_3)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

    def selected_homework_1(self):
        homework_1_widget = Homework1Widget()
        homework_1_widget.show()
        homework_1_widget._raise()

    def selected_homework_2(self):
        homework_2_widget = Homework2Widget()
        homework_2_widget.show()
        homework_2_widget._raise()

    def selected_homework_3(self):
        homework_3_widget = Homework3Widget()
        homework_3_widget.show()
        homework_3_widget._raise()

    def selected_back(self):
        homeworkmenuwidget.show()
        homeworkmenuwidget._raise()
