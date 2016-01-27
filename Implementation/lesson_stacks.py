from PyQt4.QtCore import *
from PyQt4.QtGui import *

from lesson_stack_parent import *
from derived_lesson_menus import *
from easy_trig_widget import *
from lesson_page_2 import *

class Trig1StackSides(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = SidesAHOWidget(self)
        self.second_widget = SidesAHOWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig1StackSOHCAHTOA(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = SOHCAHTOAWidget(self)
        self.second_widget = SOHCAHTOAWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig2StackFA(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = FindingAnglesWidget(self)
        self.second_widget = FindingAnglesWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Trig2StackTDT(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = ThreeDTrigonometryWidget(self)
        self.second_widget = ThreeDTrigonometryWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class PythagStackTheorem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = PythagTheoremWidget(self)
        self.second_widget = PythagTheoremWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class PythagStackTDP(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.showMaximized()
        
        self.first_widget = ThreeDPythagorasWidget(self)
        self.second_widget = ThreeDPythagorasWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class EasyStack(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = EasyWidget(self)
        self.second_widget = EasyWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class MediumStack(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = MediumWidget(self)
        self.second_widget = MediumWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class HardStack(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = HardWidget(self)
        self.second_widget = HardWidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Revise1Stack(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = ReviseTrig1Widget(self)
        self.second_widget = ReviseTrig1WidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Revise2Stack(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = ReviseTrig2Widget(self)
        self.second_widget = ReviseTrig2WidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)

class Revise3Stack(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = ReviseTrig3Widget(self)
        self.second_widget = ReviseTrig3WidgetPage2(self)

        self.stack = QStackedLayout()

        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)
