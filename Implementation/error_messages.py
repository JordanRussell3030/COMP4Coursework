from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

from login_widget import *
from login_screen_window import *

class ErrorMessage1(QErrorMessage):
    def __init__(self):
        super().__init__()
        message = "Either your username or password is incorrect, please try again. If you have forgotten your login details, please speak to your administrator."
        
        QErrorMessage.showMessage(self, message)

class ErrorMessage2(QErrorMessage):
    def __init__(self):
        super().__init__()
        message = "Invalid data type - please make sure you are inputting a decimal value"
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
