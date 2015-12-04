from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_menus import *
from derived_lesson_menus import *

class SidesAHOEasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Sides AHO Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)
        
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
