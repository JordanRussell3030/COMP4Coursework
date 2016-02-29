from PyQt4.QtCore import * #These two lines import all of the built in PyQt code
from PyQt4.QtGui import *

#This is the parent class which provides the default attributes for the 5 child lesson menus
class ParentLessonMenu(QWidget):
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This maximises the window of each child class
        self.showMaximized()

        #This sets the background colour of each window 
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #The QLabel is declared here because all 5 child menus will have one
        #The QPixmap is set in the child class
        self.title = QLabel()

        #All of the widgets have either 2 or 3 options to select, so 3 buttons are created
        #here, then either 2 or 3 can be addded to the layout in the child class
        #The text is set in the child class
        self.button_1 = QPushButton()
        #Sets the size of the button
        self.button_1.setMinimumHeight(110)
        self.button_1.setMinimumWidth(60)
        #Sets the font size and house style of the text in the button
        self.button_1.setFont(QFont("Courier", 40))
        
        self.button_2 = QPushButton()
        self.button_2.setMinimumHeight(110)
        self.button_2.setMinimumWidth(60)
        self.button_2.setFont(QFont("Courier", 40))
        
        self.button_3 = QPushButton()
        self.button_3.setMinimumHeight(110)
        self.button_3.setMinimumWidth(60)
        self.button_3.setFont(QFont("Courier", 40))
   
        self.back = QPushButton("Return")
        self.back.setMinimumHeight(100)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 40))
        self.back.setStyleSheet("QPushButton {background-color: red; color: white; font-size: 20;}")

        #Sets the background colour and font colour of all the buttons in all of the child classes
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        #Sets the layout to a QGridLayout so the widgets can be positioned easily
        self.layout = QGridLayout()

        #Sets layout as the layout to be used
        self.setLayout(self.layout)

        #The back button is added here because it is in the same place in every child class
        self.layout.addWidget(self.back, 3, 0) #These numbers position the widget at the bottm
                                               #it doesn't matter whether there are two or three buttons above,
                                               #as the program ignores gaps by default

        #This connection is the same in each child class so it is written here, as is the method
        self.back.clicked.connect(self.selected_back)

    #This closes the window and returns the user to the previous screen
    def selected_back(self):
        self.close()


