from PyQt4.QtCore import * #These two lines import all of the built in PyQt code
from PyQt4.QtGui import *

from lesson_widgets_page_1 import * #This contains the first widget of each stack widget
from lesson_page_2 import * #This contains the second widget of each stack widget

#These are the templates for the stack widgets which contain a first and a second page each for a lesson
class Trig1StackSides(QMainWindow):
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This maximises the window
        self.showMaximized()

        #Assigns variables to the first and second widgets so that when ths specific stack is run
        #the lesson pages will be relevant to each other
        self.first_widget = SidesAHOWidget(self)
        self.second_widget = SidesAHOWidgetPage2(self)

        #Sets the stack a a QStackedLayout so that the two windows can be switched between
        #in the same window
        self.stack = QStackedLayout()

        #Adds the widgets to the stack layout
        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        #Creates a QWidget, as this class is a QMainWindow, and sets the stack as
        #the layout to be used
        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        #Sets the QWidget as the central widget so it will actually appear
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

class VectorStack(QMainWindow):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.first_widget = EasyWidget(self)
        self.second_widget = VectorWidgetPage2(self)

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
