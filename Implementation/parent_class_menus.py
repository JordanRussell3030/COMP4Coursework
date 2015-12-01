from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *

class ParentLesson(QWidget):
    def __init__(self):
        super().__init__()
        self.lesson_1 = QPushButton("Lesson 1")
        self.lesson_2 = QPushButton("Lesson 2")
        self.lesson_3 = QPushButton("Lesson 3")
        self.back = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.lesson_1)
        self.layout.addWidget(self.lesson_2)
        self.layout.addWidget(self.lesson_3)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

    def selected_lesson_1(self):
        lesson_1_widget = Lesson1Widget()
        lesson_1_widget.show()
        lesson_1_widget._raise()

    def selected_lesson_2(self):
        lesson_2_widget = Lesson2Widget()
        lesson_2_widget.show()
        lesson_2_widget._raise()

    def selected_lesson_3(self):
        lesson_3_widget = Lesson3Widget()
        lesson_3_widget.show()
        lesson_3_widget._raise()

    def selected_back(self):
        lessonmenuwidget.show()
        lessonmenuwidget._raise()
