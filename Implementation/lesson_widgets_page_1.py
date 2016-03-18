from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

from lesson_layout_parent_class import * #This is the parent class for all of the first lesson pages, it provides all of the default attributes

#This is the child template for the first page of the Sides lesson
class SidesAHOWidget(ParentLessonLayout):
    #Constructor
    def __init__(self, parent):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This declares the parent variable so that it can be called to switch the screen in the stack
        self.parent = parent

        #The QLabel is declared in the parent class and the picture is set here so that it can be different across each child class
        self.title.setPixmap(QPixmap("sides_lesson_title"))

        #These TextEdits are declared in the parent class and the text is set here so that it can be different across each child class
        self.lesson_1.setText("Every triangle has 3 sides, and each side has a name.\nThe HYPOTENUSE is the longest side, and is always oppposite the right-angle of a triangle.\nThe length can be found using Pythagoras' Theorem of a\u00b2 + b\u00b2 = c\u00b2.\nSine function: sin(x) = Opposite {0} Hypotenuse".format(chr(247)))

        self.lesson_2.setText("The OPPOSITE is the side opposite the angle being used.\nCosine function: cos(x) = Adjacent {0} Hypotenuse".format(chr(247)))

    #The connection is in the parent class, because each setCurrentIndex(1) (each second screen in the stack) is declared in the lesson stack template which is already in use
    def selected_next_page(self):
        #Sets the stack to the next screen
        self.parent.stack.setCurrentIndex(1)
            
class SOHCAHTOAWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("sohcahtoa_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTOA stands for: \nSine Opposite Hypotenuse\nCosine Adjacent Hypotenuse\nTan Opposite Adjacent.\nThis is the best way to remember the three different rules for working out trigonometry problems.They each turn into a FORMULA TRIANGLE, a triangle which shows the formula inside in a memorable format.")

        self.lesson_2.setText("Method\n1. Label the three sides O, A and H\n2. Write down from memory SOHCAHTOA\n3. Decide which two sides are involved: O,H, A,H or O,A\n4. Turn the one you choose into one of the formula triangles to the left of the screen\n5. Cover up the thing you want to find and write down whatever is left showing\n6. Translate into numbers and work it out\n7. Finally, check that your answer is sensible")

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("formula_triangles.png"))

        self.layout.addWidget(self.pic, 2, 0)

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class FindingAnglesWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("finding_angles_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class ThreeDTrigonometryWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("three_d_trig_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class PythagTheoremWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("pythag_theorem_lesson_title"))

        self.lesson_1_pic = QLabel()
        self.lesson_1_pic.setPixmap(QPixmap("pythag_lesson_pic_1"))
        self.lesson_1_pic.setAlignment(Qt.AlignCenter)

        self.lesson_2_pic = QLabel()
        self.lesson_2_pic.setPixmap(QPixmap("pythag_lesson_pic_2"))
        self.lesson_2_pic.setAlignment(Qt.AlignCenter)
        
        self.lesson_1.setText("Pythagoras' Theorem is: a\u00b2 + b\u00b2 = c\u00b2\nPythagoras' Theorem always goes with SIN, COS and TAN because they are both involved with right angled triangles.\nHowever, Pythagoras does not ibvolve any angles - it just uses two sides to find the third side.\nGeneral trigonometry always involves angles.\nThe two shorter sides squared add to equal the longest side squared.\nIn trigonometry terms, the opposite squared plus the adjacent squared add up to make the hypotenuse squared.")
        
        self.lesson_2.setText("Example:\n\nFind the missing side in the triangle shown.\n\na\u00b2 + b\u00b2 = c\u00b2\n3\u00b2 + x\u00b2 = 5\u00b2\n9 + x\u00b2 = 25\nx\u00b2 = 25 - 9 = 16\nx = \u221a16 = 4m\nIs it sensible? Yes, it's just shorter than 5m and longer than 3m.")

        self.layout.addWidget(self.lesson_1_pic, 2, 0)
        self.layout.addWidget(self.lesson_2_pic, 2, 1)

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class ThreeDPythagorasWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("three_d_pythag_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class EasyWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("vectors_1_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class MediumWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("vectors_2_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class HardWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("vectors_3_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")
        
    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class ReviseTrig1Widget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("easy_summary_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class ReviseTrig2Widget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("medium_summary_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class ReviseTrig3Widget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("hard_summary_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTROA stuff")
        
        self.lesson_2.setText("")

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)
