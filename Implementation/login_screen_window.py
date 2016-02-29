from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

from student_account_home import * #Contains the home screen class, needed to switch from the first screen to the home screen
from error_messages import * #Contains all the QErrorMessage classes.
from first_screen_widget import * #This file has the class which creates the first screen
                                  #in the initial stack

import sys

#This window is the main window of the system; it contains two widgets in a
#stack and accepts a pyqtsignal, then transfers to the next page.
class MyWindow(QMainWindow):
    #The signal which activates the next window.
    NameEntered = pyqtSignal()
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()
        #This is the first widget which opens when the program is run.
        self.login_widget = FirstScreen()
        
        #This is the second widget in the stack.      
        self.student_home = UserAccountWidget(self)
        
        #Sets the layout to a stack.
        self.stack = QStackedLayout()
        
        #Adds the two widgets to a stack.
        self.stack.addWidget(self.login_widget)
        self.stack.addWidget(self.student_home)
       
        self.widget = QWidget()
        
        #This sets the stack layout as the program's layout.
        self.widget.setLayout(self.stack)
        
        self.setCentralWidget(self.widget)

        #This is the connection for the continue button which uses the pyqtSignal().
        #When pressed, it switches to the second window in the stack.
        self.login_widget.NameEntered.connect(self.enter_program)
        
    #The method which is run when the above connection is made.
    def enter_program(self):
        #Sets the displayed window to self.student_home.
        self.stack.setCurrentIndex(1)
        #Maximises the screen.
        self.student_home.showMaximized()
        self.student_home.raise_()
        
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
    
