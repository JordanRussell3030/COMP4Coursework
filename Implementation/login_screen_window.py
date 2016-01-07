from PyQt4.QtGui import *
from PyQt4.QtCore import *
#
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *
from admin_account_home import *
from homework_set_screen import *
from results_menu_widget import *
from error_messages import *
###
##from temp import *
###
import sys

class MyWindow(QMainWindow):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.login_widget = LoginWidget()
        self.student_home = UserAccountWidget(self)
##        self.student_home = AdminAccountWidget()
##        self.student_home = AnyWidget()
##        self.student_home = RWidget()

##        self.student_home = HomeworkSetScreen()  

##        self.student_home = HomeworkSetScreen()
##        self.student_home = ErrorMessage2()

        self.stack = QStackedLayout()

        self.stack.addWidget(self.login_widget)
        self.stack.addWidget(self.student_home)
       
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

        self.login_widget.NameEntered.connect(self.username_provided)

    def username_provided(self):
        self.stack.setCurrentIndex(1)
        self.student_home.showMaximized()
        username = self.login_widget.username.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    window.showMaximized()
    app.exec_()
    
