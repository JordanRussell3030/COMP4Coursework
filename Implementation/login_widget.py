from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from error_messages import *

import sys

class LoginWidget(QWidget):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()
        
        self.username = QLineEdit()
        self.u_label = QLabel("Username: ")
        self.password = QLineEdit()
        self.p_label = QLabel("Password: ")
        self.a_label = QLabel("Please log in\nwith your username\nand password.")
        self.b_label = QLabel("Consult your administrator\nif you have forgotten\nyour login details.")
        self.login = QPushButton("Log in")
        
        self.setWindowTitle("Welcome to Trigonometry and Pythagoras Lessons")

        self.layout = QGridLayout()

        self.layout.addWidget(self.u_label, 0, 0)
        self.layout.addWidget(self.username, 0, 1)
        self.layout.addWidget(self.p_label, 1, 0)
        self.layout.addWidget(self.password, 1, 1)
        self.layout.addWidget(self.a_label, 2, 1)
        self.layout.addWidget(self.b_label, 3, 1)
        self.layout.addWidget(self.login, 4, 1)

        self.setLayout(self.layout)

        self.login.clicked.connect(self.submit_pushed)

    def submit_pushed(self):
        username = self.username.text()
        print(username)
        self.NameEntered.emit()
##        self.error_message_1 = ErrorMessage5()
##        self.error_message_1.show()
##        self.error_message_1._raise()
