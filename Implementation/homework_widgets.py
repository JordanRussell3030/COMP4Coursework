from PyQt4.QtGui import * #These two lines import all of the built in PyQt code
from PyQt4.QtCore import *

from homework_parent_class import * #This contains the parent class which proides the default attributes for all of these child classes
from database_class import * #This contains the method which saves the task name and the first question score to the database
from error_messages import * #This contains the error message classes displayed when the user makes a mistake

#These are the child classes which inherit from the homework_parent_class
class SidesAHOEasyWidget(ParentHomeworkPage1Class):
    #Constructor
    def __init__(self, parent):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This is the parent variable which allows the child classes to inherit the connections to the second widget in the stacks       
        self.parent = parent

        #This overrides the task name in each child class and is saved to the database to identify the task that has been ocmpleted
        self.task = "Sides Easy"
        
        self.title.setText("Sides Easy")

        #The widget variables are all created in the parent class as they are used in each child class, then the
        #text is set in the child classes so that they can all be different
        self.question_1.setText("Question 1: Look at the diagram below\nand answer the following questions: ")
        
        self.q1a.setText("Which side is opposite angle A?")
    
        self.q1b.setText("Which side is the adjacent?")
                
        self.q1c.setText("Which side is the hypotenuse?")        

        self.q1d.setText("Which formula would you use to find AB?")

        self.q1e.setText("If BC is 7cm, and AC is 8cm, then what is the length of AB?")

        self.q1f.setText("If BC is 4cm, and AC is 6cm, then what is the length of AB?")
        
        self.question_1_shape.setPixmap(QPixmap("sides_easy_q1"))

        #These are the hard-coded answers to the questions which are checked in the check methods
        self.answer_1_a = "BC"
        self.answer_1_b = "AC"
        self.answer_1_c = "AB"
        self.answer_1_d = "cosine"
        self.answer_1_e = "10.6cm"
        self.answer_1_f = "7.2cm"

        self.answer_e.setText("cm")
        self.answer_f.setText("cm")

    #The connection for this is in the parent class as the code is the same; it knows which screen to switch to because the stack is
    #already instantiated by this point
    def open_page_2(self):
        #Switches to screen to in the stack widget
        self.parent.stack.setCurrentIndex(1)
       
class SidesAHOMediumWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent

        self.task = "Sides Medium"
        
        self.title.setText("Sides Medium")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = "7"
        self.answer_1_b = "8"
        self.answer_1_c = "9"
        self.answer_1_d = "10"
        self.answer_1_e = "11"
        self.answer_1_f = "12"

class SidesAHOHardWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Sides Hard")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class SOHCAHTOAEasyWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("SOHCAHTOA Easy")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class SOHCAHTOAMediumWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("SOHCAHTOA Medium")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class SOHCAHTOAHardWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("SOHCAHTOA Hard")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class FindingAnglesEasyWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Finding Angles Easy")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = "1"
        self.answer_1_b = "2"
        self.answer_1_c = "3"
        self.answer_1_d = "4"
        self.answer_1_e = "5"
        self.answer_1_f = "6"

class FindingAnglesMediumWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Finding Angles Medium")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class FindingAnglesHardWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Finding Angles Hard")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None
        
class ThreeDTrigEasyWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("3D Trigonometry Easy")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class ThreeDTrigMediumWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("3D Trigonometry Medium")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class ThreeDTrigHardWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("3D Trigonometry Hard")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class PythagTheoremEasyWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Pythagoras' Theorem Easy")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class PythagTheoremMediumWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Pythagoras' Theorem Medium")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class PythagTheoremHardWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Pythagoras' Theorem Hard")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class ThreeDPythagEasyWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("3D Pythagoras Easy")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class ThreeDPythagMediumWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("3D Trigonometry Medium")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class ThreeDPythagHardWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("3D Pythagoras Hard")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class VectorsEasyWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Easy Problems")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class VectorsMediumWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Medium Problems")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class VectorsHardWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Hard Problems")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class EasySummaryWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Easy Summary")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class MediumSummaryWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Medium Summary")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None

class HardSummaryWidget(ParentHomeworkPage1Class):
    def __init__(self, parent):
        super().__init__()
        
        self.parent = parent
        
        self.title.setText("Hard Summary")
        
        self.question_1.setText("Question 1:\n ___________\n__________")
        
        self.question_1_shape.setText("Shape")

        self.answer_1_a = None
        self.answer_1_b = None
        self.answer_1_c = None
        self.answer_1_d = None
        self.answer_1_e = None
        self.answer_1_f = None
