from PyQt4.QtCore import *
from PyQt4.QtGui import *

from homework_widgets import *

class SidesAHOEasyWidget2(QWidget):
    def __init__(self):
        super().__init__()
        self.question_2 = QLabel("Question 2\n_________\n_________")
        self.shape_2 = QLabel("Shape")
        self.answer_2 = QComboBox()
        self.mark_2 = QPushButton("Mark it  |  2")
        self.question_3 = QLabel("Question 3\n_________\n_________")
        self.shape_3 = QLabel("Shape")
        self.answer_3 = QComboBox()
        self.mark_3 = QPushButton("Mark it  |  2")
        self.previous = QPushButton("Previous")
        self.drag_drop = QLabel("Drag and drop space")
        self.question_4 = QLabel("Question 4\n______\n______\n______")
        self.mark_4 = QPushButton("Mark it  |  2")
        self.finish = QPushButton("Finish")

        self.layout = QGridLayout()

        self.layout.addWidget(self.question_2, 0, 0)
        self.layout.addWidget(self.shape_2, 1, 0)
        self.layout.addWidget(self.answer_2, 2, 0)
        self.layout.addWidget(self.mark_2, 2, 1)
        self.layout.addWidget(self.question_3, 3, 0)
        self.layout.addWidget(self.shape_3, 4, 0)
        self.layout.addWidget(self.answer_3, 5, 0)
        self.layout.addWidget(self.mark_3, 5, 1)
        self.layout.addWidget(self.previous, 6, 0)
        self.layout.addWidget(self.drag_drop, 0, 2)
        self.layout.addWidget(self.question_4, 5, 2)
        self.layout.addWidget(self.mark_4, 5, 3)
        self.layout.addWidget(self.finish, 6, 3)

        self.setLayout(self.layout)

        self.mark_2.clicked.connect(self.selected_mark_2)
        self.mark_3.clicked.connect(self.selected_mark_3)
        self.previous.clicked.connect(self.selected_previous)
        self.mark_4.clicked.connect(self.selected_mark_4)
        self.finish.clicked.connect(self.selected_finish)

    def selected_mark_2(self):
        pass

    def selected_mark_3(self):
        pass

    def selected_previous(self):
        pass

    def selected_mark_4(self):
        pass

    def selected_finish(self):
        pass
