from PyQt4.QtGui import *
from PyQt4.QtCore import *

from login_widget import *
from student_account_home import *
from lesson_menu_widget import *
from database_class import *
from report_widget import *

class DatabaseWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.showMaximized()

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        
        self.title = QLabel("Progress")
##        self.details = QLabel("Account No: XXXX\nUsername: XXXX\nAverage Rating: X")
##        self.not_success = QPushButton("Not completed")
##        self.not_success_2 = QPushButton("Not enough score")
        self.back = QPushButton("Return")
        self.database = QTableWidget()
        self.report = QPushButton("Report")

        self.title.setFont(QFont("Courier", 40))
##        self.details.setFont(QFont("Courier", 40))

##        self.not_success.setMinimumWidth(60)
##        self.not_success.setMinimumHeight(100)
##        self.not_success.setFont(QFont("Courier", 40))

        self.report.setMinimumWidth(60)
        self.report.setMinimumHeight(100)
        self.report.setFont(QFont("Courier", 40))

##        self.not_success_2.setMinimumWidth(60)
##        self.not_success_2.setMinimumHeight(100)
##        self.not_success_2.setFont(QFont("Courier", 40))

        self.back.setMinimumWidth(60)
        self.back.setMinimumHeight(100)
        self.back.setFont(QFont("Courier", 40))

        self.database.setRowCount(100)
        self.database.setColumnCount(6)
        self.database_header = ("Task Name", "Question 1", "Question 2", "Question 3", "Question 4")#"Total"
        self.database.setHorizontalHeaderLabels(self.database_header)
        self.database.setMinimumWidth(45)
        self.database.setMinimumHeight(890)
        
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")
        self.database.setStyleSheet("QTableView {selection-background-color: #A3C1DA;}")
        self.back.setStyleSheet("QPushButton {background-color: #D3E5FF; color: red;}")

        students = g_database.GetAllNames()
        for student in students:
            self.database.setItem(0, 0, QTableWidgetItem(student[0]))
            self.database.setItem(0, 1, QTableWidgetItem(str(student[1])))
            self.database.setItem(0, 2, QTableWidgetItem(str(student[2])))
            self.database.setItem(0, 3, QTableWidgetItem(str(student[3])))
            self.database.setItem(0, 4, QTableWidgetItem(str(student[4])))
##            self.database.setItem(0, 5, QTableWidgetItem(str(student[5])))

        self.layout = QGridLayout()

        self.layout.addWidget(self.database, 0, 1)
        self.layout.addWidget(self.title, 0, 0)
##        self.layout.addWidget(self.details, 1, 0)
##        self.layout.addWidget(self.not_success, 2, 0)
##        self.layout.addWidget(self.not_success_2, 3, 0)
        self.layout.addWidget(self.back, 4, 0)
        self.layout.addWidget(self.report, 4, 1)

        self.setLayout(self.layout)

        self.back.clicked.connect(self.selected_back)
        self.report.clicked.connect(self.selected_report)

    def selected_back(self):
        self.close()

    def selected_report(self):
        report_widget = ReportWidget()
        report_widget.show()
        report_widget._raise()

##class AdminDatabaseWidget(QWidget):
##    def __init__(self):
##        super().__init__()
##        
##        self.showMaximized()
##        
##        self.title = QLabel("Progress")
##        self.details = QLabel("Account No: XXXX\nUsername: XXXX\nClass: X")
##        self.back = QPushButton("Return")
##        self.database = QTableWidget()
##        self.report = QPushButton("Report")
##
##        self.title.setFont(QFont("Courier", 40))
##        self.details.setFont(QFont("Courier", 40))
##
##        self.report.setMinimumWidth(60)
##        self.report.setMinimumHeight(100)
##        self.report.setFont(QFont("Courier", 40))
##        self.report.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")
##
##        self.back.setMinimumWidth(60)
##        self.back.setMinimumHeight(100)
##        self.back.setFont(QFont("Courier", 40))
##        self.back.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")
##
##        self.database.setRowCount(22)
##        self.database.setColumnCount(8)
##        self.database_header = ("StudentID", "First Name", "Last Name")
##        self.database.setHorizontalHeaderLabels(self.database_header)
##        self.database.setMinimumWidth(45)
##        self.database.setMinimumHeight(577)
##
##        self.database.setStyleSheet("QTableView {selection-background-color: cyan;}");
##
####        students = g_database.GetAllNames()
####        for student in students:
####            self.database.setItem(0, 0, QTableWidgetItem(str(student[0])))
####            self.database.setItem(0, 1, QTableWidgetItem(student[1]))
##
##        self.layout = QGridLayout()
##
##        self.layout.addWidget(self.database, 0, 1)
##        self.layout.addWidget(self.title, 0, 0)
##        self.layout.addWidget(self.details, 1, 0)
##        self.layout.addWidget(self.back, 2, 0)
##        self.layout.addWidget(self.report, 2, 1)
##
##        self.setLayout(self.layout)
##
##        self.back.clicked.connect(self.selected_back)
##        self.report.clicked.connect(self.selected_report)
##
##    def selected_back(self):
##        self.close()
##        
##    def selected_report(self):
##        report_widget = ReportWidget()
##        report_widget.show()
##        report_widget._raise()
