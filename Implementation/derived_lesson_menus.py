from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

from parent_lesson_menu import * #This imports the parent class from which the following 5 classes inherit all of their default attributes
from lesson_stacks import * #This imports the lesson stacks for the connections to open when the buttons are clicked

#This is the template for the trigonometry 1 lesson menu, most of which is defined in the parent class ParentLessonMenu
class Trigonometry1(ParentLessonMenu):
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        self.title.setPixmap(QPixmap("trig_1_title"))
        self.title.setAlignment(Qt.AlignCenter)

        #The buttons are created in the parent class
        #The text is set here so that they can be different in each of the 5 child classes
        self.button_1.setText("Sides")
        self.button_2.setText("SOHCAHTOA")

        #The QLabels are defined here because pictures aren't necessarily included in every child class
        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("trig_1_pic"))
        #Aligns the picture to the center of the area to which it is positioned
        self.pic.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setPixmap(QPixmap("trig_1_pic_2"))
        self.pic_2.setAlignment(Qt.AlignCenter)

        #The widgets are added to the layout here so that there are no overlaps from the parent class
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.button_2, 1, 1)
        self.layout.addWidget(self.button_1, 2, 0)
        self.layout.addWidget(self.pic_2, 2, 1)

        #The connections are added in the child class because each button connects to different stack widgets depending on which menu it is
        self.button_1.clicked.connect(self.SidesAHO)
        self.button_2.clicked.connect(self.SOHCAHTOA)

    #Each of these methods, called in the above connections, opens a different stack widget which is why they are declared in the child classes
    def SidesAHO(self):
        sides_aho = Trig1StackSides()
        sides_aho.show()
        sides_aho._raise()

    def SOHCAHTOA(self):
        sohcahtoa = Trig1StackSOHCAHTOA()
        sohcahtoa.show()
        sohcahtoa._raise()

#Essentially the same as the above class except with different images, button text and lesson stack connections
class Trigonometry2(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("trig_2_title"))
        self.title.setAlignment(Qt.AlignCenter)

        self.button_1.setText("Finding Angles")
        self.button_2.setText("3D Trigonometry")

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("trig_2_pic_1"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setPixmap(QPixmap("trig_2_pic_3"))
        self.pic_2.setAlignment(Qt.AlignCenter)    

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.button_1, 1, 1)
        self.layout.addWidget(self.button_2, 2, 0)
        self.layout.addWidget(self.pic_2, 2, 1)
        self.layout.addWidget(self.back, 3, 0)

        self.button_1.clicked.connect(self.FindingAngles)
        self.button_2.clicked.connect(self.ThreeDTrigonometry)
    
    def FindingAngles(self):
        finding_angles = Trig2StackFA()
        finding_angles.show()
        finding_angles._raise()

    def ThreeDTrigonometry(self):
        three_d_trig = Trig2StackTDT()
        three_d_trig.show()
        three_d_trig._raise()

class Pythagoras(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("pythag_vector_label"))
        self.title.setAlignment(Qt.AlignCenter)

        self.button_1.setText("Pythagoras' Theorem")
        self.button_2.setText("Vectors")

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("pythag_pic_1"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setPixmap(QPixmap("pythag_pic_2"))
        self.pic_2.setAlignment(Qt.AlignCenter)

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.button_1, 1, 1)
        self.layout.addWidget(self.button_2, 2, 0)
        self.layout.addWidget(self.pic_2, 2, 1)

        self.button_1.clicked.connect(self.PythagTheorem)
        self.button_2.clicked.connect(self.Vectors)
    
    def PythagTheorem(self):
        pythag_theorem = PythagStackTheorem()
        pythag_theorem.show()
        pythag_theorem._raise()

    def Vectors(self):
        vectors = VectorStack()
        vectors.show()
        vectors._raise()

class Summary(ParentLessonMenu):
    def __init__(self):
        super().__init__()

        self.title.setPixmap(QPixmap("summary_title"))
        self.title.setAlignment(Qt.AlignCenter)
        
        self.button_1.setText("Trigonometry")
        self.button_2.setText("Pythagoras")
        self.button_3.setText("Vectors")

        self.pic = QLabel()
        self.pic.setPixmap(QPixmap("summary_pic_1"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setPixmap(QPixmap("summary_pic_2"))
        self.pic_2.setAlignment(Qt.AlignCenter)

        self.pic_3 = QLabel()
        self.pic_3.setPixmap(QPixmap("summary_pic_3"))
        self.pic_3.setAlignment(Qt.AlignCenter)
        
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.pic, 1, 0)
        self.layout.addWidget(self.button_1, 1, 1)
        self.layout.addWidget(self.button_2, 2, 0)
        self.layout.addWidget(self.pic_2, 2, 1)
        self.layout.addWidget(self.pic_3, 3, 0)
        self.layout.addWidget(self.button_3, 3, 1)
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
