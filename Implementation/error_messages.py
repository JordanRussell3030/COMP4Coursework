from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

#These are child class from the built in QErrorMessage class and these are called when the user inputs wrong data types or no value at all on the homeworks
class ErrorMessage2(QErrorMessage):
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()
        
        #This is the message that is passed into the call for the message to be shown
        message = "Invalid data type - please make sure you are inputting a decimal value"

        #This shows the error message on the screen
        QErrorMessage.showMessage(self, message)

class ErrorMessage3(QErrorMessage):
    def __init__(self):
        super().__init__()
        
        message = "Invalid data type - please make sure you are inputting an integer value"
        
        QErrorMessage.showMessage(self, message)

class ErrorMessage4(QErrorMessage):
    def __init__(self):
        super().__init__()
        
        message = "Invalid data type - please make sure you are inputting a string value"
        
        QErrorMessage.showMessage(self, message)

class ErrorMessage5(QErrorMessage):
    def __init__(self):
        super().__init__()
        
        message = "That is incorrect - please try again. You have X more attempts"
        
        QErrorMessage.showMessage(self, message)

class ErrorMessage8(QErrorMessage):
    def __init__(self):
        super().__init__()
        
        message = "Please input your answers"
        
        QErrorMessage.showMessage(self, message)
