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
    def __init__(self, parent):
        super().__init__()
        self.parent_window = parent
        self.lessons = QPushButton("Lessons")
        self.homework = QPushButton("Homework")
        self.progress = QPushButton("Progress")
        self.lessons_label = QLabel("To view lessons\nand learn more,\nclick here! ")
        self.homework_label = QLabel("To access the\nhomework set for\nyou to complete,\nclick here! ")
        self.database_label = QLabel("To view your\nprogress so far,\nclick here! ")
        self.account_label = QLabel("Account No: XXXX\nUsername: XXXX\nAverage Rating: XXXX")
        self.log_out = QPushButton("Log out")
        self.picture = QLabel("Shape")

        
        self.layout = QGridLayout()

        self.layout.addWidget(self.lessons, 0, 1)
        self.layout.addWidget(self.picture, 0, 2)
        self.layout.addWidget(self.homework, 1, 1)
        self.layout.addWidget(self.progress, 2, 1)
        self.layout.addWidget(self.lessons_label, 0, 0)
        self.layout.addWidget(self.homework_label, 1, 0)
        self.layout.addWidget(self.database_label, 2, 0)
        self.layout.addWidget(self.account_label, 0, 3)
        self.layout.addWidget(self.picture, 1, 3)
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
        self.parent_window.close()

    def selected_homework(self):
        homeworkmenuwidget = HomeworkMenuWidget()
        homeworkmenuwidget.show()
        homeworkmenuwidget._raise()

    def selected_progress(self):
        databasewidget = DatabaseWidget()
        databasewidget.show()
        databasewidget._raise()
        
       
        
