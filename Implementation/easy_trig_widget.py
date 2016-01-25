from PyQt4.QtGui import *
from PyQt4.QtCore import *

from lesson_page_2 import *
from lesson_layout_parent_class import *

class SidesAHOWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("sides_lesson_title"))
        self.lesson_1.setText("Every triangle has 3 sides, and each side has a name. The HYPOTENUSE is the longest side. The OPPOSITE is the side opposite the angle being used. The ADJACENT is next to the angle being used.")
        self.lesson_2.setText("How to do this")

        self.second_window = SidesAHOWidgetPage2()
       
class SOHCAHTOAWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()
        
        self.title.setPixmap(QPixmap("sohcahtoa_lesson_title"))
        self.lesson_1.setText("SOHCAHTOA stands for: \nSine Opposite Hypotenuse\nCosine Adjacent Hypotenuse\nTan Opposite Adjacent.\nThis is the best way to remember the three different rules for working out trigonometry problems. They each turn into a FORMULA TRIANGLE, a triangle which shows the formula inside in a memorable format.")
        self.lesson_2.setText("Method\n1. Label the three sides O, A and H\n2. Write down from memory SOHCAHTOA\n3. Decide which two sides are involved: O,H, A,H or O,A\n4. Turn the one you choose into one of the formula triangles to the left of the screen\n5. Cover up the thing you want to find and write down whatever is left showing\n6. Translate into numbers and work it out\n7. Finally, check that your answer is sensible")

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("formula_triangles.png"))

        self.layout.addWidget(self.pic, 2, 0)

        self.second_window = SOHCAHTOAWidgetPage2()

class FindingAnglesWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = FindingAnglesWidgetPage2()
        
        self.title.setPixmap(QPixmap("finding_angles_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class InvertedAnglesWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = InvertedAnglesWidgetPage2()
        
        self.title.setPixmap(QPixmap("inverted_angles_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class ThreeDTrigonometryWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = ThreeDTrigonometryWidgetPage2()
        
        self.title.setPixmap(QPixmap("three_d_trig_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class PythagTheoremWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = PythagTheoremWidgetPage2()
        
        self.title.setPixmap(QPixmap("pythag_theorem_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class ThreeDPythagorasWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = ThreeDPythagorasWidgetPage2()
        
        self.title.setPixmap(QPixmap("three_d_pythag_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class EasyWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = EasyWidgetPage2()
        
        self.title.setPixmap(QPixmap("vectors_1_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class MediumWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = MediumWidgetPage2()
        
        self.title.setPixmap(QPixmap("vectors_2_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class HardWidget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = HardWidgetPage2()
        
        self.title.setPixmap(QPixmap("vectors_3_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class ReviseTrig1Widget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = ReviseTrig1Page2()
        
        self.title.setPixmap(QPixmap("easy_summary_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class ReviseTrig2Widget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = ReviseTrig2Page2()
        
        self.title.setPixmap(QPixmap("medium_summary_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")

class ReviseTrig3Widget(ParentLessonLayout):
    def __init__(self):
        super().__init__()

        self.second_window = ReviseTrig3Page2()
        
        self.title.setPixmap(QPixmap("hard_summary_lesson_title"))
        self.lesson_1.setText("SOHCAHTROA stuff")
        self.lesson_2.setText("")
