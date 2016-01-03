from PyQt4.QtGui import *
from PyQt4.QtCore import *

from database_widget import *

class ReportWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.header = QLabel("Report")
        self.header.setFont(QFont("Courier", 30))

        self.criteria = QLabel("Please select the criteria for your progress report: ")
        self.criteria.setFont(QFont("Courier", 30))

        self.class_box_label = QLabel("Please select a class to query")
        self.class_box_label.setFont(QFont("Courier", 25))
        self.class_box = QComboBox()
        self.choice = QLabel("Please select a student or a\ntask to query: ")
        self.choice.setFont(QFont("Courier", 25))
        self.student_box_label = QLabel("Please select a student\nto query")
        self.student_box_label.setFont(QFont("Courier", 25))
        self.student_box = QComboBox()
        self.task_box_label = QLabel("Please select a task\nto query")
        self.task_box_label.setFont(QFont("Courier", 25))
        self.task_box = QComboBox()
        self.score_box_label = QLabel("Please input the maximum\nscore you would like\nto query: ")
        self.score_box_label.setFont(QFont("Courier", 25))
        self.score_box = QComboBox()
        self.back = QPushButton("Return")
        self.submit = QPushButton("Query")

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.class_box_label, 0, 0)
        self.layout.addWidget(self.class_box, 0, 1)
        self.layout.addWidget(self.choice, 1, 0)
        self.layout.addWidget(self.student_box_label, 2, 0)
        self.layout.addWidget(self.student_box, 3, 0)
        self.layout.addWidget(self.task_box_label, 2, 1)
        self.layout.addWidget(self.task_box, 3, 1)
        self.layout.addWidget(self.score_box_label, 4, 0)
        self.layout.addWidget(self.score_box, 4, 1)
        self.layout.addWidget(self.back, 5, 0)
        self.layout.addWidget(self.submit, 5, 1)

        self.class_box.setMinimumWidth(60)
        self.class_box.setMinimumHeight(100)
        self.class_box.setFont(QFont("Courier", 30))
        self.class_box.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")


        self.student_box.setMinimumWidth(60)
        self.student_box.setMinimumHeight(100)
        self.student_box.setFont(QFont("Courier", 30))
        self.student_box.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")


        self.task_box.setMinimumWidth(60)
        self.task_box.setMinimumHeight(100)
        self.task_box.setFont(QFont("Courier", 30))
        self.task_box.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")


        self.score_box.setMinimumWidth(60)
        self.score_box.setMinimumHeight(100)
        self.score_box.setFont(QFont("Courier", 30))
        self.score_box.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")


        self.back.setMinimumWidth(60)
        self.back.setMinimumHeight(100)
        self.back.setFont(QFont("Courier", 30))
        self.back.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")


        self.submit.setMinimumWidth(60)
        self.submit.setMinimumHeight(100)
        self.submit.setFont(QFont("Courier", 30))
        self.submit.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")


        self.back.clicked.connect(self.selected_back)
        self.submit.clicked.connect(self.selected_submit)

    def selected_back(self):
        self.close()

    def selected_submit(self):
        pass
        #search database for input items
