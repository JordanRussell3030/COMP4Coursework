from PyQt4.QtCore import *
from PyQt4.QtGui import *

from homework_widgets import *
from homework_widgets_page_2 import *

class SidesAHOEasyStack(QWidget):
    nextWindow = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.page_1 = SidesAHOEasyWidget()
        self.page_2 = SidesAHOEasyWidget2()

        self.layout = QStackedLayout()

        self.layout.addWidget(self.page_1)
        self.layout.addWidget(self.page_2)

        self.setLayout(self.layout)

        self.setCentralWidget(self.page_1)

        
