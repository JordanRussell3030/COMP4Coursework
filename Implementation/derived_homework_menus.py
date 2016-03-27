from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

from homework_menu_parent_class import * #This contains the parent template for each of the 5 menus to take from
from homework_stacks import * #This has the templates for the stacks which are opened from each button which is clicked

#This is the template for the trigonometry 1 menu which takes most of its attributes from the ParentHomeworkMenuClass parent class
class Trigonometry1HW(ParentHomeworkMenuClass):
    ##constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This is an image - the words trigonometry 1 in large bold black text
        self.title.setPixmap(QPixmap("trig_1_title"))

        #These buttons have already been created in the parent class
        #The text is set here so that it can be different across each of the 5 child menus
        self.button_1.setText("Sides Easy")
        self.button_2.setText("Sides Medium")
        self.button_3.setText("Sides Hard")
        self.button_4.setText("SOHCAHTOA Easy")
        self.button_5.setText("SOHCAHTOA Medium")
        self.button_6.setText("SOHCAHTOA Hard")

        #The QLabels have already been created in the parent class
        #The pixmaps are set here so that they can be different across each of the 5 child classes
        self.pic_1.setPixmap(QPixmap("trig_1_pic_1_h"))
        self.pic_2.setPixmap(QPixmap("trig_1_pic_2_h"))
        self.pic_3.setPixmap(QPixmap("trig_1_pic_3_h"))
        self.pic_4.setPixmap(QPixmap("trig_1_pic_4_h"))
        self.pic_5.setPixmap(QPixmap("trig_1_pic_5_h"))
        self.pic_6.setPixmap(QPixmap("trig_1_pic_6_h"))

        #The layouts are set in the child classes so that nothing overlaps from the parent class
        self.layout.addWidget(self.button_1, 1, 0)
        self.layout.addWidget(self.pic_1, 1, 1)
        self.layout.addWidget(self.pic_2, 2, 0)
        self.layout.addWidget(self.button_2, 2, 1)
        self.layout.addWidget(self.button_3, 3, 0)
        self.layout.addWidget(self.pic_3, 3, 1)
        self.layout.addWidget(self.pic_4, 4, 0)
        self.layout.addWidget(self.button_4, 4, 1)
        self.layout.addWidget(self.button_5, 5, 0)
        self.layout.addWidget(self.pic_5, 5, 1)
        self.layout.addWidget(self.pic_6, 6, 0)
        self.layout.addWidget(self.button_6, 6, 1)

        #The connections are here because the stack widgets that each button needs to connect to are different in each child class
        self.button_1.clicked.connect(self.sides_aho_easy)
        self.button_2.clicked.connect(self.sides_aho_medium)
        self.button_3.clicked.connect(self.sides_aho_hard)
        self.button_4.clicked.connect(self.sohcahtoa_easy)
        self.button_5.clicked.connect(self.sohcahtoa_medium)
        self.button_6.clicked.connect(self.sohcahtoa_hard)

    #These are the methods which open the homework stack widgets when the corresponding button is clicked
    def sides_aho_easy(self):
        #Opens and displays the Sides Easy homework stack
        sides_aho_1 = Trig1StackSidesEasy()
        sides_aho_1.show()
        sides_aho_1._raise()

    def sides_aho_medium(self):
        sides_aho_2 = Trig1StackSidesMedium()
        sides_aho_2.show()
        sides_aho_2._raise()

    def sides_aho_hard(self):
        sides_aho_3 = Trig1StackSidesHard()
        sides_aho_3.show()
        sides_aho_3._raise()

    def sohcahtoa_easy(self):
        sohcahtoa_1 = Trig1StackSOHCAHTOAEasy()
        sohcahtoa_1.show()
        sohcahtoa_1._raise()

    def sohcahtoa_medium(self):
        sohcahtoa_2 = Trig1StackSOHCAHTOAMedium()
        sohcahtoa_2.show()
        sohcahtoa_2._raise()

    def sohcahtoa_hard(self):
        sohcahtoa_3 = Trig1StackSOHCAHTOAHard()
        sohcahtoa_3.show()
        sohcahtoa_3._raise()
        
#Everything is essentially the same as the above class except with different text on the buttons, different images and connections to different stack widgets
class Trigonometry2HW(ParentHomeworkMenuClass):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("trig_2_title"))

        self.button_1.setText("Finding Angles Easy")
        self.button_2.setText("Finding Angles Medium")
        self.button_3.setText("Finding Angles Hard")
        self.button_4.setText("3D Trigonometry Easy")
        self.button_5.setText("3D Trigonometry Medium")
        self.button_6.setText("3D Trigonometry Hard")

        self.pic_1.setPixmap(QPixmap("trig_2_pic_1_h"))
        self.pic_2.setPixmap(QPixmap("trig_2_pic_2_h"))
        self.pic_3.setPixmap(QPixmap("trig_2_pic_3_h"))
        self.pic_4.setPixmap(QPixmap("trig_2_pic_7_h"))
        self.pic_5.setPixmap(QPixmap("trig_2_pic_8_h"))
        self.pic_6.setPixmap(QPixmap("trig_2_pic_9_h"))

        self.layout.addWidget(self.button_1, 1, 0)
        self.layout.addWidget(self.pic_1, 1, 1)
        self.layout.addWidget(self.pic_2, 2, 0)
        self.layout.addWidget(self.button_2, 2, 1)
        self.layout.addWidget(self.button_3, 3, 0)
        self.layout.addWidget(self.pic_3, 3, 1)
        self.layout.addWidget(self.pic_4, 4, 0)
        self.layout.addWidget(self.button_4, 4, 1)
        self.layout.addWidget(self.button_5, 5, 0)
        self.layout.addWidget(self.pic_5, 5, 1)
        self.layout.addWidget(self.pic_6, 6, 0)
        self.layout.addWidget(self.button_6, 6, 1)

        self.button_1.clicked.connect(self.finding_angles_easy)
        self.button_2.clicked.connect(self.finding_angles_medium)
        self.button_3.clicked.connect(self.finding_angles_hard)
        self.button_4.clicked.connect(self.three_d_trig_easy)
        self.button_5.clicked.connect(self.three_d_trig_medium)
        self.button_6.clicked.connect(self.three_d_trig_hard)
    
    def finding_angles_easy(self):
        finding_angles_1 = Trig2StackFindingAnglesEasy()
        finding_angles_1.show()
        finding_angles_1._raise()

    def finding_angles_medium(self):
        finding_angles_2 = Trig2StackFindingAnglesMedium()
        finding_angles_2.show()
        finding_angles_2._raise()

    def finding_angles_hard(self):
        finding_angles_3 = Trig2StackFindingAnglesHard()
        finding_angles_3.show()
        finding_angles_3._raise()

    def three_d_trig_easy(self):
        three_d_trig_1 = Trig2StackTDTEasy()
        three_d_trig_1.show()
        three_d_trig_1._raise()

    def three_d_trig_medium(self):
        three_d_trig_2 = Trig2StackTDTMedium()
        three_d_trig_2.show()
        three_d_trig_2._raise()

    def three_d_trig_hard(self):
        three_d_trig_3 = Trig2StackTDTHard()
        three_d_trig_3.show()
        three_d_trig_3._raise()

class PythagorasHW(ParentHomeworkMenuClass):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("pythag_vector_label"))

        self.button_1.setText("Pythagoras' Theorem Easy")
        self.button_2.setText("Pythagoras' Theorem Medium")
        self.button_3.setText("Pythagoras' Theorem Hard")
        self.button_4.setText("Vectors Easy")
        self.button_5.setText("Vectors Medium")
        self.button_6.setText("Vectors Hard")

        self.pic_1.setPixmap(QPixmap("pythag_pic_1_h"))
        self.pic_2.setPixmap(QPixmap("pythag_pic_2_h"))
        self.pic_3.setPixmap(QPixmap("pythag_pic_3_h"))
        
        self.layout.addWidget(self.button_1, 1, 0)
        self.layout.addWidget(self.pic_1, 1, 1)
        self.layout.addWidget(self.pic_2, 2, 0)
        self.layout.addWidget(self.button_2, 2, 1)
        self.layout.addWidget(self.button_3, 3, 0)
        self.layout.addWidget(self.pic_3, 3, 1)
        self.layout.addWidget(self.button_4, 4, 1)
        self.layout.addWidget(self.button_5, 5, 0)
        self.layout.addWidget(self.button_6, 6, 1)

        self.button_1.clicked.connect(self.pythag_theorem_easy)
        self.button_2.clicked.connect(self.pythag_theorem_medium)
        self.button_3.clicked.connect(self.pythag_theorem_hard)
        self.button_4.clicked.connect(self.vectors_easy)
        self.button_5.clicked.connect(self.vectors_medium)
        self.button_6.clicked.connect(self.vectors_hard)
    
    def pythag_theorem_easy(self):
        pythag_theorem_1 = PythagStackTheoremEasy()
        pythag_theorem_1.show()
        pythag_theorem_1._raise()

    def pythag_theorem_medium(self):
        pythag_theorem_2 = PythagStackTheoremMediun()
        pythag_theorem_2.show()
        pythag_theorem_2._raise()

    def pythag_theorem_hard(self):
        pythag_theorem_3 = PythagStackTheoremHard()
        pythag_theorem_3.show()
        pythag_theorem_3._raise()

    def vectors_easy(self):
        three_d_pythag_1 = VectorsStackEasy()
        three_d_pythag_1.show()
        three_d_pythag_1._raise()

    def vectors_medium(self):
        three_d_pythag_2 = VectorsStackMedium()
        three_d_pythag_2.show()
        three_d_pythag_2._raise()

    def vectors_hard(self):
        three_d_pythag_3 = VectorsStackHard()
        three_d_pythag_3.show()
        three_d_pythag_3._raise()

class SummaryHW(ParentHomeworkMenuClass):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("summary_title"))

        self.button_1.setText("Easy Summary")
        self.button_2.setText("Medium Summary")
        self.button_3.setText("Hard Summary")

        self.layout.addWidget(self.button_1, 0, 1)
        self.layout.addWidget(self.button_2, 1, 0)
        self.layout.addWidget(self.button_3, 2, 1)

        self.button_1.clicked.connect(self.easy_summary)
        self.button_2.clicked.connect(self.medium_summary)
        self.button_3.clicked.connect(self.hard_summary)
          
    def easy_summary(self):
        summary_1 = ReviseTrigStackEasy()
        summary_1.show()
        summary_1._raise()

    def medium_summary(self):
        summary_2 = ReviseTrigStackMedium()
        summary_2.show()
        summary_2._raise()

    def hard_summary(self):
        summary_3 = ReviseTrigStackHard()
        summary_3.show()
        summary_3._raise()
