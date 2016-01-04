from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
#
from lesson_menu_widget import *
from homework_menu_widget import *
from database_widget import *
from admin_homework_widget import *
from results_menu_widget import *
from add_names_widget import *

class AdminAccountWidget(QWidget):
##    selected_homework = pyqtSignal()
##    selected_results = pyqtSignal()
##    selected_progress = pyqtSignal()
    #self.radio_buttons = RadioButtonWidget("GCSE Trigonometry and Pythagoras Program", "Please select an option" ("Lessons", "Homework", "Progress"))
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.homework = QPushButton("Homework")
        self.results = QPushButton("Results")
        self.progress = QPushButton("Progress")
        self.add_names = QPushButton("Add Students")
        self.homework_label = QLabel("To set homework,\nclick here: ")
        self.homework_label.setFont(QFont("Courier", 30))
        self.results_label = QLabel("To view your classes\nmost recent results\nclick here: ")
        self.results_label.setFont(QFont("Courier", 30))
        self.database_label = QLabel("To view all students\nprogress so far,\nclick here: ")
        self.database_label.setFont(QFont("Courier", 30))
        self.account_label = QLabel("Account No: XXXX\nUsername: XXXX\nClass XXXX")
        self.account_label.setFont(QFont("Courier", 30))
        self.log_out = QPushButton("Log out")
        self.picture = QLabel("Shape")
        self.names_label = QLabel("To add a new\nclass or names,\nclick here: ")
        self.names_label.setFont(QFont("Courier", 30))

        self.homework.setMinimumHeight(110)
        self.homework.setMinimumWidth(60)
        self.homework.setFont(QFont("Courier", 40))
        self.homework.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.results.setMinimumHeight(110)
        self.results.setMinimumWidth(60)
        self.results.setFont(QFont("Courier", 40))
        self.results.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.progress.setMinimumHeight(110)
        self.progress.setMinimumWidth(60)
        self.progress.setFont(QFont("Courier", 40))
        self.progress.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.log_out.setMinimumHeight(110)
        self.log_out.setMinimumWidth(60)
        self.log_out.setFont(QFont("Courier", 40))
        self.log_out.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.add_names.setMinimumHeight(110)
        self.add_names.setMinimumWidth(60)
        self.add_names.setFont(QFont("Courier", 40))
        self.add_names.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")
        
        self.layout = QGridLayout()

        self.layout.addWidget(self.homework, 0, 1)
        self.layout.addWidget(self.picture, 0, 2)
        self.layout.addWidget(self.results, 1, 1)
        self.layout.addWidget(self.progress, 2, 1)
        self.layout.addWidget(self.add_names, 3, 1)
        self.layout.addWidget(self.homework_label, 0, 0)
        self.layout.addWidget(self.results_label, 1, 0)
        self.layout.addWidget(self.database_label, 2, 0)
        self.layout.addWidget(self.account_label, 0, 3)
        self.layout.addWidget(self.picture, 1, 3)
        self.layout.addWidget(self.log_out, 3, 3)
        self.layout.addWidget(self.names_label, 3, 0)

        self.setLayout(self.layout)

        self.homework.clicked.connect(self.selected_homework)
        self.results.clicked.connect(self.selected_results)
        self.progress.clicked.connect(self.selected_progress)
        self.log_out.clicked.connect(self.log_out_selected)
        self.add_names.clicked.connect(self.selected_add_names)

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

    def selected_add_names(self):
        add_names_widget = AddNamesWidget()
        add_names_widget.show()
        add_names_widget._raise()
