from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *

import sys

class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.username = QLineEdit()
        self.u_label = QLabel("Please enter your username: ")
        self.password = QLineEdit()
        self.p_label = QLabel("Please enter your password: ")
        self.login = QPushButton("Submit")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.u_label)
        self.layout.addWidget(self.username)
        self.layout.addWidget(self.p_label)
        self.layout.addWidget(self.password)
        self.layout.addWidget(self.login)

        self.setLayout(self.layout)

        self.login.clicked.connect(self.submit_pushed)

    def submit_pushed(self):
        print("Success login")
        self.stack.setCurrentIndex(1)
##        if self.username.text == "Jordan" and self.password.text == "abc":
##            print("Valid")
##        else:
##            print("Nope")
