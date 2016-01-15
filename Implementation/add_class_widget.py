from PyQt4.QtGui import *
from PyQt4.QtCore import *
#
#from database import *
##from admin_account_home import *
from add_names_widget import *

class AddClassWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        self.add_students = QPushButton("Add Students")
        self.input_class_id = QLineEdit()
        self.label_1 = QLabel("Please input the Class ID: ")
        self.submit_1 = QPushButton("Add Class")
        self.submit_2 = QPushButton("Add Another")
        self.back = QPushButton("Return")

        self.add_students.setMinimumHeight(110)
        self.add_students.setMinimumWidth(60)
        self.add_students.setFont(QFont("Courier", 40))
        self.add_students.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.back.setMinimumHeight(110)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 40))
        self.back.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.submit_1.setMinimumHeight(110)
        self.submit_1.setMinimumWidth(60)
        self.submit_1.setFont(QFont("Courier", 40))
        self.submit_1.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.submit_2.setMinimumHeight(110)
        self.submit_2.setMinimumWidth(60)
        self.submit_2.setFont(QFont("Courier", 40))
        self.submit_2.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.input_class_id.setMinimumHeight(110)
        self.input_class_id.setMinimumWidth(60)
        self.input_class_id.setFont(QFont("Courier", 40))

        self.label_1.setFont(QFont("Courier", 20))

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.add_students, 0, 1)
        self.layout.addWidget(self.input_class_id, 1, 1)
        self.layout.addWidget(self.label_1, 1, 0)
        self.layout.addWidget(self.submit_1, 2, 0)
        self.layout.addWidget(self.submit_2, 2, 1)
        self.layout.addWidget(self.back, 3, 0)

        self.add_students.clicked.connect(self.selected_add_students)
        self.submit_1.clicked.connect(self.selected_submit_1)
        self.submit_2.clicked.connect(self.selected_submit_2)
        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()

    def selected_add_students(self):
        pass
##        add_student = AddNamesWidget()
##        add_student.show()
##        add_student._raise()

    def selected_submit_1(self):
        pass
        #SQL add class to database

    def selected_submit_2(self):
        pass
        #SQL add classes to database
