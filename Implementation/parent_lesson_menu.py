from PyQt4.QtCore import *
from PyQt4.QtGui import *

from derived_lesson_menus import *

class ParentLessonMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.button_1 = None
        self.button_2 = None
        self.button_3 = None
        self.back = QPushButton("Return")
        self.title = QLabel("Trigonometry 1:")
        self.label_1 = QLabel("Please select a lesson: ")
        self.picture = QLabel("Shape")

        self.layout = QGridLayout()

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.label_1, 1, 0)
        self.layout.addWidget(self.picture, 2, 0)
        self.layout.addWidget(self.back, 3, 0)

        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()


