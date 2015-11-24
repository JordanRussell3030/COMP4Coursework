from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_homework import *
from easy_trig_widget import *
from homework_widgets import *

class EasyTrigonometry1HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_easy_1)
        self.lesson_2.clicked.connect(self.selected_easy_2)
        self.lesson_3.clicked.connect(self.selected_easy_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_easy_1(self):
        easy_1_1 = Easy1_1TrigWidgetHW()
        easy_1_1.show()
        easy_1_1._raise()

    def selected_easy_2(self):
        easy_1_2 = Easy1_2TrigWidgetHW()
        easy_1_2.show()
        easy_1_2._raise()

    def selected_easy_3(self):
        easy_1_3 = Easy1_3TrigWidgetHW()
        easy_1_3.show()
        easy_1_3._raise()

class EasyTrigonometry2HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_easy_1)
        self.lesson_2.clicked.connect(self.selected_easy_2)
        self.lesson_3.clicked.connect(self.selected_easy_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_easy_1(self):
        easy_2_1 = Easy2_1TrigWidgetHW()
        easy_2_1.show()
        easy_2_1._raise()

    def selected_easy_2(self):
        easy_2_2 = Easy2_2TrigWidgetHW()
        easy_2_2.show()
        easy_2_2._raise()

    def selected_easy_3(self):
        easy_2_3 = Easy2_3TrigWidgetHW()
        easy_2_3.show()
        easy_2_3._raise()

class EasyTrigonometry3HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_easy_1)
        self.lesson_2.clicked.connect(self.selected_easy_2)
        self.lesson_3.clicked.connect(self.selected_easy_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_easy_1(self):
        easy_3_1 = Easy3_1TrigWidgetHW()
        easy_3_1.show()
        easy_3_1._raise()

    def selected_easy_2(self):
        easy_3_2 = Easy3_2TrigWidgetHW()
        easy_3_2.show()
        easy_3_2._raise()

    def selected_easy_3(self):
        easy_3_3 = Easy3_3TrigWidgetHW()
        easy_3_3.show()
        easy_3_3._raise()

class MediumTrigonometry1HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_medium_1)
        self.lesson_2.clicked.connect(self.selected_medium_2)
        self.lesson_3.clicked.connect(self.selected_medium_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_medium_1(self):
        medium_1_1 = Medium1_1TrigWidgetHW()
        medium_1_1.show()
        medium_1_1._raise()

    def selected_medium_2(self):
        medium_1_2 = Medium1_2TrigWidgetHW()
        medium_1_2.show()
        medium_1_2._raise()

    def selected_medium_3(self):
        medium_1_3 = Medium1_3TrigWidgetHW()
        medium_1_3.show()
        medium_1_3._raise()

class MediumTrigonometry2HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_medium_1)
        self.lesson_2.clicked.connect(self.selected_medium_2)
        self.lesson_3.clicked.connect(self.selected_medium_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_medium_1(self):
        medium_2_1 = Medium2_1TrigWidgetHW()
        medium_2_1.show()
        medium_2_1._raise()

    def selected_medium_2(self):
        medium_2_2 = Medium2_2TrigWidgetHW()
        medium_2_2.show()
        medium_2_2._raise()

    def selected_medium_3(self):
        medium_2_3 = Medium2_3TrigWidgetHW()
        medium_2_3.show()
        medium_2_3._raise()

class MediumTrigonometry3HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_medium_1)
        self.lesson_2.clicked.connect(self.selected_medium_2)
        self.lesson_3.clicked.connect(self.selected_medium_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_medium_1(self):
        medium_3_1 = Medium3_1TrigWidgetHW()
        medium_3_1.show()
        medium_3_1._raise()

    def selected_medium_2(self):
        medium_3_2 = Medium3_2TrigWidgetHW()
        medium_3_2.show()
        medium_3_2._raise()

    def selected_medium_3(self):
        medium_3_3 = Medium3_3TrigWidgetHW()
        medium_3_3.show()
        medium_3_3._raise()

class HardTrigonometry1HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_hard_1)
        self.lesson_2.clicked.connect(self.selected_hard_2)
        self.lesson_3.clicked.connect(self.selected_hard_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_hard_1(self):
        hard_1_1 = Hard1_1TrigWidgetHW()
        hard_1_1.show()
        hard_1_1._raise()

    def selected_hard_2(self):
        hard_1_2 = Hard1_2TrigWidgetHW()
        hard_1_2.show()
        hard_1_2._raise()

    def selected_hard_3(self):
        hard_1_3 = Hard1_3TrigWidgetHW()
        hard_1_3.show()
        hard_1_3._raise()

class HardTrigonometry2HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_hard_1)
        self.lesson_2.clicked.connect(self.selected_hard_2)
        self.lesson_3.clicked.connect(self.selected_hard_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_hard_1(self):
        hard_2_1 = Hard2_1TrigWidgetHW()
        hard_2_1.show()
        hard_2_1._raise()

    def selected_hard_2(self):
        hard_2_2 = Hard2_2TrigWidgetHW()
        hard_2_2.show()
        hard_2_2._raise()

    def selected_hard_3(self):
        hard_2_3 = Hard2_3TrigWidgetHW()
        hard_2_3.show()
        hard_2_3._raise()

class HardTrigonometry3HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_hard_1)
        self.lesson_2.clicked.connect(self.selected_hard_2)
        self.lesson_3.clicked.connect(self.selected_hard_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_hard_1(self):
        hard_3_1 = Hard3_1TrigWidgetHW()
        hard_3_1.show()
        hard_3_1._raise()

    def selected_hard_2(self):
        hard_3_2 = Hard3_2TrigWidgetHW()
        hard_3_2.show()
        hard_3_2._raise()

    def selected_hard_3(self):
        hard_3_3 = Hard3_3TrigWidgetHW()
        hard_3_3.show()
        hard_3_3._raise()

class ExtendedTrigonometry1HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_extended_1)
        self.lesson_2.clicked.connect(self.selected_extended_2)
        self.lesson_3.clicked.connect(self.selected_extended_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_extended_1(self):
        extended_1_1 = Extended1_1TrigWidgetHW()
        extended_1_1.show()
        extended_1_1._raise()

    def selected_extended_2(self):
        extended_1_2 = Extended1_2TrigWidgetHW()
        extended_1_2.show()
        extended_1_2._raise()

    def selected_extended_3(self):
        extended_1_3 = Extended1_3TrigWidgetHW()
        extended_1_3.show()
        extended_1_3._raise()

class ExtendedTrigonometry2HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_extended_1)
        self.lesson_2.clicked.connect(self.selected_extended_2)
        self.lesson_3.clicked.connect(self.selected_extended_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_extended_1(self):
        extended_2_1 = Extended2_1TrigWidgetHW()
        extended_2_1.show()
        extended_2_1._raise()

    def selected_extended_2(self):
        extended_2_2 = Extended2_2TrigWidgetHW()
        extended_2_2.show()
        extended_2_2._raise()

    def selected_extended_3(self):
        extended_2_3 = Extended2_3TrigWidgetHW()
        extended_2_3.show()
        extended_2_3._raise()

class ExtendedTrigonometry3HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_extended_1)
        self.lesson_2.clicked.connect(self.selected_extended_2)
        self.lesson_3.clicked.connect(self.selected_extended_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_extended_1(self):
        extended_3_1 = Extended3_1TrigWidgetHW()
        extended_3_1.show()
        extended_3_1._raise()

    def selected_extended_2(self):
        extended_3_2 = Extended3_2TrigWidgetHW()
        extended_3_2.show()
        extended_3_2._raise()

    def selected_extended_3(self):
        extended_3_3 = Extended3_3TrigWidgetHW()
        extended_3_3.show()
        extended_3_3._raise()
        
class EasyPythagorasHW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_easy_pythag_1)
        self.lesson_2.clicked.connect(self.selected_easy_pythag_2)
        self.lesson_3.clicked.connect(self.selected_easy_pythag_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_easy_pythag_1(self):
        easy_1_1 = EasyPythagoras1WidgetHW()
        easy_1_1.show()
        easy_1_1._raise()

    def selected_easy_pythag_2(self):
        easy_1_2 = EasyPythagoras2WidgetHW()
        easy_1_2.show()
        easy_1_2._raise()

    def selected_easy_pythag_3(self):
        easy_1_3 = EasyPythagoras3WidgetHW()
        easy_1_3.show()
        easy_1_3._raise()

class MediumPythagorasHW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_medium_pythag_1)
        self.lesson_2.clicked.connect(self.selected_medium_pythag_2)
        self.lesson_3.clicked.connect(self.selected_medium_pythag_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_medium_pythag_1(self):
        medium_1_1 = MediumPythagoras1WidgetHW()
        medium_1_1.show()
        medium_1_1._raise()

    def selected_medium_pythag_2(self):
        medium_1_2 = MediumPythagoras2WidgetHW()
        medium_1_2.show()
        medium_1_2._raise()

    def selected_medium_pythag_3(self):
        medium_1_3 = MediumPythagoras3WidgetHW()
        medium_1_3.show()
        medium_1_3._raise()

class HardPythagorasHW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_hard_pythag_1)
        self.lesson_2.clicked.connect(self.selected_hard_pythag_2)
        self.lesson_3.clicked.connect(self.selected_hard_pythag_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_hard_pythag_1(self):
        hard_1_1 = HardPythagoras1WidgetHW()
        hard_1_1.show()
        hard_1_1._raise()

    def selected_hard_pythag_2(self):
        hard_1_2 = HardPythagoras2WidgetHW()
        hard_1_2.show()
        hard_1_2._raise()

    def selected_hard_pythag_3(self):
        hard_1_3 = HardPythagoras3WidgetHW()
        hard_1_3.show()
        hard_1_3._raise()

class TDPythagoras1HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_threed_pythag_1)
        self.lesson_2.clicked.connect(self.selected_threed_pythag_2)
        self.lesson_3.clicked.connect(self.selected_threed_pythag_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_threed_pythag_1(self):
        threed_1_1 = TDPythagoras1_1WidgetHW()
        threed_1_1.show()
        threed_1_1._raise()

    def selected_threed_pythag_2(self):
        threed_1_2 = TDPythagoras1_2WidgetHW()
        threed_1_2.show()
        threed_1_2._raise()

    def selected_threed_pythag_3(self):
        threed_1_3 = TDPythagoras1_3WidgetHW()
        threed_1_3.show()
        threed_1_3._raise()

class TDPythagoras2HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_threed_pythag_1)
        self.lesson_2.clicked.connect(self.selected_threed_pythag_2)
        self.lesson_3.clicked.connect(self.selected_threed_pythag_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_threed_pythag_1(self):
        threed_2_1 = TDPythagoras2_1WidgetHW()
        threed_2_1.show()
        threed_2_1._raise()

    def selected_threed_pythag_2(self):
        threed_2_2 = TDPythagoras2_2WidgetHW()
        threed_2_2.show()
        threed_2_2._raise()

    def selected_threed_pythag_3(self):
        threed_2_3 = TDPythagoras2_3WidgetHW()
        threed_2_3.show()
        threed_2_3._raise()

class TDTrigonometry1HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_threed_trig_1)
        self.lesson_2.clicked.connect(self.selected_threed_trig_2)
        self.lesson_3.clicked.connect(self.selected_threed_trig_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_threed_trig_1(self):
        threed_1_1 = TDTrigonometry1_1WidgetHW()
        threed_1_1.show()
        threed_1_1._raise()

    def selected_threed_trig_2(self):
        threed_1_2 = TDTrigonometry1_2WidgetHW()
        threed_1_2.show()
        threed_1_2._raise()

    def selected_threed_trig_3(self):
        threed_1_3 = TDTrigonometry1_3WidgetHW()
        threed_1_3.show()
        threed_1_3._raise()

class TDTrigonometry2HW(ParentLesson):
    def __init__(self):
        super().__init__()

        self.lesson_1.clicked.connect(self.selected_threed_trig_1)
        self.lesson_2.clicked.connect(self.selected_threed_trig_2)
        self.lesson_3.clicked.connect(self.selected_threed_trig_3)
        self.back.clicked.connect(self.selected_back)
    
    def selected_threed_trig_1(self):
        threed_2_1 = TDTrigonometry2_1WidgetHW()
        threed_2_1.show()
        threed_2_1._raise()

    def selected_threed_trig_2(self):
        threed_2_2 = TDTrigonometry2_2WidgetHW()
        threed_2_2.show()
        threed_2_2._raise()

    def selected_threed_trig_3(self):
        threed_2_3 = TDTrigonometry2_3WidgetHW()
        threed_2_3.show()
        threed_2_3._raise()
