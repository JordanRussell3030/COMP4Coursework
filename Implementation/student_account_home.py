from PyQt4.QtGui import * #These two lines import all of the built in PyQt code
from PyQt4.QtCore import *

import sys #This is needed for the exit button - to close the entire program
#The only built-in function that works exactly how it needs to here is from sys

from lesson_menu_widget import * #Contains the lesson menu for when the lessons button is clicked
from homework_menu_widget import * #Contains the homework menu for when the homework button is clicked
from database_widget import * #Contains the database widget for when the progress button is clicked

#This class is the template for the home screen; the second screen in the first stack
#when the program is first run
class UserAccountWidget(QWidget):
    #Constructor
    def __init__(self, parent):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()
        
        #This is the parent variable which allows the child classes to inherit the connections to the second widget in the stacks       
        self.parent_window = parent

        #Sets the background colour of the window to white
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #This button connects to the lesson menu
        self.lessons = QPushButton("Lessons")
        #Sets the size of the buttons
        self.lessons.setMinimumWidth(90)
        self.lessons.setMinimumHeight(110)
        #Sets the font size and house style of the text in the buttons
        self.lessons.setFont(QFont("Courier", 40))

        #This button connects to the homework menu        
        self.homework = QPushButton("Homework")
        self.homework.setMinimumWidth(90)
        self.homework.setMinimumHeight(110)
        self.homework.setFont(QFont("Courier", 40))

        #This button connects to the progress screen
        self.progress = QPushButton("Progress")
        self.progress.setMinimumWidth(90)
        self.progress.setMinimumHeight(110)
        self.progress.setFont(QFont("Courier", 40))
        
        self.lessons_label = QLabel("To view lessons\nand learn more,\nclick here! ")
        #Sets the font size and house style in of the QLabel text
        self.lessons_label.setFont(QFont("Courier", 25))
        
        self.homework_label = QLabel("To access the\nhomework set for\nyou to complete,\nclick here! ")
        self.homework_label.setFont(QFont("Courier", 25))
        
        self.database_label = QLabel("To view your\nprogress so far,\nclick here! ")
        self.database_label.setFont(QFont("Courier", 25))
        
        self.log_out = QPushButton("Exit Program")
        self.log_out.setMinimumWidth(90)
        self.log_out.setMinimumHeight(110)
        self.log_out.setFont(QFont("Courier", 40))
        #Overrides the style of the buttons in the window - exit button distinguished from
        #other buttons
        self.log_out.setStyleSheet("QPushButton {background-color: #D3E5FF; color: red; font-size: 20;}")

        #These are pictures - one for each button
        self.picture = QLabel()
        #This imports the picture from the below file
        self.picture.setPixmap(QPixmap("student_account_home_pic"))
        #This aligns the picture to the centre of its designated area
        self.picture.setAlignment(Qt.AlignCenter)
        
        self.homework_pic = QLabel()
        self.homework_pic.setPixmap(QPixmap("student_home_homework"))
        self.homework_pic.setAlignment(Qt.AlignCenter)  
        
        self.smiler = QLabel()
        self.smiler.setPixmap(QPixmap("smile"))
        self.smiler.setAlignment(Qt.AlignCenter)

        #Sets the background colour and font colour of all of the buttons in the window
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")

        #Sets the layout to a QGridLayout so that the widgets are positioned easily
        self.layout = QGridLayout()

        #Adds the widgets to the layout
        self.layout.addWidget(self.lessons, 0, 1)#These numbers position the widgets in the layout
        self.layout.addWidget(self.picture, 0, 2)
        self.layout.addWidget(self.homework, 1, 1)
        self.layout.addWidget(self.progress, 2, 1)
        self.layout.addWidget(self.lessons_label, 0, 0)
        self.layout.addWidget(self.homework_label, 1, 0)
        self.layout.addWidget(self.database_label, 2, 0)
        self.layout.addWidget(self.picture, 1, 3)
        self.layout.addWidget(self.log_out, 2, 3)
        self.layout.addWidget(self.smiler, 2, 2)
        self.layout.addWidget(self.homework_pic, 1, 2)

        #Sets layout as the layout to be used
        self.setLayout(self.layout)

        #These are the connections which connect to the next screens when the buttons are clicked
        self.lessons.clicked.connect(self.selected_lessons)
        self.homework.clicked.connect(self.selected_homework)
        self.progress.clicked.connect(self.selected_progress)
        self.log_out.clicked.connect(self.log_out_selected)

    #This is where the 'import sys' is needed - it stops the entire program without
    #displaying a message asking the user if they are sure they want to exit
    def log_out_selected(self):
        sys.exit()

    #These are the methods from the connections
    def selected_lessons(self):
        #Assigns a variable to the widget
        lessonmenuwidget = LessonMenuWidget()
        #This displays the window in front of the previous window
        lessonmenuwidget.show()
        lessonmenuwidget._raise()
        lessonmenuwidget.showMaximized()
##        self.parent_window.close()

    def selected_homework(self):
        homeworkmenuwidget = HomeworkMenuWidget()
        homeworkmenuwidget.show()
        homeworkmenuwidget._raise()
        homeworkmenuwidget.showMaximized()

    def selected_progress(self):
        databasewidget = DatabaseWidget()
        databasewidget.show()
        databasewidget._raise()
        databasewidget.showMaximized()  
