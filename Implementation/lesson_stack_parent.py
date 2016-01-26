from PyQt4.QtCore import *
from PyQt4.QtGui import *

from login_widget import *
from easy_trig_widget import *
from lesson_page_2 import *
from derived_lesson_menus import *

class ParentStackWidgetLesson(QMainWindow):
    def __init__(self):
        super().__init__()

        self.first_widget = None
        self.second_widget = None

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.stack = QStackedLayout()
        
        self.stack.addWidget(self.first_widget)
        self.stack.addWidget(self.second_widget)

        self.widget = QWidget()
        self.widget.setLayout(self.stack)

        self.setCentralWidget(self.widget)
