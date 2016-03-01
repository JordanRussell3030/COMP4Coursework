from PyQt4.QtCore import * #These two lines import all of the built in PyQt code
from PyQt4.QtCore import *

from lesson_page_2_parent_class import * #This contains the parent class which provides the default attributes
                                         #for all of these child classes

class SidesAHOWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("The ADJACENT is next to the angle being used.\nTangent function: tan(x) = Opposite {0} Adjacent".format(chr(247)))
        
        self.text_2.setText("Space for a practice question based on the lesson e.g what is the length of a")

        self.answer_lesson = None

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
        
        self.text_1.setText("More FA""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ThreeDTrigonometryWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More 3DT""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class PythagTheoremWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More PT""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ThreeDPythagorasWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More 3DP""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class EasyWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More Easy""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class MediumWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More Medium""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class HardWidgetPage2(ParentLessonPage2):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text_1.setText("More Hard""")
        
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

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
