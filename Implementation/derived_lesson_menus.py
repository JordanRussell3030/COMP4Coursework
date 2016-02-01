from PyQt4.QtGui import *
from PyQt4.QtCore import *

from login_screen_window import *
from login_widget import *
from lesson_menu_widget import *
from homework_menu_widget import *
from easy_trig_widget import *
from parent_lesson_menu import *
from lesson_stacks import *

class Trigonometry1(ParentLessonMenu):
    def __init__(self):
        super().__init__()
        self.title.setPixmap(QPixmap("trig_1_title"))

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("trig_1_pic"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setPixmap(QPixmap("trig_1_pic_2"))
        self.pic_2.setAlignment(Qt.AlignCenter)

        self.button_1.setText("Sides")
        self.button_2.setText("SOHCAHTOA")
        
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 2, 0)
        self.layout.addWidget(self.button_2, 1, 1)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.pic_2, 2, 1)

        self.button_1.clicked.connect(self.SidesAHO)
        self.button_2.clicked.connect(self.SOHCAHTOA)
    
    def SidesAHO(self):
        sides_aho = Trig1StackSides()
        sides_aho.show()
        sides_aho._raise()

    def SOHCAHTOA(self):
        sohcahtoa = Trig1StackSOHCAHTOA()
        sohcahtoa.show()
        sohcahtoa._raise()

class Trigonometry2(ParentLessonMenu):
    def __init__(self):
        super().__init__()
        
        self.title.setPixmap(QPixmap("trig_2_title"))

        self.pic = QLabel()
        self.pic_2 = QLabel()
        self.pic_3 = QLabel()

        self.pic.setPixmap(QPixmap("trig_2_pic_1"))
        self.pic_2.setPixmap(QPixmap("trig_2_pic_3"))

        self.pic.setAlignment(Qt.AlignCenter)
        self.pic_2.setAlignment(Qt.AlignCenter)

        self.button_1.setText("Finding Angles")
        self.button_2.setText("3D Trigonometry")

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 1, 1)
        self.layout.addWidget(self.button_2, 2, 0)
        self.layout.addWidget(self.back, 4, 0)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.pic_2, 2, 1)
        self.layout.addWidget(self.pic_3, 3, 0)

        self.button_1.clicked.connect(self.FindingAngles)
        self.button_2.clicked.connect(self.ThreeDTrigonometry)
    
    def FindingAngles(self):
        finding_angles = Trig2StackFA()
        finding_angles.show()
        finding_angles._raise()

##    def InvertedAngles(self):
##        inverted_angles = InvertedAnglesWidget()
##        inverted_angles.show()
##        inverted_angles._raise()

    def ThreeDTrigonometry(self):
        three_d_trig = Trig2StackTDT()
        three_d_trig.show()
        three_d_trig._raise()

class Pythagoras(ParentLessonMenu):
    def __init__(self):
        super().__init__()
        
        self.title.setPixmap(QPixmap("pythag_title"))

        self.pic = QLabel()
        self.pic_2 = QLabel()

        self.pic.setPixmap(QPixmap("pythag_pic_1"))
        self.pic_2.setPixmap(QPixmap("pythag_pic_2"))

        self.pic.setAlignment(Qt.AlignCenter)
        self.pic_2.setAlignment(Qt.AlignCenter)
        
        self.button_1.setText("Pythagoras' Theorem")
        self.button_2.setText("3D Pythagoras")

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 1, 1)
        self.layout.addWidget(self.button_2, 2, 0)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.pic_2, 2, 1)

        self.button_1.clicked.connect(self.PythagTheorem)
        self.button_2.clicked.connect(self.ThreeDPythagoras)
    
    def PythagTheorem(self):
        pythag_theorem = PythagStackTheorem()
        pythag_theorem.show()
        pythag_theorem._raise()

    def ThreeDPythagoras(self):
        three_d_pythag = PythagStackTDP()
        three_d_pythag.show()
        three_d_pythag._raise()

class PythagTrig(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("vectors_title"))

        self.button_1.setText("Vectors 1")
        self.button_2.setText("Vectors 2")
        self.button_3.setText("Vectors 3")

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("vectors_pic_1"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setPixmap(QPixmap("vectors_pic_2"))
        self.pic_2.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 1, 1)
        self.layout.addWidget(self.button_2, 2, 0)
        self.layout.addWidget(self.button_3, 3, 1)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.pic_2, 2, 1)
        self.layout.addWidget(self.back, 4, 0)

        self.button_1.clicked.connect(self.Easy)
        self.button_2.clicked.connect(self.Medium)
        self.button_3.clicked.connect(self.Hard)
    
    def Easy(self):
        easy = EasyStack()
        easy.show()
        easy._raise()

    def Medium(self):
        medium = MediumStack()
        medium.show()
        medium._raise()

    def Hard(self):
        hard = HardStack()
        hard.show()
        hard._raise()

class Summary(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("summary_title"))

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("summary_pic_1"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setPixmap(QPixmap("summary_pic_2"))
        self.pic_2.setAlignment(Qt.AlignCenter)

        self.pic_3 = QLabel()
        self.pic_3.setPixmap(QPixmap("summary_pic_3"))
        self.pic_3.setAlignment(Qt.AlignCenter)

        self.button_1.setText("Easy")
        self.button_2.setText("Medium")
        self.button_3.setText("Hard")
        
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.button_1, 1, 1)
        self.layout.addWidget(self.button_2, 2, 0)
        self.layout.addWidget(self.button_3, 3, 1)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.pic_2, 2, 1)
        self.layout.addWidget(self.pic_3, 3, 0)
        self.layout.addWidget(self.back, 4, 0)

        self.button_1.clicked.connect(self.ReviseTrig1)
        self.button_2.clicked.connect(self.ReviseTrig2)
        self.button_3.clicked.connect(self.ReviseTrig3)
    
    def ReviseTrig1(self):
        revise_trig_1 = Revise1Stack()
        revise_trig_1.show()
        revise_trig_1._raise()

    def ReviseTrig2(self):
        revise_trig_2 = Revise2Stack()
        revise_trig_2.show()
        revise_trig_2._raise()

    def ReviseTrig3(self):
        revise_trig_3 = Revise3Stack()
        revise_trig_3.show()
        revise_trig_3._raise()
