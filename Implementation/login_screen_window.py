from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #self.login_widget = LoginWidget()
        #self.student_home = UserAccountWidget()
        #self.error_message_1 = ErrorMessage1()
        self.lesson_menu = LessonMenuWidget()

        self.stack = QStackedLayout()

        #self.stack.addWidget(self.login_widget)
        #self.stack.addWidget(self.student_home)
        #self.stack.addWidget(self.error_message_1)
        self.stack.addWidget(self.lesson_menu)
       
        
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.raise_()
    app.exec_()
    
