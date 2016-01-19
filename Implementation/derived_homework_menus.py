from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
#
from lesson_menu_widget import *
from homework_menu_widget import *
##from parent_class_homework import *
from easy_trig_widget import *
from homework_widgets import *
from homework_menu_parent_class import *
from homework_widgets_page_2 import *

class Trigonometry1HW(ParentHomeworkMenuClass):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("trig_1_title"))

        self.button_1.setText("Sides Easy")
        self.button_2.setText("Sides Medium")
        self.button_3.setText("Sides Hard")
        self.button_4.setText("SOHCAHTOA Easy")
        self.button_5.setText("SOHCAHTOA Medium")
        self.button_6.setText("SOHCAHTOA Hard")

        self.pic_1.setPixmap(QPixmap("trig_1_pic_1_h"))
        self.pic_2.setPixmap(QPixmap("trig_1_pic_2_h"))
        self.pic_3.setPixmap(QPixmap("trig_1_pic_3_h"))
        self.pic_4.setPixmap(QPixmap("trig_1_pic_4_h"))
        self.pic_5.setPixmap(QPixmap("trig_1_pic_5_h"))
        self.pic_6.setPixmap(QPixmap("trig_1_pic_6_h"))

        self.layout.addWidget(self.button_1, 1, 0)
        self.layout.addWidget(self.button_2, 2, 1)
        self.layout.addWidget(self.button_3, 3, 0)
        self.layout.addWidget(self.button_4, 4, 1)
        self.layout.addWidget(self.button_5, 5, 0)
        self.layout.addWidget(self.button_6, 6, 1)
        self.layout.addWidget(self.pic_1, 1, 1)
        self.layout.addWidget(self.pic_2, 2, 0)
        self.layout.addWidget(self.pic_3, 3, 1)
        self.layout.addWidget(self.pic_4, 4, 0)
        self.layout.addWidget(self.pic_5, 5, 1)
        self.layout.addWidget(self.pic_6, 6, 0)
     
        self.button_1.clicked.connect(self.sides_aho_easy)
        self.button_2.clicked.connect(self.sides_aho_medium)
        self.button_3.clicked.connect(self.sides_aho_hard)
        self.button_4.clicked.connect(self.sohcahtoa_easy)
        self.button_5.clicked.connect(self.sohcahtoa_medium)
        self.button_6.clicked.connect(self.sohcahtoa_hard)

    #compress into 1 method
    def sides_aho_easy(self):
        sides_aho_1 = SidesAHOEasyWidget()
        sides_aho_1.show()
        sides_aho_1._raise()

    def sides_aho_medium(self):
        sides_aho_2 = SidesAHOMediumWidget()
        sides_aho_2.show()
        sides_aho_2._raise()

    def sides_aho_hard(self):
        sides_aho_3 = SidesAHOHardWidget()
        sides_aho_3.show()
        sides_aho_3._raise()

    def sohcahtoa_easy(self):
        sohcahtoa_1 = SOHCAHTOAEasyWidget()
        sohcahtoa_1.show()
        sohcahtoa_1._raise()

    def sohcahtoa_medium(self):
        sohcahtoa_2 = SOHCAHTOAMediumWidget()
        sohcahtoa_2.show()
        sohcahtoa_2._raise()

    def sohcahtoa_hard(self):
        sohcahtoa_3 = SOHCAHTOAHardWidget()
        sohcahtoa_3.show()
        sohcahtoa_3._raise()

class Trigonometry2HW(ParentHomeworkMenuClass):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("trig_2_title"))

        self.button_1.setText("Finding Angles Easy")
        self.button_2.setText("Finding Angles Medium")
        self.button_3.setText("Finding Angles Hard")
##        self.button_4.setText("Inverted Angles Easy")
##        self.button_5.setText("Inverted Angles Medium")
##        self.button_6.setText("Inverted Angles Hard")
        self.button_4.setText("3D Trigonometry Easy")
        self.button_5.setText("3D Trigonometry Medium")
        self.button_6.setText("3D Trigonometry Hard")

        self.pic_1.setPixmap(QPixmap("trig_2_pic_1_h"))
        self.pic_2.setPixmap(QPixmap("trig_2_pic_2_h"))
        self.pic_3.setPixmap(QPixmap("trig_2_pic_3_h"))
##        self.pic_4.setPixmap(QPixmap("trig_2_pic_4_h"))
##        self.pic_5.setPixmap(QPixmap("trig_2_pic_5_h"))
##        self.pic_6.setPixmap(QPixmap("trig_2_pic_6_h"))
        self.pic_4.setPixmap(QPixmap("trig_2_pic_7_h"))
        self.pic_5.setPixmap(QPixmap("trig_2_pic_8_h"))
        self.pic_6.setPixmap(QPixmap("trig_2_pic_9_h"))

        self.layout.addWidget(self.button_1, 1, 0)
        self.layout.addWidget(self.button_2, 2, 1)
        self.layout.addWidget(self.button_3, 3, 0)
##        self.layout.addWidget(self.button_4, 4, 0)
##        self.layout.addWidget(self.button_5, 5, 1)
##        self.layout.addWidget(self.button_6, 6, 0)
        self.layout.addWidget(self.button_4, 4, 1)
        self.layout.addWidget(self.button_5, 5, 0)
        self.layout.addWidget(self.button_6, 6, 1)
        self.layout.addWidget(self.pic_1, 1, 1)
        self.layout.addWidget(self.pic_2, 2, 0)
        self.layout.addWidget(self.pic_3, 3, 1)
##        self.layout.addWidget(self.pic_4, 4, 1)
##        self.layout.addWidget(self.pic_5, 5, 0)
##        self.layout.addWidget(self.pic_6, 6, 1)
        self.layout.addWidget(self.pic_4, 4, 0)
        self.layout.addWidget(self.pic_5, 5, 1)
        self.layout.addWidget(self.pic_6, 6, 0)

        self.button_1.clicked.connect(self.finding_angles_easy)
        self.button_2.clicked.connect(self.finding_angles_medium)
        self.button_3.clicked.connect(self.finding_angles_hard)
        self.button_4.clicked.connect(self.three_d_trig_easy)
        self.button_5.clicked.connect(self.three_d_trig_medium)
        self.button_6.clicked.connect(self.three_d_trig_hard)
    
    def finding_angles_easy(self):
        finding_angles_1 = FindingAnglesEasyWidget()
        finding_angles_1.show()
        finding_angles_1._raise()

    def finding_angles_medium(self):
        finding_angles_2 = FindingAnglesMediumWidget()
        finding_angles_2.show()
        finding_angles_2._raise()

    def finding_angles_hard(self):
        finding_angles_3 = FindingAnglesHardWidget()
        finding_angles_3.show()
        finding_angles_3._raise()

##    def inverted_angles_easy(self):
##        inverted_angles_1 = InvertedAnglesEasyWidget()
##        inverted_angles_1.show()
##        inverted_angles_1._raise()
##
##    def inverted_angles_medium(self):
##        inverted_angles_2 = InvertedAnglesMediumWidget()
##        inverted_angles_2.show()
##        inverted_angles_2._raise()
##
##    def inverted_angles_hard(self):
##        inverted_angles_3 = InvertedAnglesHardWidget()
##        inverted_angles_3.show()
##        inverted_angles_3._raise()

    def three_d_trig_easy(self):
        three_d_trig_1 = ThreeDTrigEasyWidget()
        three_d_trig_1.show()
        three_d_trig_1._raise()

    def three_d_trig_medium(self):
        three_d_trig_2 = ThreeDTrigMediumWidget()
        three_d_trig_2.show()
        three_d_trig_2._raise()

    def three_d_trig_hard(self):
        three_d_trig_3 = ThreeDTrigHardWidget()
        three_d_trig_3.show()
        three_d_trig_3._raise()

class PythagorasHW(ParentHomeworkMenuClass):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("pythag_title"))

        self.button_1.setText("Pythagoras' Theorem Easy")
        self.button_2.setText("Pythagoras' Theorem Medium")
        self.button_3.setText("Pythagoras' Theorem Hard")
        self.button_4.setText("3D Pythagoras Easy")
        self.button_5.setText("3D Pythagoras Medium")
        self.button_6.setText("3D Pythagoras Hard")

        self.pic_1.setPixmap(QPixmap("pythag_pic_1_h"))
        self.pic_2.setPixmap(QPixmap("pythag_pic_2_h"))
        self.pic_3.setPixmap(QPixmap("pythag_pic_3_h"))
        
        self.layout.addWidget(self.button_1, 1, 0)
        self.layout.addWidget(self.button_2, 2, 1)
        self.layout.addWidget(self.button_3, 3, 0)
        self.layout.addWidget(self.button_4, 4, 1)
        self.layout.addWidget(self.button_5, 5, 0)
        self.layout.addWidget(self.button_6, 6, 1)
        self.layout.addWidget(self.pic_1, 1, 1)
        self.layout.addWidget(self.pic_2, 2, 0)
        self.layout.addWidget(self.pic_3, 3, 1)

        self.button_1.clicked.connect(self.pythag_theorem_easy)
        self.button_2.clicked.connect(self.pythag_theorem_medium)
        self.button_3.clicked.connect(self.pythag_theorem_hard)
        self.button_4.clicked.connect(self.three_d_pythag_easy)
        self.button_5.clicked.connect(self.three_d_pythag_medium)
        self.button_6.clicked.connect(self.three_d_pythag_hard)
    
    def pythag_theorem_easy(self):
        pythag_theorem_1 = PythagTheoremEasyWidget()
        pythag_theorem_1.show()
        pythag_theorem_1._raise()

    def pythag_theorem_medium(self):
        pythag_theorem_2 = PythagTheoremMediumWidget()
        pythag_theorem_2.show()
        pythag_theorem_2._raise()

    def pythag_theorem_hard(self):
        pythag_theorem_3 = PythagTheoremHardWidget()
        pythag_theorem_3.show()
        pythag_theorem_3._raise()

    def three_d_pythag_easy(self):
        three_d_pythag_1 = ThreeDPythagEasyWidget()
        three_d_pythag_1.show()
        three_d_pythag_1._raise()

    def three_d_pythag_medium(self):
        three_d_pythag_2 = ThreeDPythagMediumWidget()
        three_d_pythag_2.show()
        three_d_pythag_2._raise()

    def three_d_pythag_hard(self):
        three_d_pythag_3 = ThreeDPythagHardWidget()
        three_d_pythag_3.show()
        three_d_pythag_3._raise()

class PythagTrigonometryHW(ParentHomeworkMenuClass):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("vectors_title"))

        self.button_1.setText("Vectors Easy")
        self.button_2.setText("Vectors Medium")
        self.button_3.setText("Vectors Hard")

        self.layout.addWidget(self.button_1, 0, 1)
        self.layout.addWidget(self.button_2, 1, 0)
        self.layout.addWidget(self.button_3, 2, 1)

        self.button_1.clicked.connect(self.pythag_trig_problems_easy)
        self.button_2.clicked.connect(self.pythag_trig_problems_medium)
        self.button_3.clicked.connect(self.pythag_trig_problems_hard)
        
    def pythag_trig_problems_easy(self):
        pythag_trig_problems_1 = PythagTrigProblemsEasyWidget()
        pythag_trig_problems_1.show()
        pythag_trig_problems_1._raise()

    def pythag_trig_problems_medium(self):
        pythag_trig_problems_2 = PythagTrigProblemsMediumWidget()
        pythag_trig_problems_2.show()
        pythag_trig_problems_2._raise()

    def pythag_trig_problems_hard(self):
        pythag_trig_problems_3 = PythagTrigProblemsHardWidget()
        pythag_trig_problems_3.show()
        pythag_trig_problems_3._raise()

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
        summary_1 = EasySummaryWidget()
        summary_1.show()
        summary_1._raise()

    def medium_summary(self):
        summary_2 = MediumSummaryWidget()
        summary_2.show()
        summary_2._raise()

    def hard_summary(self):
        summary_3 = HardSummaryWidget()
        summary_3.show()
        summary_3._raise()
