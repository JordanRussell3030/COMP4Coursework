from PyQt4.QtGui import *
from PyQt4.QtCore import *
#
from login_screen_window import *
from admin_account_home import *

class ResultsMenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Results")
        self.picture = QLabel("Shape")
        self.back = QPushButton("Return")
        self.result_1 = QPushButton("Result 1")
        self.result_2 = QPushButton("Result 2")
        self.result_3 = QPushButton("Result 3")
        self.result_4 = QPushButton("Result 4")
        self.result_5 = QPushButton("Result 5")

        self.layout = QGridLayout()

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.picture, 1, 0)
        self.layout.addWidget(self.back, 5, 0)
        self.layout.addWidget(self.result_1, 1, 1)
        self.layout.addWidget(self.result_2, 2, 1)
        self.layout.addWidget(self.result_3, 3, 1)
        self.layout.addWidget(self.result_4, 4, 1)
        self.layout.addWidget(self.result_5, 5, 1)

        self.setLayout(self.layout)

        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        pass
