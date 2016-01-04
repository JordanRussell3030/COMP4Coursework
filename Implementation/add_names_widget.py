from PyQt4.QtGui import *
from PyQt4.QtCore import *
#
from admin_account_home import *
from add_class_widget import *
#from database import *

class AddNamesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        self.add_class = QPushButton("Add Class")
        self.select_class = QComboBox()
        self.input_first_name = QLineEdit()
        self.label_1 = QLabel("Please input the student's first name: ")
        self.input_last_name = QLineEdit()
        self.label_2 = QLabel("Please input the student's last name: ")
        self.submit_1 = QPushButton("Add Name")
        self.submit_2 = QPushButton("Add Another")
        self.back = QPushButton("Return")

        self.add_class.setMinimumHeight(110)
        self.add_class.setMinimumWidth(60)
        self.add_class.setFont(QFont("Courier", 40))
        self.add_class.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

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

        self.input_first_name.setMinimumHeight(110)
        self.input_first_name.setMinimumWidth(60)
        self.input_first_name.setFont(QFont("Courier", 40))
##        self.submit_2.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.input_last_name.setMinimumHeight(110)
        self.input_last_name.setMinimumWidth(60)
        self.input_last_name.setFont(QFont("Courier", 40))

        self.label_1.setFont(QFont("Courier", 20))
        self.label_2.setFont(QFont("Courier", 20))

        self.select_class.setMinimumHeight(110)
        self.select_class.setMinimumWidth(60)
        self.select_class.setFont(QFont("Courier", 40))
        self.select_class.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue}")

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.add_class, 0, 1)
        self.layout.addWidget(self.select_class, 0, 0)
        self.layout.addWidget(self.input_first_name, 1, 1)
        self.layout.addWidget(self.input_last_name, 2, 1)
        self.layout.addWidget(self.label_1, 1, 0)
        self.layout.addWidget(self.label_2, 2, 0)
        self.layout.addWidget(self.submit_1, 3, 0)
        self.layout.addWidget(self.submit_2, 3, 1)
        self.layout.addWidget(self.back, 4, 0)

        self.add_class.clicked.connect(self.selected_add_class)
        self.submit_1.clicked.connect(self.selected_submit_1)
        self.submit_2.clicked.connect(self.selected_submit_2)
        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()

    def selected_add_class(self):
        self.close()
        add_class = AddClassWidget()
        add_class.show()
        add_class._raise()

    def selected_submit_1(self):
        pass
        #SQL add name to database

    def selected_submit_2(self):
        pass
        #SQL add names to database
