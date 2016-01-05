from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
from student_account_home import *
from derived_lesson_menus import *
#
class LessonMenuWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        
        self.t1 = QPushButton("Trigonometry 1")
        self.t2 = QPushButton("Trigonometry 2")
        self.pyt = QPushButton("Pythagoras")
        self.pytrig = QPushButton("Pythagoras and Trigonometry Problems")
        self.sum = QPushButton("Summary")
        self.back = QPushButton("Return")
        self.lesson_label = QLabel("Lessons")
        self.picture = QLabel("Shape")
        self.select = QLabel("Please select a topic: ")

        self.t1.setMinimumWidth(90)
        self.t1.setMinimumHeight(110)
        self.t1.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")
        self.t1.setFont(QFont("Courier", 40))

        self.t2.setMinimumWidth(90)
        self.t2.setMinimumHeight(110)
        self.t2.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")
        self.t2.setFont(QFont("Courier", 40))

        self.pyt.setMinimumWidth(90)
        self.pyt.setMinimumHeight(110)
        self.pyt.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")
        self.pyt.setFont(QFont("Courier", 40))

        self.pytrig.setMinimumWidth(90)
        self.pytrig.setMinimumHeight(110)
        self.pytrig.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")
        self.pytrig.setFont(QFont("Courier", 30))

        self.sum.setMinimumWidth(90)
        self.sum.setMinimumHeight(110)
        self.sum.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")
        self.sum.setFont(QFont("Courier", 40))

        self.back.setMinimumWidth(90)
        self.back.setMinimumHeight(110)
        self.back.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")
        self.back.setFont(QFont("Courier", 40))

        self.lesson_label.setFont(QFont("Courier", 40))
        self.picture.setFont(QFont("Courier", 25))
        self.select.setFont(QFont("Courier", 25))

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
        trig_1_widget.showMaximized()

    def selected_t2(self):
        trig_2_widget = Trigonometry2()
        trig_2_widget.show()
        trig_2_widget._raise()
        trig_2_widget.showMaximized()

    def selected_pyt(self):
        pythagoras_widget = Pythagoras()
        pythagoras_widget.show()
        pythagoras_widget._raise()
        pythagoras_widget.showMaximized()

    def selected_pytrig(self):
        pyth_trig_widget = PythagTrig()
        pyth_trig_widget.show()
        pyth_trig_widget._raise()
        pyth_trig_widget.showMaximized()

    def selected_sum(self):
        summary_widget = Summary()
        summary_widget.show()
        summary_widget._raise()
        summary_widget.showMaximized()

    def selected_back(self):
        self.close()
        self.student_home = UserAccountWidget()
        self.student_home.show()
        self.student_home._raise()
