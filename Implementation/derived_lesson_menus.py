from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
#
from lesson_menu_widget import *
from homework_menu_widget import *
##from parent_class_menus import *
from easy_trig_widget import *
from parent_lesson_menu import *
##from default_button_widget import *

class Trigonometry1(ParentLessonMenu):
    def __init__(self):
        super().__init__()
        self.title.setText("Trigonometry 1")

        self.button_1.setText("Sides")
        self.button_2.setText("SOHCAHTOA")
        
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 1, 1)
        self.layout.addWidget(self.button_2, 0, 1)

        self.button_1.clicked.connect(self.SidesAHO)
        self.button_2.clicked.connect(self.SOHCAHTOA)
    
    def SidesAHO(self):
        sides_aho = SidesAHOWidget()
        sides_aho.show()
        sides_aho._raise()

    def SOHCAHTOA(self):
        sohcahtoa = SOHCAHTOAWidget()
        sohcahtoa.show()
        sohcahtoa._raise()

class Trigonometry2(ParentLessonMenu):
    def __init__(self):
        super().__init__()
        
        self.title.setText("Trigonometry 2")

        self.button_1.setText("Finding Angles")
        self.button_2.setText("Inverted Angles")
        self.button_3.setText("3D Trigonometry")

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 0, 1)
        self.layout.addWidget(self.button_2, 1, 1)
        self.layout.addWidget(self.button_3, 2, 1)

        self.button_1.clicked.connect(self.FindingAngles)
        self.button_2.clicked.connect(self.InvertedAngles)
        self.button_3.clicked.connect(self.ThreeDTrigonometry)
    
    def FindingAngles(self):
        finding_angles = FindingAnglesWidget()
        finding_angles.show()
        finding_angles._raise()

    def InvertedAngles(self):
        inverted_angles = InvertedAnglesWidget()
        inverted_angles.show()
        inverted_angles._raise()

    def ThreeDTrigonometry(self):
        three_d_trig = ThreeDTrigonometryWidget()
        three_d_trig.show()
        three_d_trig._raise()

class Pythagoras(ParentLessonMenu):
    def __init__(self):
        super().__init__()
        
        self.title.setText("Pythagoras")

        self.button_1.setText("Pythagoras' Theorem")
        self.button_2.setText("3D Pythagoras")

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 0, 1)
        self.layout.addWidget(self.button_2, 1, 1)

        self.button_1.clicked.connect(self.PythagTheorem)
        self.button_2.clicked.connect(self.ThreeDPythagoras)
    
    def PythagTheorem(self):
        pythag_theorem = PythagTheoremWidget()
        pythag_theorem.show()
        pythag_theorem._raise()

    def ThreeDPythagoras(self):
        three_d_pythag = ThreeDPythagorasWidget()
        three_d_pythag.show()
        three_d_pythag._raise()

class PythagTrig(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.title.setText("Pythagoras and Trigonometry Problems")

        self.button_1.setText("Easy")
        self.button_2.setText("Medium")
        self.button_3.setText("Hard")

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 0, 1)
        self.layout.addWidget(self.button_2, 1, 1)
        self.layout.addWidget(self.button_3, 2, 1)

        self.button_1.clicked.connect(self.Easy)
        self.button_2.clicked.connect(self.Medium)
        self.button_3.clicked.connect(self.Hard)
    
    def Easy(self):
        easy = EasyWidget()
        easy.show()
        easy._raise()

    def Medium(self):
        medium = MediumWidget()
        medium.show()
        medium._raise()

    def Hard(self):
        hard = HardWidget()
        hard.show()
        hard._raise()

class Summary(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.title.setText("Summary")

        self.button_1.setText("Easy")
        self.button_2.setText("Medium")
        self.button_3.setText("Hard")
        
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 0, 1)
        self.layout.addWidget(self.button_2, 1, 1)
        self.layout.addWidget(self.button_3, 2, 1)

        self.button_1.clicked.connect(self.ReviseTrig1)
        self.button_2.clicked.connect(self.ReviseTrig2)
        self.button_3.clicked.connect(self.ReviseTrig3)
    
    def ReviseTrig1(self):
        revise_trig_1 = ReviseTrig1Widget()
        revise_trig_1.show()
        revise_trig_1._raise()

    def ReviseTrig2(self):
        revise_trig_2 = ReviseTrig2Widget()
        revise_trig_2.show()
        revise_trig_2._raise()

    def ReviseTrig3(self):
        revise_trig_3 = ReviseTrig3Widget()
        revise_trig_3.show()
        revise_trig_3._raise()
