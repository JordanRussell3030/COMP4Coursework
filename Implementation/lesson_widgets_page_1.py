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
        self.lesson_1.setText("Every triangle has 3 sides, and each side has a name.\n\nThe HYPOTENUSE is the longest side, and is always opposite the right-angle of a triangle.\n\nThe length can be found using Pythagoras' Theorem of a\u00b2 + b\u00b2 = c\u00b2.\n\nSine function: sin(x) = Opposite {0} Hypotenuse\n\nb {0} SIN B = c {0} SIN C or a {0} SIN A = b {0} SIN B".format(chr(247)))

        self.lesson_2.setText("The OPPOSITE is the side opposite the angle being used.\n\nCosine function: cos(x) = Adjacent {0} Hypotenuse\n\na\u00b2 = b\u00b2 + c\u00b2 - 2bcCOS A\n\nOR\n\nCOS A = b\u00b2 + c\u00b2 - a\u00b2 {0} 2bc\n\nThe ADJACENT is next to the angle being used.\nTangent function: tan(x) = Opposite {0} Adjacent".format(chr(247)))

    #The connection is in the parent class, because each setCurrentIndex(1) (each second screen in the stack) is declared in the lesson stack template which is already in use
    def selected_next_page(self):
        #Sets the stack to the next screen
        self.parent.stack.setCurrentIndex(1)
            
class SOHCAHTOAWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("sohcahtoa_lesson_title"))
        
        self.lesson_1.setText("SOHCAHTOA stands for:\n\nSine Opposite Hypotenuse\nCosine Adjacent Hypotenuse\nTan Opposite Adjacent.\n\nThis is the best way to remember the three different rules for working out trigonometry problems.\n\nThey each turn into a FORMULA TRIANGLE, a triangle which shows the formula inside in a memorable format.")

        self.lesson_2.setText("Method\n\n1. Label the three sides O, A and H\n\n2. Write down from memory SOHCAHTOA\n\n3. Decide which two sides are involved: O,H, A,H or O,A\n\n4. Turn the one you choose into one of the formula triangles to the left of the screen\n\n5. Cover up the thing you want to find and write down whatever is left showing\n\n6. Translate into numbers and work it out\n\n7. Finally, check that your answer is sensible")

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

        self.lesson_1_pic = QLabel()
        self.lesson_2_pic = QLabel()

        self.lesson_1_pic.setPixmap(QPixmap("find_angles_lesson_1_pic"))
        self.lesson_1_pic.setAlignment(Qt.AlignCenter)

        self.lesson_2_pic.setPixmap(QPixmap("find_angles_text_1_pic"))
        self.lesson_2_pic.setAlignment(Qt.AlignCenter)
        
        self.lesson_1.setText("Each of the three trigonometry rules has a graph representing its cycle.\n\nFor 0\u00b0 - 360\u00b0, you get a SINE WAVE, which has one peak and one trough, and a COS BUCKET, which starts at the top, dips, and finishes at the top.\n\nThe underlying shape of both the SIN and COS graphs are identical when you extend them in both directions. The only difference between the two is that the SIN graph is shifted by 90\u00b0 right compared to the COS graph.\n\nBoth graphs wiggle between y limits of exactly +1 and -1.\n\nThe key to drawing the extended graphs is to draw the 0 - 360\u00b0 cycle of either the SIN WAVE or the COS BUCKET and then repeat it in both directions as shown.")
        
        self.lesson_2.setText("The TAN graph bears no resemblance to the SIN WAVE or COS BUCKET.\n\nEvery 180\u00b0, starting at 90\u00b0, the line disappears up into + infinity and then reappears at - infinity on the y line (asymptote).\nTherefore, the TAN wave is not limited to y values between +1 and -1.\n\nWhilst the SIN and COS graphs repeat every 360\u00b0, the TAN graph repeats every 180\u00b0.")

        self.layout.addWidget(self.lesson_1_pic, 2, 0)
        self.layout.addWidget(self.lesson_2_pic, 2, 1)

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class ThreeDTrigonometryWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.lesson_1_pic = QLabel()
        self.lesson_1_pic.setPixmap(QPixmap("three_d_trig_lesson_1_pic"))
        self.lesson_1_pic.setAlignment(Qt.AlignCenter)

        self.lesson_2_pic = QLabel()
        self.lesson_2_pic.setPixmap(QPixmap("three_d_trig_lesson_2_pic"))
        self.lesson_2_pic.setAlignment(Qt.AlignCenter)
        
        self.title.setPixmap(QPixmap("three_d_trig_lesson_title"))
        
        self.lesson_1.setText("When you are presented with a 3D pyramid, make a right angled triangle using the line, a line in the plane and a line between the two.\n\nDraw this right angled triangle again so that you can see it clearly. Label the sides. You might have to use Pythagoras to work out the length of one of the sides.\n\nUse trigonometry to calculate the angle.")
        
        self.lesson_2.setText("Example: ABCDE is a square based pyramid. It is 12cm high and the square base has sides of length 7cm. Find the angle the edge AE makes with the base.\n\n1. First draw a right-angled triangle using the edge AE, the base and a line between the two (in this case the central height). Call the angle you're trying to find X.\n\n2. Now draw this triangle clearly and label it.\nTo find X, you need to know the length of side EZ. So, using Pythagoras - EZ\u00b2 = 3.5\u00b2 + 3.5\u00b2 = 24.5 - EZ = \u221a24.5cm\n\n3. Now use trigonometry to find the angle X: tan X = 12 {0}\u221a24.5 = 2.4\n\nX = 67.6\u00b0".format(chr(247)))

        self.layout.addWidget(self.lesson_1_pic, 2, 0)
        self.layout.addWidget(self.lesson_2_pic, 2, 1)
        
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
        
        self.lesson_1.setText("Pythagoras' Theorem is: a\u00b2 + b\u00b2 = c\u00b2\nPythagoras' Theorem always goes with SIN, COS and TAN because they are both involved with right angled triangles.\n\nHowever, Pythagoras does not involve any angles - it just uses two sides to find the third side.\n\nGeneral trigonometry always involves angles.\n\nThe two shorter sides squared add to equal the longest side squared.\n\nIn trigonometry terms, the opposite squared plus the adjacent squared add up to make the hypotenuse squared.")
        
        self.lesson_2.setText("Example:\n\nFind the missing side in the triangle shown.\n\na\u00b2 + b\u00b2 = c\u00b2\n3\u00b2 + x\u00b2 = 5\u00b2\n9 + x\u00b2 = 25\nx\u00b2 = 25 - 9 = 16\nx = \u221a16 = 4m\nIs it sensible? Yes, it's just shorter than 5m and longer than 3m.")

        self.layout.addWidget(self.lesson_1_pic, 2, 0)
        self.layout.addWidget(self.lesson_2_pic, 2, 1)

    def selected_next_page(self):
        self.parent.stack.setCurrentIndex(1)

class EasyWidget(ParentLessonLayout):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.title.setPixmap(QPixmap("vectors_1_lesson_title"))

        self.lesson_1_pic = QLabel()
        self.lesson_1_pic.setPixmap(QPixmap("vectors_lesson_1_pic"))
        self.lesson_1_pic.setAlignment(Qt.AlignCenter)

        self.lesson_2_pic = QLabel()
        self.lesson_2_pic.setPixmap(QPixmap("vectors_lesson_2_pic"))
        self.lesson_2_pic.setAlignment(Qt.AlignCenter)
        
        self.lesson_1.setText("There are three things to know about vectors:\n\n1. The four notations\n\nThe vector image below can be referred to as a with a ~ underneath or just a in bold.\n\nMake sure you know which is which in the column vector and what a negative value means in a column vector.\n\n\n2. Adding and subtracting values:\n\nVectors must always be added end to end, so that the arrows all point with each other, not against each other.\n\nIf a = 5 over 3 and b = -2 over 4, then 2a - b = 2(5 over 3) - -2 over 4 = 12 over 2.")
        
        self.lesson_2.setText("This is a very common type of question and it illustrates a very important vector technique:\n\nTo obtain the unknown vector just get there by any route made up of known vectors.\n\nApplying this rule we can eaasily obtain the following:\n\nvectors in term of a~, b~ and m~ (given that M and N are mid-points):\n\n1. AM = -a~ + b~ + m~ (via O and B)\nOC = b~ + 2m (via B and M)\nAC = -a~ + b~ + 2m~ (A to C via O, B and M)")

        self.layout.addWidget(self.lesson_1_pic, 2, 0)
        self.layout.addWidget(self.lesson_2_pic, 2, 1)

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
