from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

#This is the template for the very first screen which appears when the program is run
class FirstScreen(QWidget):
    #This is the signal for the connection which switches to the second screen in the stack
    #When the button is clicked, NameEntered becomes true and the connection is executed
    NameEntered = pyqtSignal()
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #These four lines of code set the background of the screen to white
        pal = QPalette()
        #This line selects the colour for the background
        pal.setColor(QPalette.Background, Qt.white)
        #This line makes the background automatically change to the chosen colour whenever it is displayed
        self.setAutoFillBackground(True)
        #Sets the screen's palette to the one selected above
        self.setPalette(pal)

        self.message = QLabel("Welcome to the Triangle Geometry Education Program")
        #This changes the QLabel's font size and house style
        self.message.setFont(QFont("Courier", 40))
        #This aligns the QLabel to the centre of the width of the screen
        self.message.setAlignment(Qt.AlignCenter)

        #This is the button which connects to the home screen, the second screen in the stack
        self.cont = QPushButton("Continue")
        #This sets the minimum height and width for the QPushButton so that different screen sizes can all work
        self.cont.setMinimumHeight(110)
        self.cont.setMinimumWidth(60)
        #Changes the font size and house style of the text in the QPushButton
        self.cont.setFont(QFont("Courier", 40))

        #This is a picture
        self.pic = QLabel()
        #The picture is imported from the file below
        self.pic.setPixmap(QPixmap("powered_by_python"))
        #This centralises the picture in its designated area
        self.pic.setAlignment(Qt.AlignCenter)

        #Sets the layout to a QGridLayout so that all the widgets can be positioned easily
        self.layout = QGridLayout()

        #Sets layout as the layot used in the widget
        self.setLayout(self.layout)

        #Adds the widgets to the layout 
        self.layout.addWidget(self.pic, 0, 0) #The numbers here position the widgets
        self.layout.addWidget(self.message, 1, 0)
        self.layout.addWidget(self.cont, 2, 0)

        #This sets the QPushButton's background colour and font colour
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        #This is the connection for the button, when clicked the enter method is executed
        self.cont.clicked.connect(self.enter)

    #This is run when the continue button is clicked
    def enter(self):
        #This is the pyqtSignal - when NameEntered is changed to true, the signal is emitted, and this switches the screento the home screen
        self.NameEntered.emit()
