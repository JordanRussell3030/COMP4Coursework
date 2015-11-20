from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_menus import *
from easy_trig_widget import *

class EasyTrigonometry1(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_easy_1)
        self.lesson_2.clicked.connect(self.selected_easy_2)
        self.lesson_3.clicked.connect(self.selected_easy_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_easy_1(self):
        easy_1_1 = Easy1_1TrigWidget()
        easy_1_1.show()
        easy_1_1._raise()

    def selected_easy_2(self):
        easy_1_2 = Easy1_2TrigWidget()
        easy_1_2.show()
        easy_1_2._raise()

    def selected_easy_3(self):
        easy_1_3 = Easy1_3TrigWidget()
        easy_1_3.show()
        easy_1_3._raise()
        

    
