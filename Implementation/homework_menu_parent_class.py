from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

#This is the template for the parent homework menu, which provides default attributes for 5 child homework menu classes
class ParentHomeworkMenuClass(QWidget):
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This maximises the screen - each child class will be maximised when displayed
        self.showMaximized()

        #This sets the background colour to white
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #Each child class has a title in the form of a picture, so the QLabel is defined here and the QPixmap is defined in each separate child class
        self.title = QLabel()

        #Each of the child classes have either 3 or 6 buttons which connect to a homework
        #The buttons are defined here, and all have the same characteristics, and the text is added in the child classes
        #This way either 3 or 6 buttons can be added to the layout in each child class
        self.button_1 = QPushButton()
        self.button_1.setMinimumHeight(110)
        self.button_1.setMinimumWidth(60)
        self.button_1.setFont(QFont("Courier", 40))
        
        self.button_2 = QPushButton()
        self.button_2.setMinimumHeight(110)
        self.button_2.setMinimumWidth(60)
        self.button_2.setFont(QFont("Courier", 40))
        
        self.button_3 = QPushButton()
        self.button_3.setMinimumHeight(110)
        self.button_3.setMinimumWidth(60)
        self.button_3.setFont(QFont("Courier", 40))
        
        self.button_4 = QPushButton()
        self.button_4.setMinimumHeight(110)
        self.button_4.setMinimumWidth(60)
        self.button_4.setFont(QFont("Courier", 40))
        
        self.button_5 = QPushButton()
        self.button_5.setMinimumHeight(110)
        self.button_5.setMinimumWidth(60)
        self.button_5.setFont(QFont("Courier", 40))
        
        self.button_6 = QPushButton()
        self.button_6.setMinimumHeight(110)
        self.button_6.setMinimumWidth(60)
        self.button_6.setFont(QFont("Courier", 40))

        #This button appears in every child class
        self.back = QPushButton("Return")
        self.back.setMinimumHeight(100)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 40))
        #The colour of this one is different so it can be distinguished between the buttons that take you to a homework
        self.back.setStyleSheet("QPushButton {background-color: #D3E5FF; color: red;}")

        #Each child class has 1 picture for every homework button, so the QLabels are created here,
        #and the desired amount of them can be added to the layout, depending on the number of buttons. The QPixmap is defined in the child class
        self.pic_1 = QLabel()
        #This aligns the picture to the centre of its designated area, which is required for every picture in every child class
        self.pic_1.setAlignment(Qt.AlignCenter)

        self.pic_2 = QLabel()
        self.pic_2.setAlignment(Qt.AlignCenter)
        
        self.pic_3 = QLabel()
        self.pic_3.setAlignment(Qt.AlignCenter)
        
        self.pic_4 = QLabel()
        self.pic_4.setAlignment(Qt.AlignCenter)

        self.pic_5 = QLabel()
        self.pic_5.setAlignment(Qt.AlignCenter)
        
        self.pic_6 = QLabel()
        self.pic_6.setAlignment(Qt.AlignCenter)

        #This sets the background colour and font colour for every button in each child class, except for the back button which is overridden
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")   

        #This sets the layout to a QGridLayout so that each widget can be positioned easily
        self.layout = QGridLayout()

        #This sets layout as the layout to be used
        self.setLayout(self.layout)

        #Only these two widgets are added here, because they are the same across each child class
        self.layout.addWidget(self.title, 0, 0)
        #The back button will be on the bottom one space beneath the next widget regardless of how many buttons are on the screen. No extra gaps are included
        self.layout.addWidget(self.back, 10, 0)
        #The buttons and pictures are added in the child class because 4, 5 and 6 of each won't always be used

        #This is in the parent class because it is the same for each child class; the window just closes and the previous menu is displayed
        self.back.clicked.connect(self.selected_back)
        #The other connections are in the child classes because they all have to connect to different homeworks stacks

    #The method which is executed when back is selected in any of the 5 child classes
    def selected_back(self):
        #This closes the window - the previous window will still be there
        self.close()
