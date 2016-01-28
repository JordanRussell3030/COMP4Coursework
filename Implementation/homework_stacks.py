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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

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

        self.first_widget = SidesAHOEasyWidget(self)
        self.second_widget = SidesAHOEasyWidget2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)
