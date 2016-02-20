from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

from derived_homework_menus import * #This contains the topic specific menu classes which open when the buttons are clicked

#This is the template for the homework topic menu (before the individual homework menus)
class HomeworkMenuWidget(QMainWindow):
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #Maximises the screen
        self.showMaximized()

        #Changes the background colour of the window to white
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.title = QLabel()
        self.title.setFont(QFont("Courier", 40))

        #These buttons all connect to a child menu class, which inherit from the HomeworkMenuParentClass
        self.ht1 = QPushButton("Trigonometry 1")
        #Sets the minimum width and height of the button to reduce problems with different screen sizes
        self.ht1.setMinimumWidth(90)
        self.ht1.setMinimumHeight(110)
        #Sets the font size and house style of the text in the QPushButton
        self.ht1.setFont(QFont("Courier", 40))
        
        self.ht2 = QPushButton("Trigonometry 2")
        self.ht2.setMinimumWidth(90)
        self.ht2.setMinimumHeight(110)
        self.ht2.setFont(QFont("Courier", 40))
        
        self.hpyt = QPushButton("Pythagoras")
        self.hpyt.setMinimumWidth(90)
        self.hpyt.setMinimumHeight(110)
        self.hpyt.setFont(QFont("Courier", 40))
        
        self.hpytrig = QPushButton("Vectors")
        self.hpytrig.setMinimumWidth(90)
        self.hpytrig.setMinimumHeight(110)
        self.hpytrig.setFont(QFont("Courier", 40))
        
        self.hsum = QPushButton("Summary")
        self.hsum.setMinimumWidth(90)
        self.hsum.setMinimumHeight(110)
        self.hsum.setFont(QFont("Courier", 40))
        
        self.back = QPushButton("Return")
        self.back.setMinimumWidth(90)
        self.back.setMinimumHeight(110)
        self.back.setFont(QFont("Courier", 40))
        #Overrides the style of the other buttons so the user can distinguish it from the homework menu buttons easily
        self.back.setStyleSheet("QPushButton {background-color: #D3E5FF; color: red; font-size: 20;}")

        #Each button has a picture with it
        self.ht1_pic = QLabel()
        #This imports the picture from the file name below
        self.ht1_pic.setPixmap(QPixmap("homework_trig_1_pic"))
        #This aligns the picture to the centre of its designated area
        self.ht1_pic.setAlignment(Qt.AlignCenter)
        
        self.ht2_pic = QLabel()
        self.ht2_pic.setPixmap(QPixmap("homework_trig_2_pic"))
        self.ht2_pic.setAlignment(Qt.AlignCenter)
        
        self.hpyt_pic = QLabel()
        self.hpyt_pic.setPixmap(QPixmap("homework_pythag_pic"))
        self.hpyt_pic.setAlignment(Qt.AlignCenter)
        
        self.hpytrig_pic = QLabel()
        self.hpytrig_pic.setPixmap(QPixmap("homework_vectors_pic"))
        self.hpytrig_pic.setAlignment(Qt.AlignCenter)
        
        self.hsum_pic = QLabel()
        self.hsum_pic.setPixmap(QPixmap("homework_summary_pic"))
        self.hsum_pic.setAlignment(Qt.AlignCenter)

        #This sets the bacground colour and font colour of all of the buttons in the window
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")

        #This sets the layout as a QGridLayout so that each widget can be positioned easily
        self.layout = QGridLayout()

        #These add the widgets to the layout
        self.layout.addWidget(self.title, 0, 0) #These numbers position the widget in the window
        self.layout.addWidget(self.ht1_pic, 2, 0)
        self.layout.addWidget(self.ht1, 2, 1)
        self.layout.addWidget(self.ht2, 3, 0)
        self.layout.addWidget(self.ht2_pic, 3, 1)
        self.layout.addWidget(self.hpyt_pic, 4, 0)
        self.layout.addWidget(self.hpyt, 4, 1)
        self.layout.addWidget(self.hpytrig, 5, 0)
        self.layout.addWidget(self.hpytrig_pic, 5, 1)
        self.layout.addWidget(self.hsum_pic, 6, 0)
        self.layout.addWidget(self.hsum, 6, 1)
        self.layout.addWidget(self.back, 7, 0)

        #This chunk of code sets the centralwidget as the layout - it has to use a QWidget because this class is a QMainWindow
        self._centralwidget = QWidget()
        self._centralwidget.setLayout(self.layout)
        self.setCentralWidget(self._centralwidget)

        #These are the connections for the buttons - the methods are executed when they are clicked
        self.ht1.clicked.connect(self.selected_ht1)
        self.ht2.clicked.connect(self.selected_ht2)
        self.hpyt.clicked.connect(self.selected_hpyt)
        self.hpytrig.clicked.connect(self.selected_hpytrig)
        self.hsum.clicked.connect(self.selected_hsum)
        self.back.clicked.connect(self.selected_back)

    #These are the methods executed when the buttons are clicked
    def selected_ht1(self):
        #This assigns a variable to a widget then opens and displays the widget
        trigonometry_1_homework = Trigonometry1HW()
        trigonometry_1_homework.show()
        trigonometry_1_homework._raise()
        trigonometry_1_homework.showMaximized()

    def selected_ht2(self):
        trigonometry_2_homework = Trigonometry2HW()
        trigonometry_2_homework.show()
        trigonometry_2_homework._raise()
        trigonometry_2_homework.showMaximized()

    def selected_hpyt(self):
        pythagoras_homework = PythagorasHW()
        pythagoras_homework.show()
        pythagoras_homework._raise()
        pythagoras_homework.showMaximized()

    def selected_hpytrig(self):
        pythag_trig_homework = PythagTrigonometryHW()
        pythag_trig_homework.show()
        pythag_trig_homework._raise()
        pythag_trig_homework.showMaximized()

    def selected_hsum(self):
        summary_homework = SummaryHW()
        summary_homework.show()
        summary_homework._raise()
        summary_homework.showMaximized()

    def selected_back(self):
        #This closes the entire window
        self.close()
