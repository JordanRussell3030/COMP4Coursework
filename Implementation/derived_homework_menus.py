from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_homework import *
from easy_trig_widget import *
from homework_widgets import *

class Trigonometry1HW(QWidget):
    def __init__(self):
        super().__init__()

        self.sides_aho_easy_button = QPushButton("Sides AHO Easy")
        self.sides_aho_medium_button = QPushButton("Sides AHO Medium")
        self.sides_aho_hard_button = QPushButton("Sides AHO Hard")
        self.sohcahtoa_easy_button = QPushButton("SOHCAHTOA Easy")
        self.sohcahtoa_medium_button = QPushButton("SOHCAHTOA Medium")
        self.sohcahtoa_hard_button = QPushButton("SOHCAHTOA Hard")
        self.back_button = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.sides_aho_easy_button)
        self.layout.addWidget(self.sides_aho_medium_button)
        self.layout.addWidget(self.sides_aho_hard_button)
        self.layout.addWidget(self.sohcahtoa_easy_button)
        self.layout.addWidget(self.sohcahtoa_medium_button)
        self.layout.addWidget(self.sohcahtoa_hard_button)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)
        
        self.sides_aho_easy_button.clicked.connect(self.sides_aho_easy)
        self.sides_aho_medium_button.clicked.connect(self.sides_aho_medium)
        self.sides_aho_hard_button.clicked.connect(self.sides_aho_hard)
        self.sohcahtoa_easy_button.clicked.connect(self.sohcahtoa_easy)
        self.sohcahtoa_medium_button.clicked.connect(self.sohcahtoa_medium)
        self.sohcahtoa_hard_button.clicked.connect(self.sohcahtoa_hard)
        self.back_button.clicked.connect(self.selected_back)
    
    def sides_aho_easy(self):
        sides_aho_1 = SidesAHOEasyWidget()
        sides_aho_1.show()
        sides_aho_1._raise()

    def sides_aho_medium(self):
        sides_aho_2 = SidesAHOMediumWidget()
        sides_aho_2.show()
        sides_aho_2._raise()

    def sides_aho_hard(self):
        sides_aho_3 = SidesAHOHardWidget()
        sides_aho_3.show()
        sides_aho_3._raise()

    def sohcahtoa_easy(self):
        sohcahtoa_1 = SOHCAHTOAEasyWidget()
        sohcahtoa_1.show()
        sohcahtoa_1._raise()

    def sohcahtoa_medium(self):
        sohcahtoa_2 = SOHCAHTOAMediumWidget()
        sohcahtoa_2.show()
        sohcahtoa_3._raise()

    def sohcahtoa_hard(self):
        sohcahtoa_3 = SOHCAHTOAHardWidget()
        sohcahtoa_3.show()
        sohcahtoa_3._raise()

    def selected_back(self):
        pass

class Trigonometry2HW(QWidget):
    def __init__(self):
        super().__init__()

        self.finding_angles_easy_button = QPushButton("Finding Angles Easy")
        self.finding_angles_medium_button = QPushButton("Finding Angles Medium")
        self.finding_angles_hard_button = QPushButton("Finding Angles Hard")
        self.inverted_angles_easy_button = QPushButton("Inverted Angles Easy")
        self.inverted_angles_medium_button = QPushButton("Inverted Angles Medium")
        self.inverted_angles_hard_button = QPushButton("Inverted Angles Hard")
        self.three_d_trig_easy_button = QPushButton("3D Trigonometry Easy")
        self.three_d_trig_medium_button = QPushButton("3D Trigonometry Medium")
        self.three_d_trig_hard_button = QPushButton("3D Trigonometry Hard")
        self.back_button = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.finding_angles_easy_button)
        self.layout.addWidget(self.finding_angles_medium_button)
        self.layout.addWidget(self.finding_angles_hard_button)
        self.layout.addWidget(self.inverted_angles_easy_button)
        self.layout.addWidget(self.inverted_angles_medium_button)
        self.layout.addWidget(self.inverted_angles_hard_button)
        self.layout.addWidget(self.three_d_trig_easy_button)
        self.layout.addWidget(self.three_d_trig_medium_button)
        self.layout.addWidget(self.three_d_trig_hard_button)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.finding_angles_easy_button.clicked.connect(self.finding_angles_easy)
        self.finding_angles_medium_button.clicked.connect(self.finding_angles_medium)
        self.finding_angles_hard_button.clicked.connect(self.finding_angles_hard)
        self.inverted_angles_easy_button.clicked.connect(self.inverted_angles_easy)
        self.inverted_angles_medium_button.clicked.connect(self.inverted_angles_medium)
        self.inverted_angles_hard_button.clicked.connect(self.inverted_angles_hard)
        self.three_d_trig_easy_button.clicked.connect(self.three_d_trig_easy)
        self.three_d_trig_medium_button.clicked.connect(self.three_d_trig_medium)
        self.three_d_trig_hard_button.clicked.connect(self.three_d_trig_hard)
        self.back_button.clicked.connect(self.selected_back)
    
    def finding_angles_easy(self):
        finding_angles_1 = FindingAnglesEasyWidget()
        finding_angles_1.show()
        finding_angles_1._raise()

    def finding_angles_medium(self):
        finding_angles_2 = FindingAnglesMediumWidget()
        finding_angles_2.show()
        finding_angles_2._raise()

    def finding_angles_hard(self):
        finding_angles_3 = FindingAnglesHardWidget()
        finding_angles_3.show()
        finding_angles_3._raise()

    def inverted_angles_easy(self):
        inverted_angles_1 = InvertedAnglesEasyWidget()
        inverted_angles_1.show()
        inverted_angles_1._raise()

    def inverted_angles_medium(self):
        inverted_angles_2 = InvertedAnglesMediumWidget()
        inverted_angles_2.show()
        inverted_angles_2._raise()

    def inverted_angles_hard(self):
        inverted_angles_3 = InvertedAnglesHardWidget()
        inverted_angles_3.show()
        inverted_angles_3._raise()

    def three_d_trig_easy(self):
        three_d_trig_1 = ThreeDTrigEasyWidget()
        three_d_trig_1.show()
        three_d_trig_1._raise()

    def three_d_trig_medium(self):
        three_d_trig_2 = ThreeDTrigMediumWidget()
        three_d_trig_2.show()
        three_d_trig_2._raise()

    def three_d_trig_hard(self):
        three_d_trig_3 = ThreeDTrigHardWidget()
        three_d_trig_3.show()
        three_d_trig_3._raise()

    def selected_back(self):
        pass

class PythagorasHW(QWidget):
    def __init__(self):
        super().__init__()

        self.pythag_theorem_easy_button = QPushButton("Pythagoras' Theorem Easy")
        self.pythag_theorem_medium_button = QPushButton("Pythagoras' Theorem Medium")
        self.pythag_theorem_hard_button = QPushButton("Pythagoras' Theorem Hard")
        self.three_d_pythag_easy_button = QPushButton("3D Pythagoras Easy")
        self.three_d_pythag_medium_button = QPushButton("3D Pythagoras Medium")
        self.three_d_pythag_hard_button = QPushButton("3D Pythagoras Hard")
        self.back_button = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.pythag_theorem_easy_button)
        self.layout.addWidget(self.pythag_theorem_medium_button)
        self.layout.addWidget(self.pythag_theorem_hard_button)
        self.layout.addWidget(self.three_d_pythag_easy_button)
        self.layout.addWidget(self.three_d_pythag_medium_button)
        self.layout.addWidget(self.three_d_pythag_hard_button)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.pythag_theorem_easy_button.clicked.connect(self.pythag_theorem_easy)
        self.pythag_theorem_medium_button.clicked.connect(self.pythag_theorem_medium)
        self.pythag_theorem_hard_button.clicked.connect(self.pythag_theorem_hard)
        self.three_d_pythag_easy_button.clicked.connect(self.three_d_pythag_easy)
        self.three_d_pythag_medium_button.clicked.connect(self.three_d_pythag_medium)
        self.three_d_pythag_hard_button.clicked.connect(self.three_d_pythag_hard)
        self.back_button.clicked.connect(self.selected_back)
    
    def pythag_theorem_easy(self):
        pythag_theorem_1 = PythagTheoremEasyWidget()
        pythag_theorem_1.show()
        pythag_theorem_1._raise()

    def pythag_theorem_medium(self):
        pythag_theorem_2 = PythagTheoremMediumWidget()
        pythag_theorem_2.show()
        pythag_theorem_2._raise()

    def pythag_theorem_hard(self):
        pythag_theorem_3 = PythagTheoremHardWidget()
        pythag_theorem_3.show()
        pythag_theorem_3._raise()

    def three_d_pythag_easy(self):
        three_d_pythag_1 = ThreeDPythagEasyWidget()
        three_d_pythag_1.show()
        three_d_pythag._raise()

    def three_d_pythag_medium(self):
        three_d_pythag_2 = ThreeDPythagMediumWidget()
        three_d_pythag_2.show()
        three_d_pythag_2._raise()

    def three_d_pythag_hard(self):
        three_d_pythag_3 = ThreeDPythagHardWidget()
        three_d_pythag_3.show()
        three_d_pythag_3._raise()

    def selected_back(self):
        pass

class PythagTrigonometryHW(QWidget):
    def __init__(self):
        super().__init__()

        self.pythag_trig_problems_easy_button = QPushButton("Trigonometry and Pythagoras Problems Easy")
        self.pythag_trig_problems_medium_button = QPushButton("Trigonometry and Pythagoras Problems Mediu")
        self.pythag_trig_problems_hard_button = QPushButton("Trigonometry and Pythagoras Problems Hard")
        self.back_button= QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.pythag_trig_problems_easy_button)
        self.layout.addWidget(self.pythag_trig_problems_medium_button)
        self.layout.addWidget(self.pythag_trig_problems_hard_button)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.pythag_trig_problems_easy_button.clicked.connect(self.pythag_trig_problems_easy)
        self.pythag_trig_problems_medium_button.clicked.connect(self.pythag_trig_problems_medium)
        self.pythag_trig_problems_hard_button.clicked.connect(self.pythag_trig_problems_hard)
        self.back_button.clicked.connect(self.selected_back)
        
    def pythag_trig_problems_easy(self):
        pythag_trig_problems_1 = PythagTrigProblemsEasyWidget()
        pythag_trig_problems_1.show()
        pythag_trig_problems_1._raise()

    def pythag_trig_problems_medium(self):
        pythag_trig_problems_2 = PythagTrigProblemsMediumWidget()
        pythag_trig_problems_2.show()
        pythag_trig_problems_2._raise()

    def pythag_trig_problems_hard(self):
        pythag_trig_problems_3 = PythagTrigProblemsHardWidget()
        pythag_trig_problems_3.show()
        pythag_trig_problems_3._raise()

    def selected_back(self):
        pass

class SummaryHW(QWidget):
    def __init__(self):
        super().__init__()

        self.easy_summary_button = QPushButton("Easy Summary")
        self.medium_summary_button = QPushButton("Medium Summary")
        self.hard_summary_button = QPushButton("Hard Summary")
        self.back_button = QPushButton("Back")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.easy_summary_button)
        self.layout.addWidget(self.medium_summary_button)
        self.layout.addWidget(self.hard_summary_button)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

        self.easy_summary_button.clicked.connect(self.easy_summary)
        self.medium_summary_button.clicked.connect(self.medium_summary)
        self.hard_summary_button.clicked.connect(self.hard_summary)
        self.back_button.clicked.connect(self.selected_back)
          
    def easy_summary(self):
        summary_1 = EasySummaryWidget()
        summary_1.show()
        summary_1._raise()

    def medium_summary(self):
        summary_2 = MediumSummaryWidget()
        summary_2.show()
        summary_2._raise()

    def hard_summary(self):
        summary_3 = HardSummaryWidget()
        summary_3.show()
        summary_3._raise()

    def selected_back(self):
        pass
