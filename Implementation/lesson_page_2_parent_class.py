from PyQt4.QtGui import * #These two lines import all of the built in PyQt code
from PyQt4.QtCore import *

#This is the parent class which provides the default attributes for all of these child classes
class ParentLessonPage2(QWidget):
    #Constructor
    def __init__(self, parent = None):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This is the parent variable which allows the child classes to inherit the connections to the second widget in the stacks       
        self.parent = parent

        #Sets the background colour of the window to white for all of the child classes
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #All of the widgets are created here, as they are used in each child class
        #The text unique attributes are set in the child classes
        self.answer = QLineEdit()
        #Sets the size of the widgets
        self.answer.setMinimumWidth(80)
        self.answer.setMinimumHeight(110)
        #Sets the font size and house style of the text
        self.answer.setFont(QFont("Courier", 40))
        
        self.previous = QPushButton("Previous")
        self.previous.setMinimumHeight(110)
        self.previous.setMinimumWidth(60)
        self.previous.setFont(QFont("Courier", 40))
        self.previous.setStyleSheet("QPushButton {background-color: red; color: white; font-size: 20;}")
        
        self.check = QPushButton("Check Answer")
        self.check.setMinimumHeight(110)
        self.check.setMinimumWidth(60)
        self.check.setFont(QFont("Courier", 40))
        self.check.setStyleSheet("QPushButton {background-color: yellow; color: black; font-size: 20;}")
        
        self.finish = QPushButton("Finish")
        self.finish.setMinimumHeight(110)
        self.finish.setMinimumWidth(60)
        self.finish.setFont(QFont("Courier", 40))
        self.finish.setStyleSheet("QPushButton {background-color: green; color: white; font-size: 20;}")

        self.text_1 = QTextEdit()
        self.text_1.setMinimumWidth(80)
        self.text_1.setMinimumHeight(110)
        self.text_1.setFont(QFont("Courier", 20))
        self.text_1.setReadOnly(True)
        
        self.text_2 = QTextEdit()
        self.text_2.setMinimumWidth(80)
        self.text_2.setMinimumHeight(110)
        self.text_2.setFont(QFont("Courier", 20))
        self.text_2.setReadOnly(True)

        #Sets the background colour and font colour of all the buttons in all of the child classes
        #with just one line
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        #Sets the layout as a QGridLayout so all of the widgets can be positioned easily
        self.layout = QGridLayout()

        #Sets layout as the layout to be used
        self.setLayout(self.layout)

        #Adds the widgets to the layout
        self.layout.addWidget(self.text_1, 0, 0) #These numbers position the widgets in the layout
        self.layout.addWidget(self.text_2, 0, 1)
        self.layout.addWidget(self.previous, 3, 0)
        self.layout.addWidget(self.answer, 3, 1)
        self.layout.addWidget(self.finish, 4, 0)
        self.layout.addWidget(self.check, 4, 1)

        #The connections for navigation and checking the practice answer
        self.previous.clicked.connect(self.previous_selected)
        self.check.clicked.connect(self.check_selected)
        self.finish.clicked.connect(self.finish_selected)

    #Switches back to the previous screen in the stack window (page 1)
    def previous_selected(self):
        self.parent.stack.setCurrentIndex(0)

    #This checks to see if the practice answer is correct
    def check_selected(self):
        #If it's correct it just tells them they are correct
        #Nothing is saved from the lessons
        if self.answer.text() == self.answer_lesson:
            self.answer.setText("{0} Correct".format(self.answer_lesson))
        else:
            self.answer.setText("Incorrect")
        #Disables the buttons so they can't edit their answer
        self.answer.setReadOnly(True)
        self.check.setEnabled(False)

    #Closes the entire stack window
    def finish_selected(self):
        self.parent.close()
