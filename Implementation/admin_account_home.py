from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *

from lesson_menu_widget import *
from homework_menu_widget import *
from database_widget import *
from admin_homework_widget import *
from results_menu_widget import *

class AdminAccountWidget(QWidget):
    selected_homework = pyqtSignal()
    selected_results = pyqtSignal()
    selected_progress = pyqtSignal()
    #self.radio_buttons = RadioButtonWidget("GCSE Trigonometry and Pythagoras Program", "Please select an option" ("Lessons", "Homework", "Progress"))
    def __init__(self):
        super().__init__()
        self.homework = QPushButton("Homework")
        self.results = QPushButton("Results")
        self.progress = QPushButton("Progress")
        self.homework_label = QLabel("To set homework,\nclick here! ")
        self.results_label = QLabel("To view your classes\nmost recent results\nclick here! ")
        self.database_label = QLabel("To view all students\nprogress so far,\nclick here! ")
        self.account_label = QLabel("Account No: XXXX\nUsername: XXXX\nClass XXXX")
        self.log_out = QPushButton("Log out")
        self.picture = QLabel("Shape")

        
        self.layout = QGridLayout()

        self.layout.addWidget(self.homework, 0, 1)
        self.layout.addWidget(self.picture, 0, 2)
        self.layout.addWidget(self.results, 1, 1)
        self.layout.addWidget(self.progress, 2, 1)
        self.layout.addWidget(self.homework_label, 0, 0)
        self.layout.addWidget(self.results_label, 1, 0)
        self.layout.addWidget(self.database_label, 2, 0)
        self.layout.addWidget(self.account_label, 0, 3)
        self.layout.addWidget(self.picture, 1, 3)
        self.layout.addWidget(self.log_out, 2, 3)

        self.setLayout(self.layout)

        self.homework.clicked.connect(self.selected_homework)
        self.results.clicked.connect(self.selected_results)
        self.progress.clicked.connect(self.selected_progress)
        self.log_out.clicked.connect(self.log_out_selected)

    def log_out_selected(self):
        self.close()

    def selected_homework(self):
        adminhomeworkmenuwidget = AdminHomeworkMenuWidget()
        adminhomeworkmenuwidget.show()
        adminhomeworkmenuwidget._raise()
#        self.stack.setCurrentIndex(2)

    def selected_results(self):
        resultsmenuwidget = ResultsMenuWidget()
        resultsmenuwidget.show()
        resultsmenuwidget._raise()
        #self.stack.setCurrentIndex(3)

    def selected_progress(self):
        admindatabasewidget = AdminDatabaseWidget()
        admindatabasewidget.show()
        admindatabasewidget._raise()
        #self.stack.setCurrentIndex(4)
