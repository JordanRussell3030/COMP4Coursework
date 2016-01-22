from PyQt4.QtGui import *
from PyQt4.QtCore import *

from login_widget import * #The login screen window class is in here.
from student_account_home import * #The student home class is in here.
from lesson_menu_widget import * #Contains the lesson menu class.
from admin_account_home import * #Contains the admin account class.
from homework_set_screen import * #Contains the homework setting screen class.
from results_menu_widget import * #Contains the result menu class.
from error_messages import * #Contains all the QErrorMessage classes.

import sys

#This window is the main window of the system; it contains two widgets in a
#stack and accepts a pyqtsignal, then transfers to the next page.
class MyWindow(QMainWindow):
    #The signal which activates the next window.
    NameEntered = pyqtSignal()
    #Constructor.
    def __init__(self):
        super().__init__()
        #This is the first widget which opens when the progream is run.
        self.login_widget = LoginWidget()
        #This is the second widget in the stack if the user is a student.
        self.student_home = UserAccountWidget(self)
        #This is the second widget in the stack if the user is an administrator.
##        self.student_home = AdminAccountWidget()
##        self.student_home = AddNamesWidget()

##        self.student_home = HomeworkSetScreen()
        
        #Sets the layout to a stack.
        self.stack = QStackedLayout()
        
        #Adds the two widgets to a stack.
        self.stack.addWidget(self.login_widget)
        self.stack.addWidget(self.student_home)
       
        self.widget = QWidget()
        #This sets the stack layout as the program's layout.
        self.widget.setLayout(self.stack)
        
        self.setCentralWidget(self.widget)

        #This is the connection for the login button - when pressed,
        # it displays self.student_home.
        self.login_widget.NameEntered.connect(self.username_provided)
        
    #The method which is run when the above connection is made.
    def username_provided(self):
        #Sets the displayed window to self.student_home.
        self.stack.setCurrentIndex(1)
        #Maximises the screen.
        self.student_home.showMaximized()
        ##Login and password stuff
        username = self.login_widget.username.text()
        
#This makes the program start by default when run.
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #Assigns the window to the MyWindow class made above.
    window = MyWindow()
    #Forces the window to be shown.
    window.show()
    window.raise_()
    #Maximises the window.
    window.showMaximized()
    app.exec_()
    
