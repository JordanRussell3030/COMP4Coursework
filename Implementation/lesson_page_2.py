from PyQt4.QtCore import * #These two lines import all of the built in PyQt code
from PyQt4.QtCore import *

from lesson_page_2_parent_class import * #This contains the parent class which provides the default attributes
                                         #for all of these child classes

class SidesAHOWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.text_2_pic = QLabel()
        self.text_2_pic.setPixmap(QPixmap("sides_lesson_2_pic"))
        self.text_2_pic.setAlignment(Qt.AlignCenter)
        
        self.text_1.setText("There are four types of question where the SINE and COSINE rules would be applied.\n\n1. Two angles given plus any side - SINE rule needed\n\nB = A - C\n\nb {0} SIN B = c {0} SIN C\n\nWhich gives c = b x SIN C {0} SIN B = X\n\n2. Two sides given plus an angle not enclosed by them - SINE rule needed\n\nb {0} SIN B = c {0} SIN C\n\nSIN B = b x SIN C {0} c = X\n\n3. Two sides given plus the angle enclosed by them - COSINE rule needed\n\na\u00b2 = b\u00b2 + c\u00b2 - 2bcCOS A\n\n4. All three sides given but no angles - COSINE rule needed\n\nCOS A = b\u00b2 + c\u00b2 - a\u00b2 {0} 2bc".format(chr(247)))
        
        self.text_2.setText("Practice:\n\nFind the length of side c in the diagram below.\nUse example 1 to your left to help you find it.")

        self.answer_lesson = "8.05m"

        self.answer.setText("m")

        self.layout.addWidget(self.text_2_pic, 1, 1)

#These are the child classes which inherit from lesson_pge_2_parent_class
class SOHCAHTOAWidgetPage2(ParentLessonPage2):
    #Constructor
    def __init__(self, parent):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()
        
        #This is the parent variable which allows the child classes to inherit the connections to the second widget in the stacks       
        self.parent = parent

        self.answer.setText("m")

        #The widget variables are created in the parent class then the text is overridden in each child class
        self.text_1.setText("Example 1:\n1. Label O, A, H\n2. Write down SOHCAHTOA\n3. Two sides are involved: O,H\n4. So use O {0} S x H\n5. We want to find H so cover it up to leave H = (O {0} S(0))\n6. Translate: Press 15 {0} SIN(35) = 26.151702, so ans = 26.2m\n7. Check it's sensible: Yes, it's about twice as big as 15, as the diagram suggests.".format(chr(247)))
        #Sets the size of the text box
        self.text_1.setMinimumHeight(380)
        
        self.text_2.setText("You have to figure out yourself which formula to use to find this answer.\nHere's a hint: cut the triangle down the middle and it becomes a right-angled triangle.\n \n \n \n \n \n \nPut your answer in the box below:")      
        self.text_2.setMinimumHeight(380)

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("sohcahtoa_lesson_pic_2.png"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setPixmap(QPixmap("sohcahtoa_lesson_pic_3.png"))
        self.pic_2.setAlignment(Qt.AlignCenter)

        #Adds the widgets to the layout - the layout is assigned and set in the parent class
        self.layout.addWidget(self.pic, 2, 0)
        self.layout.addWidget(self.pic_2, 2, 1)

        #A hard-coded answer for the test question
        self.answer_lesson = "26.5m"

class FindingAnglesWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.text_1_pic = QLabel()
        self.text_1_pic.setPixmap(QPixmap("find_angles_example"))
        self.text_1_pic.setAlignment(Qt.AlignCenter)
                
        self.text_1.setText("Example:\n\nFind 6 different angles x such that sin x = 0.94\n\n\nMethod:\n\n1. Sketch the extended SIN graph\n2. Put a horizontal line across at 0.94\n3. Draw lines down to the x-axis wherever the horizontal croses the curve\n4. Use your calculator to find inv sin 0.94, to get the first angle (70\u00b0 in this case)\n5. The symmetry is surely obvious. You can see that 70\u00b0 is 20\u00b0 away from the peak, so all the other angles are clearly 20\u00b0 either side of the peaks at 90\u00b0, 450\u00b0, etc\n\nWe can say that sin x = +0.94 for all of the following angles:\n-290\u00b0, -250\u00b0, 70\u00b0, 110\u00b0, 430\u00b0, 470\u00b0, 790\u00b0, 830\u00b0")

        self.text_2.setText("Practice:\n\nFind one other angle which has the same cosine as 65\u00b0.\nUse the calculator to find COS 65\u00b0\n\nYou will need paper and a pen to sketch a COS graph similar to the one in the previous example.\n\n\nPlease input your answer in the box below: ")

        self.layout.addWidget(self.text_1_pic, 1, 0)

        self.answer.setText("\u00b0")
        
        self.answer_lesson = "-425\u00b0"
        self.answer_lesson_2 = "-295\u00b0"
        self.answer_lesson_3 = "-65\u00b0"

class ThreeDTrigonometryWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.text_1_pic = QLabel()
        self.text_1_pic.setPixmap(QPixmap("three_d_trig_lesson_2_pic_1"))
        self.text_1_pic.setAlignment(Qt.AlignCenter)

        self.text_2_pic = QLabel()
        self.text_2_pic.setPixmap(QPixmap("three_d_trig_lesson_2_pic_2"))
        self.text_2_pic.setAlignment(Qt.AlignCenter)
        
        self.text_1.setText("You can also use right angled triangles to find lengths.\n\nExample: Find the lengths FH and BH shown in the diagram.\n\n1.First, use Pythagoras to find the length FH.\n\nf\u00b2 = 3\u00b2 + 3\u00b2 = 18\nFH = \u221a18cm\n\n2. Now use Pythagoras again to find the length BH.\nBH\u00b2 = 3\u00b2 +(\u221a18)\u00b2 = 27\nBH = \u221a27cm = 5.2cm")
        
        self.text_2.setText("Practice:\n\nCalculate the length of AG in the cuboid below.\nInput your answer in the box to two decimal places.")

        self.layout.addWidget(self.text_1_pic, 1, 0)
        self.layout.addWidget(self.text_2_pic, 1, 1)

        self.answer_lesson = "7.07cm"

        self.answer.setText("cm")

class PythagTheoremWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        self.text_1_pic = QLabel()
        self.text_1_pic.setPixmap(QPixmap("three_d_pythag_lesson_1_pic_1"))
        self.text_1_pic.setAlignment(Qt.AlignCenter)

        self.text_2_pic = QLabel()
        self.text_2_pic.setPixmap(QPixmap("three_d_pythag_lesson_1_pic_2"))
        self.text_2_pic.setAlignment(Qt.AlignCenter)
        
        self.text_1.setText("As you may have seen in the 3D Trigonometry lesson, the rules of Trigonometry and Pythagoras can also be applied to 3-dimensional pyramid shapes.\n\nPythagoras' Theorem is useful for finding the lengths of triangles found within a 3D pyramid.\n\nLook at the square based pyramid below. You can see a red triangle highlighted within, representing the first stage of finding angles in a 3D pyramid.\n\nThe principle is hte same as 2D Pythagoras; you just have to pull a triangle out of the pyramid, find the length, and put it back in ready to use that length to get closer to finding the solution to an angle based question (see 3D Trigonometry).\n\nBC = 6cm, and AB = 9.2cm, so AC can by found using the following method:\n\n6\u00b2 = 36\n9.2\u00b2 = 85 (rounded)\n85 - 36 = 49\n\u221a49 = 7\n\nTherefore, AC must be 7.\n\nNow place the triangle back into the pyramid and use your new AC value to help find the next side or angle.")
        
        self.text_2.setText("Practice:\n\nLook at the square-based pyramid below.\nCalculate the length of AE to 1 decimal place.")

        self.layout.addWidget(self.text_1_pic, 1, 0)
        self.layout.addWidget(self.text_2_pic, 1, 1)

        self.answer_lesson = "13.9cm"

        self.answer.setText("cm")

class VectorWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("Vectors are often used in real life situations. Here is an example of a generic 'swimming across the river' question.\nyou just have to add the two velocity vectors end to end and draw the resultant vector which shows both the speed and direction of the final course.\n\nYou will need to use Pythagoras and Trigonometry to find the length and angle.\n\nExample:\n\nOverall speed = \u221a3\u00b2 + 2\u00b2 = 3.6m/s\nDirection = TAN X = 3 {0} 2\nX = TAN-1(1.5) = 56.3\u00b0.".format(chr(247)))
        
        self.text_2.setText("Practice:\n\nWork out the overall force in Newtons on the Queen Mary in the picture below:")

        self.text_2_pic = QLabel()
        self.text_2_pic.setPixmap(QPixmap("vectors_lesson_2_pic_2"))
        self.text_2_pic.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.text_2_pic, 1, 1)

        self.answer_lesson = "21800N"

        self.answer.setText("N")

class ReviseTrig1WidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More R1""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ReviseTrig2WidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More R2""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ReviseTrig3WidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More R3""")
        
        self.text_2.setText("Space for SOHCAHTOA """)
        
        self.answer_lesson = None
