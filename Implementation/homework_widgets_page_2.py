from PyQt4.QtCore import * #These two lines import all of the built in PyQt code
from PyQt4.QtGui import *

from homework_page_2_parent_class import * #This contains the parent class which provides all of the default attributes for these child classes
from database_class import * #This contains the method which saves the scores to the database

#These are the child classes which inherit all of their default attributes from homework_page_2_parent_class
class SidesAHOEasyWidget2(HomeworkPage2ParentClass):
    #Constructor
    def __init__(self, parent):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This is the parent variable which allows the child classes to inherit the connections to the second widget in the stacks       
        self.parent = parent

        #Overriding the taskname from the parent class so the user knows which task goes with the score
        self.task = "Sides Easy"

        #The widget variables are all created in the parent class because they are used in all of the child classes
        #and the text is set here so that it can be different
        self.question_2.setText("Question 2\nWhat is the length\nof b?")
        
##        self.shape_2.setText("sides easy")
        
        self.question_3.setText("Question 3\nWhat is the length\nof c?")
        
##        self.shape_3.setText("Shape")
        
        self.question_4.setText("Question 4\nWhat is the\nlength of a?")

        #Adds some wrong answers and the right answer to the combo box
        self.answer_q_2 = "15"
        self.answer_2.addItem("10")
        self.answer_2.addItem("20")
        self.answer_2.addItem("30")
        self.answer_2.addItem(self.answer_q_2)

        self.answer_q_3 = "7"
        self.answer_3.addItem("10")
        self.answer_3.addItem(self.answer_q_3)
        self.answer_3.addItem("20")
        self.answer_3.addItem("30")

        #Sets the text of the multiple choice buttons which is used to check the answer in the check methods
        self._button_1.setText("60")
        self._button_2.setText("50")
        self._button_3.setText("40")
        self._button_4.setText("30")
        self._button_5.setText("20")
        self._button_6.setText("10")

        #This is the hard-coded answer which is checked against with the text in the buttons above
        self.answer_question_4 = "40"

class SidesAHOMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent

        self.task = "Sides Medium"
        
        self.question_2.setText("Question 2\n_________\n_________")
        
        self.shape_2.setText("sides m")
        
        self.question_3.setText("Question 3\n_________\n_________")
        
        self.shape_3.setText("Shape")
        
        self.question_4.setText("Question 4\n______\n______\n______")

        self.answer_2.addItem("10")
        self.answer_2.addItem("20")
        self.answer_2.addItem("30")

        self.answer_3.addItem("10")
        self.answer_3.addItem("20")
        self.answer_3.addItem("30")

        self._button_1.setText("60")
        self._button_2.setText("50")
        self._button_3.setText("40")
        self._button_4.setText("30")
        self._button_5.setText("20")
        self._button_6.setText("10")

        self.answer_question_4 = "40"

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
