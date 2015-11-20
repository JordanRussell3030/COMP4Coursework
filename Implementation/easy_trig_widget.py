from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_menus import *
from derived_lesson_menus import *

class Easy1_1TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pass")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)
        
class Easy1_2TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pass")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class Easy1_3TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pass")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)
