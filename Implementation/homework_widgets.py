from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
##from parent_class_menus import *
from derived_lesson_menus import *
from homework_widgets_page_2 import *
from homework_parent_class import *

class SidesAHOEasyWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Sides Easy")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")
        
##        self.next = QPushButton("Next")
##        self.layout.addWidget(self.next, 9, 2)

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = SidesAHOEasyWidget2()
        self.page_2.show()
        self.page_2._raise()
        
class SidesAHOMediumWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Sides Medium")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = SidesAHOMediumWidget2()
        self.page_2.show()
        self.page_2._raise()

class SidesAHOHardWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Sides Hard")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = SidesAHOHardWidget2()
        self.page_2.show()
        self.page_2._raise()


class SOHCAHTOAEasyWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("SOHCAHTOA Easy")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")
        
        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = SOHCAHTOAEasyWidget2()
        self.page_2.show()
        self.page_2._raise()


class SOHCAHTOAMediumWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("SOHCAHTOA Medium")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = SOHCAHTOAMediumWidget2()
        self.page_2.show()
        self.page_2._raise()

class SOHCAHTOAHardWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("SOHCAHTOA Hard")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = SOHCAHTOAHardWidget2()
        self.page_2.show()
        self.page_2._raise()

class FindingAnglesEasyWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Finding Angles Easy")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = FindingAnglesEasyWidget2()
        self.page_2.show()
        self.page_2._raise()

class FindingAnglesMediumWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Finding Angles Medium")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = FindingAnglesMediumWidget2()
        self.page_2.show()
        self.page_2._raise()

class FindingAnglesHardWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Finding Angles Hard")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")
        
        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = FindingAnglesHardWidget2()
        self.page_2.show()
        self.page_2._raise()


class InvertedAnglesEasyWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Inverted Angles Easy")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = InvertedAnglesEasyWidget2()
        self.page_2.show()
        self.page_2._raise()


class InvertedAnglesMediumWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Inverted Angles Medium")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = InvertedAnglesMediumWidget2()
        self.page_2.show()
        self.page_2._raise()


class InvertedAnglesHardWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Inverted Angles Hard")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = InvertedAnglesHardWidget2()
        self.page_2.show()
        self.page_2._raise()


class ThreeDTrigEasyWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("3D Trigonometry Easy")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = ThreeDTrigEasyWidget2()
        self.page_2.show()
        self.page_2._raise()


class ThreeDTrigMediumWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("3D Trigonometry Medium")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = ThreeDTrigMediumWidget2()
        self.page_2.show()
        self.page_2._raise()


class ThreeDTrigHardWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("3D Trigonometry Hard")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = threeDTrigHardWidget2()
        self.page_2.show()
        self.page_2._raise()


class PythagTheoremEasyWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Pythagoras' Theorem Easy")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = PythagTheoremEasyWidget2()
        self.page_2.show()
        self.page_2._raise()


class PythagTheoremMediumWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Pythagoras' Theorem Medium")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = PythagTheoremMediumWidget2()
        self.page_2.show()
        self.page_2._raise()


class PythagTheoremHardWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Pythagoras' Theorem Hard")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = PythagTheoremHardWidget2()
        self.page_2.show()
        self.page_2._raise()


class ThreeDPythagEasyWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("3D Pythagoras Easy")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = ThreeDPythagEasyWidget2()
        self.page_2.show()
        self.page_2._raise()


class ThreeDPythagMediumWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("3D Trigonometry Medium")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = ThreeDPythagMediumWidget2()
        self.page_2.show()
        self.page_2._raise()


class ThreeDPythagHardWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("3D Pythagoras Hard")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = ThreeDPythagorasHardWidget2()
        self.page_2.show()
        self.page_2._raise()


class PythagTrigProblemsEasyWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Easy Problems")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = PythagTrigProblemsEasyWidget2()
        self.page_2.show()
        self.page_2._raise()

class PythagTrigProblemsMediumWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Medium Problems")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = PythagTrigProblemsMediumWidget2()
        self.page_2.show()
        self.page_2._raise()


class PythagTrigProblemsHardWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Hard Problems")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = PythagTrigProblemsHardWidget2()
        self.page_2.show()
        self.page_2._raise()


class EasySummaryWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Easy Summary")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = EasySummaryWidget2()
        self.page_2.show()
        self.page_2._raise()


class MediumSummaryWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Medium Summary")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = MediumSummaryWidget2()
        self.page_2.show()
        self.page_2._raise()


class HardSummaryWidget(ParentHomeworkPage1Class):
    def __init__(self):
        super().__init__()
        self.title.setText("Hard Summary")
        self.question_1.setText("Question 1:\n ___________\n__________")
        self.question_1_shape.setText("Shape")

        self.next.clicked.connect(self.next_selected)

    def next_selected(self):
        self.page_2 = HardSummaryWidget2()
        self.page_2.show()
        self.page_2._raise()
