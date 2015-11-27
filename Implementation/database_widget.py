from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *


class DatabaseWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self._pass = QLabel("Empty")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)
