from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
from student_account_home import *
from derived_lesson_menus import *

class LessonMenuWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.t1 = QPushButton("Trigonometry 1")
        self.t2 = QPushButton("Trigonometry 2")
        self.pyt = QPushButton("Pythagoras")
        self.pytrig = QPushButton("Pythagoras and Trigonometry Problems")
        self.sum = QPushButton("Summary")
        self.back = QPushButton("Return")
        self.lesson_label = QLabel("Lessons")
        self.picture = QLabel("Shape")
        self.select = QLabel("Please select a topic: ")

        self.layout = QGridLayout()
        
        self.layout.addWidget(self.lesson_label, 0, 0)
        self.layout.addWidget(self.t1, 2, 1)
        self.layout.addWidget(self.t2, 3, 1)
        self.layout.addWidget(self.pyt, 4, 1)
        self.layout.addWidget(self.pytrig, 5, 1)
        self.layout.addWidget(self.sum, 6, 1)
        self.layout.addWidget(self.picture, 2, 0)
        self.layout.addWidget(self.back, 6, 0)
        self.layout.addWidget(self.select, 1, 0)

        #self.setLayout(self.layout)
        self._centralwidget = QWidget()
        self._centralwidget.setLayout(self.layout)
        self.setCentralWidget(self._centralwidget)

        self.t1.clicked.connect(self.selected_t1)
        self.t2.clicked.connect(self.selected_t2)
        self.pyt.clicked.connect(self.selected_pyt)
        self.pytrig.clicked.connect(self.selected_pytrig)
        self.sum.clicked.connect(self.selected_sum)
        self.back.clicked.connect(self.selected_back)

    def selected_t1(self):
        trig_1_widget = Trigonometry1()
        trig_1_widget.show()
        trig_1_widget._raise()

    def selected_t2(self):
        trig_2_widget = Trigonometry2()
        trig_2_widget.show()
        trig_2_widget._raise()

    def selected_pyt(self):
        pythagoras_widget = Pythagoras()
        pythagoras_widget.show()
        pythagoras_widget._raise()

    def selected_pytrig(self):
        pyth_trig_widget = PythagTrig()
        pyth_trig_widget.show()
        pyth_trig_widget._raise()

    def selected_sum(self):
        summary_widget = Summary()
        summary_widget.show()
        summary_widget._raise()

    def selected_back(self):
        self.close()
        self.student_home = UserAccountWidget()
        self.student_home.show()
        self.student_home._raise()
