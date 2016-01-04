from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
##from parent_class_menus import *
from easy_trig_widget import *
from parent_lesson_menu import *

class Trigonometry1(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.sides_aho_button = QPushButton("Sides AHO")
        self.sohcahtoa_button = QPushButton("SOHCAHTOA")
        self.blank = QLabel("Shape")
        self.back = QPushButton("Return")
        self.topic_label = QLabel("Trigonometry 1")
        self.select = QLabel("Please select a lesson: ")

        self.layout = QGridLayout()

        self.layout.addWidget(self.sides_aho_button, 2, 2)
        self.layout.addWidget(self.sohcahtoa_button, 3, 2)
        self.layout.addWidget(self.blank, 2, 0)
        self.layout.addWidget(self.back, 3, 0)
        self.layout.addWidget(self.topic_label, 0, 0)
        self.layout.addWidget(self.select, 1, 0)

        self.setLayout(self.layout)

        self.sides_aho_button.clicked.connect(self.SidesAHO)
        self.sohcahtoa_button.clicked.connect(self.SOHCAHTOA)
        self.back.clicked.connect(self.selected_back)
    
    def SidesAHO(self):
        sides_aho = SidesAHOWidget()
        sides_aho.show()
        sides_aho._raise()

    def SOHCAHTOA(self):
        sohcahtoa = SOHCAHTOAWidget()
        sohcahtoa.show()
        sohcahtoa._raise()

    def selected_back(self):
        self.close()

class Trigonometry2(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.finding_angles_button = QPushButton("Finding Angles")
        self.inverted_angles_button = QPushButton("Inverted Angles")
        self.three_d_trigonometry_button = QPushButton("3D Trigonometry")
        self.back = QPushButton("Return")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.finding_angles_button)
        self.layout.addWidget(self.inverted_angles_button)
        self.layout.addWidget(self.three_d_trigonometry_button)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.finding_angles_button.clicked.connect(self.FindingAngles)
        self.inverted_angles_button.clicked.connect(self.InvertedAngles)
        self.three_d_trigonometry_button.clicked.connect(self.ThreeDTrigonometry)
        self.back.clicked.connect(self.selected_back)
    
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

    def selected_back(self):
        self.close()

class Pythagoras(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.pythag_theorem_button = QPushButton("Pythagoras Theorem")
        self.three_d_pythagoras_button = QPushButton("3D Pythagoras")
        self.back = QPushButton("Return")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.pythag_theorem_button)
        self.layout.addWidget(self.three_d_pythagoras_button)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.pythag_theorem_button.clicked.connect(self.PythagTheorem)
        self.three_d_pythagoras_button.clicked.connect(self.ThreeDPythagoras)
        self.back.clicked.connect(self.selected_back)
    
    def PythagTheorem(self):
        pythag_theorem = PythagTheoremWidget()
        pythag_theorem.show()
        pythag_theorem._raise()

    def ThreeDPythagoras(self):
        three_d_pythag = ThreeDPythagorasWidget()
        three_d_pythag.show()
        three_d_pythag._raise()

    def selected_back(self):
        self.close()

class PythagTrig(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.easy_button = QPushButton("Easy")
        self.medium_button = QPushButton("Medium")
        self.hard_button = QPushButton("Hard")
        self.back = QPushButton("Return")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.easy_button)
        self.layout.addWidget(self.medium_button)
        self.layout.addWidget(self.hard_button)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.easy_button.clicked.connect(self.Easy)
        self.medium_button.clicked.connect(self.Medium)
        self.hard_button.clicked.connect(self.Hard)
        self.back.clicked.connect(self.selected_back)
    
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

    def selected_back(self):
        self.close()

class Summary(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.revise_trig_1_button = QPushButton("Revise Trigonometry 1")
        self.revise_trig_2_button = QPushButton("Revise Trigonometry 2")
        self.revise_trig_3_button = QPushButton("Revise Trigonometry 3")
        self.back = QPushButton("Return")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.revise_trig_1_button)
        self.layout.addWidget(self.revise_trig_2_button)
        self.layout.addWidget(self.revise_trig_3_button)
        self.layout.addWidget(self.back)

        self.setLayout(self.layout)

        self.revise_trig_1_button.clicked.connect(self.ReviseTrig1)
        self.revise_trig_2_button.clicked.connect(self.ReviseTrig2)
        self.revise_trig_3_button.clicked.connect(self.ReviseTrig3)
        self.back.clicked.connect(self.selected_back)
    
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

    def selected_back(self):
        self.close()
