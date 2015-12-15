from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from homework_menu_widget import *
from student_account_home import *
from derived_homework_menus import *
from homework_widgets import *

class HomeworkMenuWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Homework")
        self.ht1 = QPushButton("Trigonometry 1")
        self.ht2 = QPushButton("Trigonometry 2")
        self.hpyt = QPushButton("Pythagoras")
        self.hpytrig = QPushButton("Pythagoras and Trigonometry Problems")
        self.hsum = QPushButton("Summary")
        self.back = QPushButton("Return")
        #self.picture = QLabel("Shape")
        self.temp_set = QPushButton("Set Homework 1")
        self.temp_set_2 = QPushButton("Set Homework 2")
        self.temp_set_3 = QPushButton("Set Homework 3")
        self.select = QLabel("Please select a topic: ")

        self.layout = QGridLayout()

        self.layout.addWidget(self.ht1, 2, 1)
        self.layout.addWidget(self.ht2, 3, 1)
        self.layout.addWidget(self.hpyt, 4, 1)
        self.layout.addWidget(self.hpytrig, 5, 1)
        self.layout.addWidget(self.hsum, 6, 1)
        self.layout.addWidget(self.back, 6, 0)
        self.layout.addWidget(self.title, 0, 0)
        #self.layout.addWidget(self.picture, 2, 0)
        self.layout.addWidget(self.temp_set, 2, 0)
        self.layout.addWidget(self.temp_set_2, 3, 0)
        self.layout.addWidget(self.temp_set_3, 4, 0)
        self.layout.addWidget(self.select, 1, 0)

        #self.setLayout(self.layout)
        self._centralwidget = QWidget()
        self._centralwidget.setLayout(self.layout)
        self.setCentralWidget(self._centralwidget)

        self.ht1.clicked.connect(self.selected_ht1)
        self.ht2.clicked.connect(self.selected_ht2)
        self.hpyt.clicked.connect(self.selected_hpyt)
        self.hpytrig.clicked.connect(self.selected_hpytrig)
        self.hsum.clicked.connect(self.selected_hsum)
        self.back.clicked.connect(self.selected_back)

    def selected_ht1(self):
        trigonometry_1_homework = Trigonometry1HW()
        trigonometry_1_homework.show()
        trigonometry_1_homework._raise()

    def selected_ht2(self):
        trigonometry_2_homework = Trigonometry2HW()
        trigonometry_2_homework.show()
        trigonometry_2_homework._raise()

    def selected_hpyt(self):
        pythagoras_homework = PythagorasHW()
        pythagoras_homework.show()
        pythagoras_homework._raise()

    def selected_hpytrig(self):
        pythag_trig_homework = PythagTrigonometryHW()
        pythag_trig_homework.show()
        pythag_trig_homework._raise()

    def selected_hsum(self):
        summary_homework = SummaryHW()
        summary_homework.show()
        summary_homework._raise()

    def selected_back(self):
        self.close()
##        student_home = UserAccountWidget()
##        student_home.show()
##        student_home._raise()
