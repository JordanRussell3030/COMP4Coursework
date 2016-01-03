from PyQt4.QtGui import *
from PyQt4.QtCore import *

from easy_trig_widget import *

import sys

class ParentLessonPage1(QWidget):
    def __init__(self):
        super().__init__()
    
        self.cancel_button = QPushButton("Cancel")
        self.next_button = QPushButton("Next")
        self.setWindowTitle("Sine 1")
        self.first_text = QLabel("This is how to use the sine rule")
        self.first_picture = QLabel("Space for a picture")

        self.layout = QGridLayout()

        self.layout.addWidget(self.first_text, 0, 0)
        self.layout.addWidget(self.first_picture, 0, 1)
        self.layout.addWidget(self.cancel_button, 1, 0)
        self.layout.addWidget(self.next_button, 1, 1)

        self.setLayout(self.layout)

    def pass_results(self):
        pass
