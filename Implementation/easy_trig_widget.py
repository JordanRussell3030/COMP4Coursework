from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
#
from lesson_menu_widget import *
from homework_menu_widget import *
##from parent_class_menus import *
from derived_lesson_menus import *
##from parent_lesson_class import *
from lesson_page_2 import *
from lesson_layout_parent_class import *

class SidesAHOWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        
        self.title.setText("Sides")
        self.lesson_1.setText("Every triangle has 3 sides, and each side has a name. The HYPOTENUSE is the longest side. The OPPOSITE is the side opposite the angle being used. The ADJACENT is next to the angle being used.")
        self.lesson_2.setText("How to do this")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sides_l = SidesAHOWidgetPage2()
        sides_l.show()
        sides_l._raise()
       
class SOHCAHTOAWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("SOHCAHTOA")
        self.lesson_1.setText("SOHCAHTOA stands for: \nSine Opposite Hypotenuse\nCosine Adjacent Hypotenuse\nTan Opposite Adjacent.\nThis is the best way to remember the three different rules for working out trigonometry problems. They each turn into a FORMULA TRIANGLE, a triangle which shows the formula inside in a memorable format.")
        self.lesson_2.setText("Method\n1. Label the three sides O, A and H\n2. Write down from memory SOHCAHTOA\n3. Decide which two sides are involved: O,H, A,H or O,A\n4. Turn the one you choose into one of the formula triangles to the left of the screen\n5. Cover up the thing you want to find and write down whateveris left showing\n6. Translate into numbers and work it out\n7. Finally, check that your answer is sensible")

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("formula_triangles.png"))
##        self.pic.setMaximumWidth(300)
##        self.pic.setMaximumHeight(200)
##
##        self.pic_2 = QLabel()
##        self.pic_2.setPixmap(QPixmap("cosine_formula_triangle.png"))
##
##        self.pic_3 = QLabel()
##        self.pic_3.setPixmap(QPixmap("tan_formula_triangle.png"))

        self.next.clicked.connect(self.selected_next)

        self.layout.addWidget(self.pic, 2, 0)
##        self.layout.addWidget(self.pic_2, 2, 1)
##        self.layout.addWidget(self.pic_3, 2, 2)

##        self.layout.addWidget(self.pic, 0, 5)

    def selected_next(self):
        sohcahtoa_l = SOHCAHTOAWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class FindingAnglesWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Finding Angles")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = FindingAnglesWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class InvertedAnglesWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Inverted Angles")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = InvertedAnglesWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class ThreeDTrigonometryWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("3D Trigonometry")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = ThreeDTrigonometryWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class PythagTheoremWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Pythagoras' Theorem")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = PythagTheoremWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class ThreeDPythagorasWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("3D Pythagoras")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = ThreeDPythagorasWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class EasyWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Easy Problems")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = EasyWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class MediumWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Medium Problems")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = MediumWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class HardWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Hard Problems")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = HardWidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class ReviseTrig1Widget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Revise Trigonometry 1")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = ReviseTrig1WidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()

class ReviseTrig2Widget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Revise Trigonometry 2")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = ReviseTrig2WidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()


class ReviseTrig3Widget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        self.title.setText("Revise Trigonometry 3")
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")
        self.next.clicked.connect(self.selected_next)

    def selected_next(self):
        sohcahtoa_l = ReviseTrig3WidgetPage2()
        sohcahtoa_l.show()
        sohcahtoa_l._raise()
