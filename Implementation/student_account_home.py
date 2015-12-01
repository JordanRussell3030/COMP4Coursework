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

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.lessons)
        self.layout.addWidget(self.homework)
        self.layout.addWidget(self.progress)

        self.setLayout(self.layout)

        self.lessons.clicked.connect(self.selected_lessons)
        self.homework.clicked.connect(self.selected_homework)
        self.progress.clicked.connect(self.selected_progress)

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
        
       
        
