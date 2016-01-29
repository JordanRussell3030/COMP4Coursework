from PyQt4.QtCore import *
from PyQt4.QtGui import *

from derived_homework_menus import *
from homework_widgets import *
from homework_widgets_page_2 import *

class Trig1StackSidesEasy(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

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
