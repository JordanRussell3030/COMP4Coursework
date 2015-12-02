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
        self.ht1 = QPushButton("Trigonometry 1")
        self.ht2 = QPushButton("Trigonometry 2")
        self.hpyt = QPushButton("Pythagoras")
        self.hpytrig = QPushButton("Pythagoras and Trigonometry Problems")
        self.hsum = QPushButton("Summary")
        self.back = QPushButton("Back")

        self.layout = QGridLayout()

        self.layout.addWidget(self.ht1)
        self.layout.addWidget(self.ht2)
        self.layout.addWidget(self.hpyt)
        self.layout.addWidget(self.hpytrig)
        self.layout.addWidget(self.hsum)
        self.layout.addWidget(self.back)

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
        lessonmenuhomework.close()
        student_home.show()
        student_home._raise()
