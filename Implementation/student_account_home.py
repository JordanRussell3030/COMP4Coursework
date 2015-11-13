from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

class UserAccountWidget(QWidget):
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
        print("Success lessons")

    def selected_homework(self):
        print("Success homework")

    def selected_progress(self):
        print("Success progress")
        
       
        
