from PyQt4.QtCore import *
from PyQt4.QtGui import *
#
from derived_homework_menus import *
from login_screen_window import *

class HomeworkSetScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Title of selected homework")
        self.class_label = QLabel("Class")
        self.class_box = QComboBox()
        self.deadline = QLabel("Deadline")
        self.deadline_box = QComboBox()
        self.score_req = QLabel("Score Requirements")
        self.score_line = QLineEdit()
        self.back_button = QPushButton("Return")
        self.set_button = QPushButton("Set")

        self.class_box.addItem("10A")
        self.class_box.addItem("10B")
        self.class_box.addItem("10C")
        self.deadline_box.addItem("12/12/15")
        self.deadline_box.addItem("13/12/15")

        self.layout = QGridLayout()

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.class_label, 1, 0)
        self.layout.addWidget(self.class_box, 1, 1)
        self.layout.addWidget(self.deadline, 2, 0)
        self.layout.addWidget(self.deadline_box, 2, 1)
        self.layout.addWidget(self.score_req, 3, 0)
        self.layout.addWidget(self.score_line, 3, 1)
        self.layout.addWidget(self.back_button, 4, 0)
        self.layout.addWidget(self.set_button, 4, 1)

        self.setLayout(self.layout)

        self.back_button.clicked.connect(self.selected_back)
        self.set_button.clicked.connect(self.selected_set)

    def selected_back(self):
        pass

    def selected_set(self):
        pass
