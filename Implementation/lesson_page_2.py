from PyQt4.QtCore import *
from PyQt4.QtCore import *
#
from easy_trig_widget import *
from lesson_page_2_parent_class import *

class SidesAHOWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More sides, BANTER")
        self.text_2.setText("Space for a practice question based on the lesson e.g what is the length of a")

        self.answer_lesson = None

class SOHCAHTOAWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("Example 1:\n1. Label O, A, H\n2. Write down SOHCAHTOA\n3. Two sides are involved: O,A\n4. So use O {0} T x A\n5. We want to find O so cover it up to leave O = (T {0} A)\n6. Translate: Press 14 {0} tan(67) = 26.151702 so ans = 26.2m\n7. Check it's sensible: Yes, it's about twice as big as 14, as the diagram suggests.".format(chr(247))) #picture
        self.text_2.setText("Example 2 like above but harder")

        self.text_1.setMinimumHeight(380)

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("sohcahtoa_page_2_lesson_triangle.png"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.pic, 2, 0)

        self.answer_lesson = None

class FindingAnglesWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More FA""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class InvertedAnglesWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More IA""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ThreeDTrigonometryWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More 3DT""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class PythagTheoremWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More PT""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ThreeDPythagorasWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More 3DP""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class EasyWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More Easy""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class MediumWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More Medium""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class HardWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More Hard""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ReviseTrig1WidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More R1""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ReviseTrig2WidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More R2""")
        self.text_2.setText("Space for SOHCAHTOA """)

        self.answer_lesson = None

class ReviseTrig3WidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More R3""")
        self.text_2.setText("Space for SOHCAHTOA """)
        
        self.answer_lesson = None
