from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *

import sys

class MyWindow(QMainWindow):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.login_widget = LoginWidget()
        self.student_home = UserAccountWidget()

        self.stack = QStackedLayout()

        self.stack.addWidget(self.login_widget)
        self.stack.addWidget(self.student_home)
       
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

        self.login_widget.NameEntered.connect(self.username_provided)

    def username_provided(self):
        self.stack.setCurrentIndex(1)
        username = self.login_widget.username.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
    