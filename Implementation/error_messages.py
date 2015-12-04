from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

from login_widget import *
from login_screen_window import *

class ErrorMessage1(QErrorMessage):
    def __init__(self):
        super().__init__()
        message = "Either your username or password is incorrect, please try again. If you have forgotten your login details, please speak to your administrator."
        
        QErrorMessage.showMessage (self, message)

