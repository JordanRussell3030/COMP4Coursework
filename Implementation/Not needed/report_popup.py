from PyQt4.QtGui import *
from PyQt4.QtCore import *

from database_class import *

class ReportWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.task_box = QLineEdit()#"{0}".format(data))
##        self.score_box = QLineEdit("{1}".format(score_data))
        self._close = QPushButton("Return")

        self.layout = QGridLayout()

        self.layout.addWidget(self.task_box, 0, 0)
##        self.layout.addWidget(self.score_box, 1, 0)
        self.layout.addWidget(self._close, 2, 0)

        self.setLayout(self.layout)

        self._close.clicked.connect(self.close_window)

    def close_window(self):
        self.close()
