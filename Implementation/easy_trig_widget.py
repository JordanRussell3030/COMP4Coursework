from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from parent_class_menus import *
from derived_lesson_menus import *
from parent_lesson_class import *

class Easy1_1TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.lesson = ParentLessonPage1()
        self.lesson.show()
        self.lesson.raise_()
        
##        self._pass = QPushButton("Easy Trig 1.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
        
class Easy1_2TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Easy Trig 1.2")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class Easy1_3TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Easy Trig 1.3")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class Easy2_1TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Easy Trig 2.1")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class Easy2_2TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Easy Trig 2.2")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

class Easy2_3TrigWidget(QWidget):
    def __init__(self):
        super().__init__()
        self._pass = QPushButton("Easy Trig 2.3")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self._pass)

        self.setLayout(self.layout)

##class Easy3_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Easy Trig 3.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Easy3_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Easy Trig 3.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Easy3_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Easy Trig 3.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium1_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Trig 1.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium1_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Trig 1.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium1_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Trig 1.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium2_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Trig 2.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium2_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Trig 2.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium2_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Trig 2.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium3_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Trig 3.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium3_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Trig 3.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Medium3_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Meidum Trig 3.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard1_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Trig 1.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard1_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Trig 1.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard1_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Trig 1.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard2_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Trig 2.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard2_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard trig 2.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard2_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Trig 2.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard3_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Trig 3.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard3_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Trig 3.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Hard3_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Trig 3.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended1_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 1.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended1_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 1.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended1_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 1.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended2_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 2.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended2_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 2.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended2_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 2.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended3_1TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 3.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended3_2TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 3.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class Extended3_3TrigWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Extended Trig 3.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class EasyPythagoras1Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Easy Pythagoras 1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class EasyPythagoras2Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Easy Pythagoras 2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class EasyPythagoras3Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Easy Pythagoras 3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class MediumPythagoras1Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Pythagoras 1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class MediumPythagoras2Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Pythagoras 2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class MediumPythagoras3Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Medium Pythagoras 3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class HardPythagoras1Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Pythagoras 1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class HardPythagoras2Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Pythagoras 2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class HardPythagoras3Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("Hard Pythagoras 3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDPythagoras1_1Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Pythagoras 1.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDPythagoras1_2Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Pythagoras 1.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDPythagoras1_3Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Pythagoras 1.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDPythagoras2_1Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Pythagoras 2.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDPythagoras2_2Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Pythagoras 2.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDPythagoras2_3Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Pythagoras 2.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##
##class TDTrigonometry1_1Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Trigonometry 1.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDTrigonometry1_2Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Trigonometry 1.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDTrigonometry1_3Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Trigonometry 1.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDTrigonometry2_1Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Trigonometry 2.1")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDTrigonometry2_2Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Trigonometry 2.2")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
##class TDTrigonometry2_3Widget(QWidget):
##    def __init__(self):
##        super().__init__()
##        self._pass = QPushButton("3D Trigonometry 2.3")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self._pass)
##
##        self.setLayout(self.layout)
##
