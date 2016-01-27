from PyQt4.QtCore import *
from PyQt4.QtGui import *

from derived_homework_menus import *
from homework_widgets import *
from homework_widgets_page_2 import *

class Trig1StackSidesEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)
