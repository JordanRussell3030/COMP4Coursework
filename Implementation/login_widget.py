from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from error_messages import *
#
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
        self.pic = QLabel()
        self.pic_2 = QLabel()

        self.setStyleSheet("layout {background-color: white;}")
        
        self.pic.setPixmap(QPixmap("login_widget_picture"))

        self.pic_2.setPixmap(QPixmap("powered_by_python"))
##        self.pic_2.setMaximumHeight(140)
##        self.pic_2.setMaximumWidth(140)

        self.username.setMinimumWidth(60)
        self.username.setMinimumHeight(100)
        self.username.setFont(QFont("Courier", 40))

        self.u_label.setFont(QFont("Courier", 30))
        self.p_label.setFont(QFont("Courier", 30))

        self.password.setMinimumWidth(60)
        self.password.setMinimumHeight(100)
        self.password.setFont(QFont("Courier", 40))
        self.password.setEchoMode(QLineEdit.Password)

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
        self.layout.addWidget(self.pic, 0, 2)
        self.layout.addWidget(self.pic_2, 4, 2)

        self.setLayout(self.layout)

        self.login.clicked.connect(self.validate_login)

        #print(self.login.icon())       

    def validate_login(self):
##        if self.username.text() == "admin" and self.password.text() == "admin":
            self.NameEntered.emit()
##        elif self.password.text() != "admin" and self.username.text() == "admin":
##            self.error_message = ErrorMessage7()
##            self.error_message.show()
##            self.error_message._raise()
##        elif self.username.text() == "admin" and self.password.text() != "admin":
##            self.error_message = ErrorMessage6()
##            self.error_message.show()
##            self.error_message._raise()
##        else:
##            self.error_message = ErrorMessage1()
##            self.error_message.show()
##            self.error_message._raise()
        
        #SQL stuff
        #if username in database and password in database
##        self.NameEntered.emit()
##        else:
##            error_message = ErrorMessage1()
##            error_message.show()
##            error_message._raise()
##            self.username.setText(None)
##            self.password.setText(None)
##        self.error_message_1 = ErrorMessage5()
##        self.error_message_1.show()
##        self.error_message_1._raise()


##            username list = []
##            password list = []
##            for count in range(len(username_list)):
##                if username_list[count] == username.text() and password.text() == password.text():
##                    nameEntered.emit()
##            if username.text() == 
