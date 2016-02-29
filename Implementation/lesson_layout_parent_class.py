from PyQt4.QtGui import * #These two lines import all of the built in PyQt code
from PyQt4.QtCore import *

#This is the parent class which provides the default attributes to all of the child lesson page 1 widgets
class ParentLessonLayout(QWidget):
    #Constructor
    def __init__(self, parent = None):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This is the parent variable which allows the child classes to inherit the connections to the second widget in the stacks       
        self.parent = parent

        #This sets the title which is included in all child classes; the QPixmap is set in the child classes so they can all be different
        self.title = QLabel()

        #Sets the background colour of the window to white in all of the child classes
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #All of these widgets are used in each of the child classes; they are created and formatted here then the text is set in the child classes
        self.back = QPushButton("Return")
        #Sets the size of the button
        self.back.setMinimumHeight(50)
        self.back.setMinimumWidth(60)
        #Changes the font size and house style of the QPushButton
        self.back.setFont(QFont("Courier", 40))
        self.back.setStyleSheet("QPushButton {background-color: red; color: white; font-size: 20;}")
        
        self.next = QPushButton("Next")
        self.next.setMinimumHeight(50)
        self.next.setMinimumWidth(60)
        self.next.setFont(QFont("Courier", 40))

        self.lesson_1 = QTextEdit()
        self.lesson_1.setMinimumHeight(400)
        self.lesson_1.setMinimumWidth(80)
        self.lesson_1.setFont(QFont("Courier", 20))
        #Prevents the user from being able to change the text of the lessons
        self.lesson_1.setReadOnly(True)
        
        self.lesson_2 = QTextEdit()
        self.lesson_2.setMinimumHeight(400)
        self.lesson_2.setMinimumWidth(80)
        self.lesson_2.setFont(QFont("Courier", 20))
        self.lesson_2.setReadOnly(True)

        #Sets the background colour and font colour of all of the QPushButtons in each child class
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        #Sets the layout to a QGridLayout so that each widget can be positioned easily
        self.layout = QGridLayout()

        #Adds all of the widgets to the layout
        self.layout.addWidget(self.title, 0, 0) #These numbers position the widgets in the window
        self.layout.addWidget(self.lesson_1, 1, 0)
        self.layout.addWidget(self.lesson_2, 1, 1)
        self.layout.addWidget(self.back, 3, 0)
        self.layout.addWidget(self.next, 3, 1)

        #Sets layout as the layout to be used
        self.setLayout(self.layout)

        #These are the connections which are the same in each child class;
        #any that are different will be in the child classes, for example connecting to different windows
        self.back.clicked.connect(self.selected_back)
        self.next.clicked.connect(self.selected_next_page)

    #This method closes the entire stack window
    def selected_back(self):
        self.parent.close()


