from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from database_widget import *

class UserAccountWidget(QWidget):
    selected_lessons = pyqtSignal()
    selected_homework = pyqtSignal()
    selected_progress = pyqtSignal()
    #self.radio_buttons = RadioButtonWidget("GCSE Trigonometry and Pythagoras Program", "Please select an option" ("Lessons", "Homework", "Progress"))
    def __init__(self):
        super().__init__()
        self.lessons = QPushButton("Lessons")
        self.homework = QPushButton("Homework")
        self.progress = QPushButton("Progress")
        self.lessons_label = QLabel("To view lessons and learn more, click here! ")
        self.homework_label = QLabel("To access the homework set for you to complete, click here! ")
        self.database_label = QLabel("To view you progress so far, click here! ")
        self.account_label = QLabel("Account No: XXXX Username: XXXX Average Rating")
        self.log_out = QPushButton("Log out")

        
        self.layout = QGridLayout()

        self.layout.addWidget(self.lessons, 0, 1)
        self.layout.addWidget(self.homework, 1, 1)
        self.layout.addWidget(self.progress, 2, 1)
        self.layout.addWidget(self.lessons_label, 0, 0)
        self.layout.addWidget(self.homework_label, 1, 0)
        self.layout.addWidget(self.database_label, 2, 0)
        self.layout.addWidget(self.account_label, 0, 3)
        #self.picture(1, 3)
        self.layout.addWidget(self.log_out, 2, 3)

        self.setLayout(self.layout)

        self.lessons.clicked.connect(self.selected_lessons)
        self.homework.clicked.connect(self.selected_homework)
        self.progress.clicked.connect(self.selected_progress)
        self.log_out.clicked.connect(self.log_out_selected)

    def log_out_selected(self):
        self.close()

    def selected_lessons(self):
        lessonmenuwidget = LessonMenuWidget()
        lessonmenuwidget.show()
        lessonmenuwidget._raise()
#        self.stack.setCurrentIndex(2)

    def selected_homework(self):
        homeworkmenuwidget = HomeworkMenuWidget()
        homeworkmenuwidget.show()
        homeworkmenuwidget._raise()
        #self.stack.setCurrentIndex(3)

    def selected_progress(self):
        databasewidget = DatabaseWidget()
        databasewidget.show()
        databasewidget._raise()
        #self.stack.setCurrentIndex(4)
        
       
        
