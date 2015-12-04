import sqlite3

from PyQt4.QtCore import *

from PyQt4.QtGui import *

import sys

from database_gui import *
from database_class import *

class DatabaseWidget(QWidget):
    def __init(self):
        super().__init__()
        self.combo_box = QComboBox()

        self.label = QLabel("Database")

        self.layout = QVBoxLayout()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.combo_box)

        self.setLayout(self.layout)
