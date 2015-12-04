from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_menus import *
from derived_lesson_menus import *
from parent_lesson_class import *

class SidesAHOWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.title = QLabel("Sides AHO")
        #self.lesson_1 = QTextFrame("Text")
        #self.lesson_2 = QTextFrame("Text")
        self.back = QPushButton("Return")
        self.next = QPushButton("Next")

        self.layout = QGridLayout()

        self.layout.addWidget(self.title, 0, 0)
##        self.layout.addWidget(self.lesson_1, 1, 0)
##        self.layout.addWidget(self.lesson_2, 0, 1)
        self.layout.addWidget(self.back, 0, 2)
        self.layout.addWidget(self.next, 0, 3)

        self.setLayout(self.layout)
##        self.lesson = ParentLessonPage1()
##        self.lesson.show()
##        self.lesson._raise()
##        
##        self._pass = QPushButton("Sides AHO")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##        
class SOHCAHTOAWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("SOHCAHTOA")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class FindingAnglesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Finding Angles")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class InvertedAnglesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Inverted Angles")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ThreeDTrigonometryWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("3D Trigonometry")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class PythagTheoremWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Pythagoras Theorem")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ThreeDPythagorasWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("3D Pythagoras")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class EasyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Easy")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class MediumWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Medium")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class HardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Hard")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ReviseTrig1Widget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Revise Trigonometry 1")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ReviseTrig2Widget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Revise Trigonometry 2")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class ReviseTrig3Widget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Revise Trigonometry 3")
        
        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)
