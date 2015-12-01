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
        self.back = QPushButton("Back")

        self.layout = QGridLayout()

        self.layout.addWidget(self.t1)
        self.layout.addWidget(self.t2)
        self.layout.addWidget(self.pyt)
        self.layout.addWidget(self.pytrig)
        self.layout.addWidget(self.sum)
        self.layout.addWidget(self.back)

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
        lessonmenuwidget.close()
        student_home.show()
        student_home._raise()
