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
        self.a_label = QLabel("Please log in with your username\nand password.")
        self.b_label = QLabel("Consult your administrator if you\nhave forgotten your login details.")
        self.login = QPushButton("Log in")

        self.username.setMinimumWidth(60)
        self.username.setMinimumHeight(100)
        self.username.setFont(QFont("Courier", 40))

        self.u_label.setFont(QFont("Courier", 30))
        self.p_label.setFont(QFont("Courier", 30))

        self.password.setMinimumWidth(60)
        self.password.setMinimumHeight(100)
        self.password.setFont(QFont("Courier", 40))

        self.login.setMinimumWidth(60)
        self.login.setMinimumHeight(110)
        self.login.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")
        self.login.setFont(QFont("Courier", 40))

        self.a_label.setFont(QFont("Courier", 40))
        self.b_label.setFont(QFont("Courier", 40))
    
        self.setWindowTitle("Welcome to Trigonometry and Pythagoras Lessons")
##        self.setStyleSheet("background: blue")

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

        #print(self.login.icon())

    def submit_pushed(self):
        username = self.username.text()
        print(username)
        self.NameEntered.emit()
##        self.error_message_1 = ErrorMessage5()
##        self.error_message_1.show()
##        self.error_message_1._raise()
