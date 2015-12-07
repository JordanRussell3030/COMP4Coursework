from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *


class DatabaseWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Progress")
        self.details = QLabel("Account No: XXXX\nUsername: XXXX\nAverage Rating: X")
        self.not_success = QPushButton("Not completed")
        self.not_success_2 = QPushButton("Not enough score")
        self.back = QPushButton("Return")
        self.database = QTableWidget()

        self.layout = QGridLayout()

        self.layout.addWidget(self.database, 0, 1)
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.details, 1, 0)
        self.layout.addWidget(self.not_success, 2, 0)
        self.layout.addWidget(self.not_success_2, 3, 0)
        self.layout.addWidget(self.back, 4, 0)

        self.setLayout(self.layout)

class AdminDatabaseWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Progress")
        self.details = QLabel("Account No: XXXX\nUsername: XXXX\nClass: X")
        self.back = QPushButton("Return")
        self.database = QTableWidget()

        self.layout = QGridLayout()

        self.layout.addWidget(self.database, 0, 1)
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.details, 1, 0)
        self.layout.addWidget(self.back, 4, 0)

        self.setLayout(self.layout)
