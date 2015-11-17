from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_widget import *
from student_account_home import *
from lesson_menu_widget import *
from easy_trigonometry_1 import *
from easy_trigonometry_2 import *
from easy_trigonometry_3 import *
from medium_trigonometry_1 import *
from medium_trigonometry_2 import *
from medium_trigonometry_3 import *
from hard_trigonometry_1 import *
from hard_trigonometry_2 import *
from hard_trigonometry_3 import *
from extended_trigonometry_1 import *
from extended_trigonometry_2 import *
from extended_trigonometry_3 import *
from easy_pythagoras import *
from medium_pythagoras import *
from hard_pythagoras import *
from td_pythagoras_1 import *
from td_pythagoras_2 import *
from td_trigonometry_1 import *
from td_trigonometry_2 import *

import sys

class MyWindow(QMainWindow):
    NameEntered = pyqtSignal()
    def __init__(self):
        super().__init__()

        self.login_widget = LoginWidget()
        self.student_home = UserAccountWidget()
##        self.error_message_1 = ErrorMessage1()
        self.lesson_menu = LessonMenuWidget()
        self.easy_trig_1 = EasyTrigonometry1()
        self.easy_trig_2 = EasyTrigonometry2()
        self.easy_trig_3 = EasyTrigonometry3()
        self.medium_trig_1 = MediumTrigonometry1()
        self.medium_trig_2 = MediumTrigonometry2()
        self.medium_trig_3 = MediumTrigonometry3()
        self.hard_trig_1 = HardTrigonometry1()
        self.hard_trig_2 = HardTrigonometry2()
        self.hard_trig_3 = HardTrigonometry3()
        self.extended_trig_1 = ExtendedTrigonometry1()
        self.extended_trig_2 = ExtendedTrigonometry2()
        self.extended_trig_3 = ExtendedTrigonometry3()
        self.easy_pythagoras = EasyPythagoras()
        self.medium_pythagoras = MediumPythagoras()
        self.hard_pythagoras = HardPythagoras()
        self.td_pythagoras_1 = TDPythagoras1()
        self.td_pythagoras_2 = TDPythagoras2()
        self.td_trigonometry_1 = TDTrigonometry1()
        self.td_trigonometry_2 = TDTrigonometry2()

        self.stack = QStackedLayout()

        self.stack.addWidget(self.login_widget)
        self.stack.addWidget(self.student_home)
##        self.stack.addWidget(self.error_message_1)
##        self.stack.addWidget(self.lesson_menu)
##        self.stack.addWidget(self.easy_trig_1)
##        self.stack.addWidget(self.easy_trig_2)
##        self.stack.addWidget(self.easy_trig_3)
##        self.stack.addWidget(self.medium_trig_1)
##        self.stack.addWidget(self.medium_trig_2)
##        self.stack.addWidget(self.medium_trig_3)
##        self.stack.addWidget(self.hard_trig_1)
##        self.stack.addWidget(self.hard_trig_2)
##        self.stack.addWidget(self.hard_trig_3)
##        self.stack.addWidget(self.extended_trig_1)
##        self.stack.addWidget(self.extended_trig_2)
##        self.stack.addWidget(self.extended_trig_3)
##        self.stack.addWidget(self.easy_pythagoras)
##        self.stack.addWidget(self.medium_pythagoras)
##        self.stack.addWidget(self.hard_pythagoras)
##        self.stack.addWidget(self.td_pythagoras_1)
##        self.stack.addWidget(self.td_pythagoras_2)
##        self.stack.addWidget(self.td_trigonometry_1)
##        self.stack.addWidget(self.td_trigonometry_2)
       
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
    
