from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_menus import *
from derived_lesson_menus import *
from homework_widgets_page_2 import *

class SidesAHOEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Sides AHO Easy")
        self.question_1 = QLabel("Question 1:\n ___________\n__________")
        self.question_1_shape = QLabel("Shape")
        self.answer_a = QLineEdit("___________\n___________")
        self.answer_b = QLineEdit("___________\n___________")
        self.answer_c = QLineEdit("___________\n___________")
        self.answer_d = QLineEdit("___________\n___________")
        self.answer_e = QLineEdit("___________\n___________")
        self.answer_f = QLineEdit("___________\n___________")
        self.score_box = QLabel("Score: X/X")
        self.cancel = QPushButton("Cancel")
        self.next = QPushButton("Next")
        self.check = QPushButton("Check Answers")
        self.reset = QPushButton("Reset Answers")

        self.layout = QGridLayout()

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.question_1, 1, 0)
        self.layout.addWidget(self.question_1_shape, 2, 0)
        self.layout.addWidget(self.answer_a, 1, 1)
        self.layout.addWidget(self.answer_b, 2, 1)
        self.layout.addWidget(self.answer_c, 3, 1)
        self.layout.addWidget(self.answer_d, 4, 1)
        self.layout.addWidget(self.answer_e, 5, 1)
        self.layout.addWidget(self.answer_f, 6, 1)
        self.layout.addWidget(self.score_box, 7, 1)
        self.layout.addWidget(self.check, 7, 2)
        self.layout.addWidget(self.reset, 8, 2)
        self.layout.addWidget(self.cancel, 8, 1)
        self.layout.addWidget(self.next, 9, 2)

        self.setLayout(self.layout)

        self.check.clicked.connect(self.check_selected)
        self.reset.clicked.connect(self.reset_selected)
        self.cancel.clicked.connect(self.cancel_selected)
        self.next.clicked.connect(self.next_selected)

    def check_selected(self):
        pass

    def reset_selected(self):
        pass

    def cancel_selected(self):
        pass

    def next_selected(self):
        self.page_2 = SidesAHOEasyWidget2()
        self.page_2.show()
        self.page_2._raise()
        
class SidesAHOMediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Sides AHO Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class SidesAHOHardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Sides AHO Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class SOHCAHTOAEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("SOHCAHTOA Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class SOHCAHTOAMediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("SOHCAHTOA Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class SOHCAHTOAHardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("SOHCAHTOA Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class FindingAnglesEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Finding Angles Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class FindingAnglesMediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Finding Angles Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class FindingAnglesHardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Finding Angles Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class InvertedAnglesEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Inverted Angles Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class InvertedAnglesMediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Inverted Angles Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class InvertedAnglesHardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Inverted Angles Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ThreeDTrigEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("3D Trigonometry Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ThreeDTrigMediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("3D Trigonometry Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ThreeDTrigHardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("3D Trigonometry Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class PythagTheoremEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pythagoras' Theorem Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class PythagTheoremMediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pythagoras' Theorem Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class PythagTheoremHardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pythagoras' Theorem Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ThreeDPythagEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("3D Pythagoras Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ThreeDPythagMediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("3D Pythagoras Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ThreeDPythagHardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("3D Pythagoras Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class PythagTrigProblemsEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pythagoras and Trigonometry Problems Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class PythagTrigProblemsMediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pythagoras and Trigonometry Problems Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class PythagTrigProblemsHardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pythagoras and Trigonometry Problems Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class EasySummaryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Summary Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class MediumSummaryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Summary Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class HardSummaryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Summary Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)
