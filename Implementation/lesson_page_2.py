from PyQt4.QtCore import *
from PyQt4.QtCore import *

from easy_trig_widget import *
from lesson_page_2_parent_class import *

class SidesAHOWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More sides, BANTER")
        self.text_2.setText("Space for a practice question based on the lesson e.g what is the length of a")

class SOHCAHTOAWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("Example 1:\n1. Label O, A, H\n2. Write down SOHCAHTOA\n3. Two sides are involved: O,H\n4. So use O/SXH\n5. We want to find H so cover it up to leave H = )/S)\n6. Translate: Press 15 / sine(35) = 26.151702 so ans = 26.2m\n7. Check it's sensible: yes, it's about twice as big as 15, as the diagram suggests") #picture
        self.text_2.setText("Example 2 like above but harder")

class FindingAnglesWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More FA""")
        self.text_2.setText("Space for SOHCAHTOA """)

class InvertedAnglesWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More IA""")
        self.text_2.setText("Space for SOHCAHTOA """)

class ThreeDTrigonometryWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More 3DT""")
        self.text_2.setText("Space for SOHCAHTOA """)

class PythagTheoremWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More PT""")
        self.text_2.setText("Space for SOHCAHTOA """)

class ThreeDPythagorasWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More 3DP""")
        self.text_2.setText("Space for SOHCAHTOA """)

class EasyWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More Easy""")
        self.text_2.setText("Space for SOHCAHTOA """)

class MediumWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More Medium""")
        self.text_2.setText("Space for SOHCAHTOA """)

class HardWidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More Hard""")
        self.text_2.setText("Space for SOHCAHTOA """)

class ReviseTrig1WidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More R1""")
        self.text_2.setText("Space for SOHCAHTOA """)

class ReviseTrig2WidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More R2""")
        self.text_2.setText("Space for SOHCAHTOA """)

class ReviseTrig3WidgetPage2(ParentLessonPage2):
    def __init__(self):
        super().__init__()
        self.text_1.setText("More R3""")
        self.text_2.setText("Space for SOHCAHTOA """)
