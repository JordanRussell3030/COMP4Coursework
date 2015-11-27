from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_menus import *
from easy_trig_widget import *

class EasyTrigonometry1(ParentLesson):
    def __init__(self, parent):
        super().__init__(parent)

        self.lesson_1.clicked.connect(self.selected_easy_1)
        self.lesson_2.clicked.connect(self.selected_easy_2)
        self.lesson_3.clicked.connect(self.selected_easy_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_easy_1(self):
        easy_1_1 = Easy1_1TrigWidget(self)
        easy_1_1.show()
        easy_1_1.raise_()

    def selected_easy_2(self):
        easy_1_2 = Easy1_2TrigWidget(self)
        easy_1_2.show()
        easy_1_2.raise_()

    def selected_easy_3(self):
        easy_1_3 = Easy1_3TrigWidget(self)
        easy_1_3.show()
        easy_1_3.raise_()

class EasyTrigonometry2(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_easy_1)
        self.lesson_2.clicked.connect(self.selected_easy_2)
        self.lesson_3.clicked.connect(self.selected_easy_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_easy_1(self):
        easy_2_1 = Easy2_1TrigWidget(self)
        easy_2_1.show()
        easy_2_1.raise_()

    def selected_easy_2(self):
        easy_2_2 = Easy2_2TrigWidget(self)
        easy_2_2.show()
        easy_2_2.raise_()

    def selected_easy_3(self):
        easy_2_3 = Easy2_3TrigWidget(self)
        easy_2_3.show()
        easy_2_3.raise_()

##class EasyTrigonometry3(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_easy_1)
##        self.lesson_2.clicked.connect(self.selected_easy_2)
##        self.lesson_3.clicked.connect(self.selected_easy_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_easy_1(self):
##        easy_3_1 = Easy3_1TrigWidget(self)
##        easy_3_1.show()
##        easy_3_1.raise_()
##
##    def selected_easy_2(self):
##        easy_3_2 = Easy3_2TrigWidget(self)
##        easy_3_2.show()
##        easy_3_2.raise_()
##
##    def selected_easy_3(self):
##        easy_3_3 = Easy3_3TrigWidget(self)
##        easy_3_3.show()
##        easy_3_3.raise_()
##
##class MediumTrigonometry1(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_medium_1)
##        self.lesson_2.clicked.connect(self.selected_medium_2)
##        self.lesson_3.clicked.connect(self.selected_medium_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_medium_1(self):
##        medium_1_1 = Medium1_1TrigWidget(self)
##        medium_1_1.show()
##        medium_1_1.raise_()
##
##    def selected_medium_2(self):
##        medium_1_2 = Medium1_2TrigWidget(self)
##        medium_1_2.show()
##        medium_1_2.raise_()
##
##    def selected_medium_3(self):
##        medium_1_3 = Medium1_3TrigWidget(self)
##        medium_1_3.show()
##        medium_1_3.raise_()
##
##class MediumTrigonometry2(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_medium_1)
##        self.lesson_2.clicked.connect(self.selected_medium_2)
##        self.lesson_3.clicked.connect(self.selected_medium_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_medium_1(self):
##        medium_2_1 = Medium2_1TrigWidget(self)
##        medium_2_1.show()
##        medium_2_1.raise_()
##
##    def selected_medium_2(self):
##        medium_2_2 = Medium2_2TrigWidget(self)
##        medium_2_2.show()
##        medium_2_2.raise_()
##
##    def selected_medium_3(self):
##        medium_2_3 = Medium2_3TrigWidget(self)
##        medium_2_3.show()
##        medium_2_3.raise_()
##
##class MediumTrigonometry3(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_medium_1)
##        self.lesson_2.clicked.connect(self.selected_medium_2)
##        self.lesson_3.clicked.connect(self.selected_medium_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_medium_1(self):
##        medium_3_1 = Medium3_1TrigWidget(self)
##        medium_3_1.show()
##        medium_3_1.raise_()
##
##    def selected_medium_2(self):
##        medium_3_2 = Medium3_2TrigWidget(self)
##        medium_3_2.show()
##        medium_3_2.raise_()
##
##    def selected_medium_3(self):
##        medium_3_3 = Medium3_3TrigWidget(self)
##        medium_3_3.show()
##        medium_3_3.raise_()
##
##class HardTrigonometry1(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_hard_1)
##        self.lesson_2.clicked.connect(self.selected_hard_2)
##        self.lesson_3.clicked.connect(self.selected_hard_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_hard_1(self):
##        hard_1_1 = Hard1_1TrigWidget(self)
##        hard_1_1.show()
##        hard_1_1.raise_()
##
##    def selected_hard_2(self):
##        hard_1_2 = Hard1_2TrigWidget(self)
##        hard_1_2.show()
##        hard_1_2.raise_()
##
##    def selected_hard_3(self):
##        hard_1_3 = Hard1_3TrigWidget(self)
##        hard_1_3.show()
##        hard_1_3.raise_()
##
##class HardTrigonometry2(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_hard_1)
##        self.lesson_2.clicked.connect(self.selected_hard_2)
##        self.lesson_3.clicked.connect(self.selected_hard_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_hard_1(self):
##        hard_2_1 = Hard2_1TrigWidget(self)
##        hard_2_1.show()
##        hard_2_1.raise_()
##
##    def selected_hard_2(self):
##        hard_2_2 = Hard2_2TrigWidget(self)
##        hard_2_2.show()
##        hard_2_2.raise_()
##
##    def selected_hard_3(self):
##        hard_2_3 = Hard2_3TrigWidget(self)
##        hard_2_3.show()
##        hard_2_3.raise_()
##
##class HardTrigonometry3(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_hard_1)
##        self.lesson_2.clicked.connect(self.selected_hard_2)
##        self.lesson_3.clicked.connect(self.selected_hard_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_hard_1(self):
##        hard_3_1 = Hard3_1TrigWidget(self)
##        hard_3_1.show()
##        hard_3_1.raise_()
##
##    def selected_hard_2(self):
##        hard_3_2 = Hard3_2TrigWidget(self)
##        hard_3_2.show()
##        hard_3_2.raise_()
##
##    def selected_hard_3(self):
##        hard_3_3 = Hard3_3TrigWidget(self)
##        hard_3_3.show()
##        hard_3_3.raise_()
##
##class ExtendedTrigonometry1(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_extended_1)
##        self.lesson_2.clicked.connect(self.selected_extended_2)
##        self.lesson_3.clicked.connect(self.selected_extended_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_extended_1(self):
##        extended_1_1 = Extended1_1TrigWidget(self)
##        extended_1_1.show()
##        extended_1_1.raise_()
##
##    def selected_extended_2(self):
##        extended_1_2 = Extended1_2TrigWidget(self)
##        extended_1_2.show()
##        extended_1_2.raise_()
##
##    def selected_extended_3(self):
##        extended_1_3 = Extended1_3TrigWidget(self)
##        extended_1_3.show()
##        extended_1_3.raise_()
##
##class ExtendedTrigonometry2(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_extended_1)
##        self.lesson_2.clicked.connect(self.selected_extended_2)
##        self.lesson_3.clicked.connect(self.selected_extended_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_extended_1(self):
##        extended_2_1 = Extended2_1TrigWidget(self)
##        extended_2_1.show()
##        extended_2_1.raise_()
##
##    def selected_extended_2(self):
##        extended_2_2 = Extended2_2TrigWidget(self)
##        extended_2_2.show()
##        extended_2_2.raise_()
##
##    def selected_extended_3(self):
##        extended_2_3 = Extended2_3TrigWidget(self)
##        extended_2_3.show()
##        extended_2_3.raise_()
##
##class ExtendedTrigonometry3(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_extended_1)
##        self.lesson_2.clicked.connect(self.selected_extended_2)
##        self.lesson_3.clicked.connect(self.selected_extended_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_extended_1(self):
##        extended_3_1 = Extended3_1TrigWidget(self)
##        extended_3_1.show()
##        extended_3_1.raise_()
##
##    def selected_extended_2(self):
##        extended_3_2 = Extended3_2TrigWidget(self)
##        extended_3_2.show()
##        extended_3_2.raise_()
##
##    def selected_extended_3(self):
##        extended_3_3 = Extended3_3TrigWidget(self)
##        extended_3_3.show()
##        extended_3_3.raise_()
##        
##class EasyPythagoras(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_easy_pythag_1)
##        self.lesson_2.clicked.connect(self.selected_easy_pythag_2)
##        self.lesson_3.clicked.connect(self.selected_easy_pythag_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_easy_pythag_1(self):
##        easy_1_1 = EasyPythagoras1Widget(self)
##        easy_1_1.show()
##        easy_1_1.raise_()
##
##    def selected_easy_pythag_2(self):
##        easy_1_2 = EasyPythagoras2Widget(self)
##        easy_1_2.show()
##        easy_1_2.raise_()
##
##    def selected_easy_pythag_3(self):
##        easy_1_3 = EasyPythagoras3Widget(self)
##        easy_1_3.show()
##        easy_1_3.raise_()
##
##class MediumPythagoras(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_medium_pythag_1)
##        self.lesson_2.clicked.connect(self.selected_medium_pythag_2)
##        self.lesson_3.clicked.connect(self.selected_medium_pythag_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_medium_pythag_1(self):
##        medium_1_1 = MediumPythagoras1Widget(self)
##        medium_1_1.show()
##        medium_1_1.raise_()
##
##    def selected_medium_pythag_2(self):
##        medium_1_2 = MediumPythagoras2Widget(self)
##        medium_1_2.show()
##        medium_1_2.raise_()
##
##    def selected_medium_pythag_3(self):
##        medium_1_3 = MediumPythagoras3Widget(self)
##        medium_1_3.show()
##        medium_1_3.raise_()
##
##class HardPythagoras(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_hard_pythag_1)
##        self.lesson_2.clicked.connect(self.selected_hard_pythag_2)
##        self.lesson_3.clicked.connect(self.selected_hard_pythag_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_hard_pythag_1(self):
##        hard_1_1 = HardPythagoras1Widget(self)
##        hard_1_1.show()
##        hard_1_1.raise_()
##
##    def selected_hard_pythag_2(self):
##        hard_1_2 = HardPythagoras2Widget(self)
##        hard_1_2.show()
##        hard_1_2.raise_()
##
##    def selected_hard_pythag_3(self):
##        hard_1_3 = HardPythagoras3Widget(self)
##        hard_1_3.show()
##        hard_1_3.raise_()
##
##class TDPythagoras1(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_threed_pythag_1)
##        self.lesson_2.clicked.connect(self.selected_threed_pythag_2)
##        self.lesson_3.clicked.connect(self.selected_threed_pythag_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_threed_pythag_1(self):
##        threed_1_1 = TDPythagoras1_1Widget(self)
##        threed_1_1.show()
##        threed_1_1.raise_()
##
##    def selected_threed_pythag_2(self):
##        threed_1_2 = TDPythagoras1_2Widget(self)
##        threed_1_2.show()
##        threed_1_2.raise_()
##
##    def selected_threed_pythag_3(self):
##        threed_1_3 = TDPythagoras1_3Widget(self)
##        threed_1_3.show()
##        threed_1_3.raise_()
##
##class TDPythagoras2(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_threed_pythag_1)
##        self.lesson_2.clicked.connect(self.selected_threed_pythag_2)
##        self.lesson_3.clicked.connect(self.selected_threed_pythag_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_threed_pythag_1(self):
##        threed_2_1 = TDPythagoras2_1Widget(self)
##        threed_2_1.show()
##        threed_2_1.raise_()
##
##    def selected_threed_pythag_2(self):
##        threed_2_2 = TDPythagoras2_2Widget(self)
##        threed_2_2.show()
##        threed_2_2.raise_()
##
##    def selected_threed_pythag_3(self):
##        threed_2_3 = TDPythagoras2_3Widget(self)
##        threed_2_3.show()
##        threed_2_3.raise_()
##
##class TDTrigonometry1(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_threed_trig_1)
##        self.lesson_2.clicked.connect(self.selected_threed_trig_2)
##        self.lesson_3.clicked.connect(self.selected_threed_trig_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_threed_trig_1(self):
##        threed_1_1 = TDTrigonometry1_1Widget(self)
##        threed_1_1.show()
##        threed_1_1.raise_()
##
##    def selected_threed_trig_2(self):
##        threed_1_2 = TDTrigonometry1_2Widget(self)
##        threed_1_2.show()
##        threed_1_2.raise_()
##
##    def selected_threed_trig_3(self):
##        threed_1_3 = TDTrigonometry1_3Widget(self)
##        threed_1_3.show()
##        threed_1_3.raise_()
##
##class TDTrigonometry2(ParentLesson):
##    def __init__(self):
##        super().__init__()
##
##        self.lesson_1.clicked.connect(self.selected_threed_trig_1)
##        self.lesson_2.clicked.connect(self.selected_threed_trig_2)
##        self.lesson_3.clicked.connect(self.selected_threed_trig_3)
##        self.back.clicked.connect(self.selected_back)
##    
##    def selected_threed_trig_1(self):
##        threed_2_1 = TDTrigonometry2_1Widget(self)
##        threed_2_1.show()
##        threed_2_1.raise_()
##
##    def selected_threed_trig_2(self):
##        threed_2_2 = TDTrigonometry2_2Widget(self)
##        threed_2_2.show()
##        threed_2_2.raise_()
##
##    def selected_threed_trig_3(self):
##        threed_2_3 = TDTrigonometry2_3Widget(self)
##        threed_2_3.show()
##        threed_2_3.raise_()
##
##
    
