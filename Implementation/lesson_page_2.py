from PyQt4.QtCore import *
from PyQt4.QtCore import *

from easy_trig_widget import *

class SidesAHOWidgetPage2(QWidget):
    def __init__(self):
        super().__init__()
        self.text_1 = QTextEdit("Space for an alternative examples showing different methods e.g c2 = a2 + b2")
        self.text_2 = QTextEdit("Space for a practice question based on the lesson e.g what is the length of a")
        self.answer = QLineEdit("Space for an answer")
        self.previous = QPushButton("Previous")
        self.check = QPushButton("Check")
        self.finish = QPushButton("Finish")

        self.layout = QGridLayout()

        self.layout.addWidget(self.text_1, 0, 0)
        self.layout.addWidget(self.text_2, 0, 1)
        self.layout.addWidget(self.answer, 1, 1)
        self.layout.addWidget(self.previous, 2, 0)
        self.layout.addWidget(self.check, 2, 1)
        self.layout.addWidget(self.finish, 3, 1)

        self.setLayout(self.layout)

        self.previous.clicked.connect(self.previous_selected)
        self.check.clicked.connect(self.check_selected)
        self.finish.clicked.connect(self.finish_selected)

    def previous_selected(self):
        pass

    def check_selected(self):
        pass

    def finish_selected(self):
        pass
