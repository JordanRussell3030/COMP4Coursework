import sqlite3
from PyQt4.QtGui import *
from PyQt4.QtCore import *
#
import sys

from database_class import *

class DatabaseGUI(QWidget):
    def __init(self):
        super().__init__()

        self._parent = parent
        self.setWindowTitle("Database")

        self._name_label = QLabel("List of students")
        self._teacher_list = QComboBox()

        self.PopulateStudentComboBox()

        self._close_button = QPushButton("Close")

        self.layout = QVBoxLayout()

        self.layout.addWidget(name_label)
        self.layout.addWidget(self._student_list)
        self.layout.addWidget(_close_button)

        self.widget = QWidget()
        self.layout.setLayout(self.layout)

        self.setCentralWidget(self.widget)

        self._close_button.clicked.connect(self.onCloseClick)

    def onCloseClick(self):
        self.close()

    def PopulateStudentComboBox(self):
        students = g_database.GetallStudents()
        for student in students:
            self._student_list.addItem(student[1])
##        self.combo_box = QComboBox()
##
##        self.label = QLabel("Database")
##
##        self.layout = QVBoxLayout()
##
##        self.layout.addWidget(self.label)
##        self.layout.addWidget(self.combo_box)
##
##        self.setLayout(self.layout)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DatabaseGUI()
    window.show()
    window.raise_()
    app.exec_()
