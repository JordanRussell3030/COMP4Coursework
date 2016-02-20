from PyQt4.QtCore import * #These two lines import the built in PyQt code
from PyQt4.QtGui import *

from homework_widgets import * #Contains the first widgets to add to each stack
from homework_widgets_page_2 import * #Contains the second widgets to add to each stack

class Trig1StackSidesEasy(QMainWindow):
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #Maximises the stack widget for both windows contained in it
        self.showMaximized()

        #Assigns the first sides easy widget from the homework_widgets file for the stack layout
        self.first_widget = SidesAHOEasyWidget(self)
        #Assigns the second sides easy widget from the homework_widgets_page_2 file for the stack layout
        self.second_widget = SidesAHOEasyWidget2(self)
        #All of the first widgets and second widgets share files so that only 1 import is necessary for each, and they share a lot of code
        #Furthermore the code is'nt too long

        #Sets the layout to a stack layout to allow for the addition of a page 1 and 2 to a single window to switch between them
        self.stack = QStackedLayout()

        #Adds the two widgets to the stack
        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        #Sets the layout to be used as a QWidget and adds the stack to it
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        #Sets the layout to be used as the central widget so that it appears
        self.setCentralWidget(self.widget)

class Trig1StackSidesMedium(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = SidesAHOMediumWidget(self)
        self.second_widget = SidesAHOMediumWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)
        
class Trig1StackSidesHard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = SidesAHOHardWidget(self)
        self.second_widget = SidesAHOHardWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig1StackSOHCAHTOAEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = SOHCAHTOAEasyWidget(self)
        self.second_widget = SOHCAHTOAEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig1StackSOHCAHTOAMedium(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = SOHCAHTOAMediumWidget(self)
        self.second_widget = SOHCAHTOAMediumWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig1StackSOHCAHTOAHard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = SOHCAHTOAHardWidget(self)
        self.second_widget = SOHCAHTOAHardWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig2StackFindingAnglesEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = FindingAnglesEasyWidget(self)
        self.second_widget = FindingAnglesEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig2StackFindingAnglesMedium(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = FindingAnglesMediumWidget(self)
        self.second_widget = FindingAnglesMediumWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig2StackFindingAnglesHard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = FindingAnglesHardWidget(self)
        self.second_widget = FindingAnglesHardWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig2StackTDTEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = ThreeDTrigEasyWidget(self)
        self.second_widget = ThreeDTrigEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig2StackTDTMedium(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = ThreeDTrigMediumWidget(self)
        self.second_widget = ThreeDTrigMediumWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig2StackTDTHard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = ThreeDTrigHardWidget(self)
        self.second_widget = ThreeDTrigHardWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class PythagStackTheoremEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = PythagTheoremEasyWidget(self)
        self.second_widget = PythagTheoremEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class PythagStackTheoremMediun(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = PythagTheoremMediumWidget(self)
        self.second_widget = PythagTheoremMediumWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class PythagStackTheoremHard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = PythagTheoremHardWidget(self)
        self.second_widget = PythagTheoremHardWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class PythagStackTDPEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = ThreeDPythagorasEasyWidget(self)
        self.second_widget = ThreeDPythagorasEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class PythagStackTDPMedium(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = ThreeDPythagorasMediumWidget(self)
        self.second_widget = ThreeDPythagorasMediumWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class PythagStackTDPHard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = ThreeDPythagorasHardWidget(self)
        self.second_widget = ThreeDPythagorasHardWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class VectorsStackEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = VectorsEasyWidget(self)
        self.second_widget = VectorsEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class VectorsStackMedium(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = VectorsMediumWidget(self)
        self.second_widget = VectorsMediumWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class VectorsStackHard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = VectorsHardWidget(self)
        self.second_widget = VectorsHardWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class ReviseTrigStackEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = EasySummaryWidget(self)
        self.second_widget = EasySummaryWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class ReviseTrigStackMedium(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = MediumSummaryWidget(self)
        self.second_widget = MediumSummaryWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class ReviseTrigStackHard(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = HardSummaryWidget(self)
        self.second_widget = HardSummaryWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)
