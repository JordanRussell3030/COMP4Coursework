from PyQt4.QtGui import * #These two lines import all of the built in PyQt code
from PyQt4.QtCore import *

from derived_lesson_menus import * #This contains all of the lesson menus which the buttons in the class connect to

#This is the template for the lesson topic menu (the one before the menus for each topic)
class LessonMenuWidget(QMainWindow):
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #Maximises the screen when it is displayed
        self.showMaximized()

        #Sets the background colour of the window to white
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #These are the buttons which each connect to  a different child menu
        self.t1 = QPushButton("Trigonometry 1")
        #Sets the size of hte buttons - having a minimum
        # and maximum size helps prevent overlapping on different sizes of screen
        self.t1.setMinimumWidth(90)
        self.t1.setMinimumHeight(110)
        #This sets the font size and house style of the text in the QPushButton
        self.t1.setFont(QFont("Courier", 40))
        
        self.t1_pic = QLabel()
        #Imports the image from the file below
        self.t1_pic.setPixmap(QPixmap("t1_pic"))
        #Aligns the image in the centre of its designated space
        self.t1_pic.setAlignment(Qt.AlignCenter)
        
        self.t2 = QPushButton("Trigonometry 2")
        self.t2.setMinimumWidth(90)
        self.t2.setMinimumHeight(110)
        self.t2.setFont(QFont("Courier", 40))
        
        self.t2_pic = QLabel()
        self.t2_pic.setPixmap(QPixmap("t2_pic"))
        self.t2_pic.setAlignment(Qt.AlignCenter)
        
        self.pyt = QPushButton("Pythagoras")
        self.pyt.setMinimumWidth(90)
        self.pyt.setMinimumHeight(110)
        self.pyt.setFont(QFont("Courier", 40))
        
        self.pyt_pic = QLabel()
        self.pyt_pic.setPixmap(QPixmap("pyt_pic"))
        self.pyt_pic.setAlignment(Qt.AlignCenter)
        
        self.pytrig = QPushButton("Vectors")
        self.pytrig.setMinimumWidth(90)
        self.pytrig.setMinimumHeight(110)
        self.pytrig.setFont(QFont("Courier", 40))
        
        self.pytrig_pic = QLabel()
        self.pytrig_pic.setPixmap(QPixmap("pytrig_pic"))
        self.pytrig_pic.setAlignment(Qt.AlignCenter)
        
        self.sum = QPushButton("Summary")
        self.sum.setMinimumWidth(90)
        self.sum.setMinimumHeight(110)
        self.sum.setFont(QFont("Courier", 40))
        
        self.sum_pic = QLabel()
        self.sum_pic.setPixmap(QPixmap("sum_pic"))
        self.sum_pic.setAlignment(Qt.AlignCenter)

        #This button returns to the previous window, unlike the other buttons,
        #so it is a different colour to make it clear that it serves a different
        #purpose
        self.back = QPushButton("Return")
        self.back.setMinimumWidth(90)
        self.back.setMinimumHeight(110)
        self.back.setFont(QFont("Courier", 40))
        #This overrides the style of the other buttons
        self.back.setStyleSheet("QPushButton {background-color: red; color: white; font-size: 20;}")
    
        self.lesson_label = QLabel("Lessons")
        self.lesson_label.setFont(QFont("Courier", 40))
        
        self.select = QLabel("Please select a topic: ")
        self.select.setFont(QFont("Courier", 25))
        
        self.title_pic = QLabel()
        self.title_pic.setPixmap(QPixmap("title_lessons"))

        #This sets the background colour and font colour of all the QPushButtons
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")

        #Sets the layout as a QGridLayout so all the widgets can be positioned easily
        self.layout = QGridLayout()

        #Adds all of the widgets to the layout
        self.layout.addWidget(self.title_pic, 0, 0) #These numbers position the widgets
        self.layout.addWidget(self.t1_pic, 1, 0)
        self.layout.addWidget(self.t1, 1, 1)
        self.layout.addWidget(self.t2, 2, 0)
        self.layout.addWidget(self.t2_pic, 2, 1)
        self.layout.addWidget(self.pyt_pic, 3, 0)
        self.layout.addWidget(self.pyt, 3, 1)
        self.layout.addWidget(self.pytrig, 4, 0)
        self.layout.addWidget(self.pytrig_pic, 4, 1)
        self.layout.addWidget(self.sum_pic, 5, 0)
        self.layout.addWidget(self.sum, 5, 1)
        self.layout.addWidget(self.back, 6, 0)

        #These 3 lines set _centralwidget as the layout to be used
        #It needs to be declared as a QWidget because the class it's in is a QMainWindow
        self._centralwidget = QWidget()
        self._centralwidget.setLayout(self.layout)
        self.setCentralWidget(self._centralwidget)

        #The connections for the buttons
        self.t1.clicked.connect(self.selected_t1) #These are the methods executed when the button is clicked
        self.t2.clicked.connect(self.selected_t2)
        self.pyt.clicked.connect(self.selected_pyt)
        self.pytrig.clicked.connect(self.selected_pytrig)
        self.sum.clicked.connect(self.selected_sum)
        self.back.clicked.connect(self.selected_back)

    #These open the selected menus and display them
    def selected_t1(self):
        trig_1_widget = Trigonometry1()
        trig_1_widget.show()
        trig_1_widget._raise()
        trig_1_widget.showMaximized()

    def selected_t2(self):
        trig_2_widget = Trigonometry2()
        trig_2_widget.show()
        trig_2_widget._raise()
        trig_2_widget.showMaximized()

    def selected_pyt(self):
        pythagoras_widget = Pythagoras()
        pythagoras_widget.show()
        pythagoras_widget._raise()
        pythagoras_widget.showMaximized()

    def selected_pytrig(self):
        pyth_trig_widget = PythagTrig()
        pyth_trig_widget.show()
        pyth_trig_widget._raise()
        pyth_trig_widget.showMaximized()

    def selected_sum(self):
        summary_widget = Summary()
        summary_widget.show()
        summary_widget._raise()
        summary_widget.showMaximized()

    #This closes the window and returns the user to the previous window
    def selected_back(self):
        self.close()
