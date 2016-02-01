from PyQt4.QtCore import *
from PyQt4.QtGui import *

from homework_widgets import *
from homework_page_2_parent_class import *
from homework_stacks import *

class SidesAHOEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("sides easy")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

        self.answer_2.addItem("10")
        self.answer_2.addItem("20")
        self.answer_2.addItem("30")

        self.answer_3.addItem("10")
        self.answer_3.addItem("20")
        self.answer_3.addItem("30")

class SidesAHOMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("sides m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class SidesAHOHardWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("sides hard")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class SOHCAHTOAEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("soh e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class SOHCAHTOAMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("soh m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class SOHCAHTOAHardWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("soh h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class FindingAnglesEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("fa e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class FindingAnglesMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("fa m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class FindingAnglesHardWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("fa h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDTrigEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dt e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDTrigMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dt m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDTrigHardWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dt h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTheoremEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("pt e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTheoremMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("pt m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTheoremHardWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("pt h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDPythagorasEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dp e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDPythagorasMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dp m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDPythagorasHardWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dp h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class VectorsEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ptp e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class VectorsMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ptp m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class VectorsHardWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ptp h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class EasySummaryWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("s e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class MediumSummaryWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("s m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class HardSummaryWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("s h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")
