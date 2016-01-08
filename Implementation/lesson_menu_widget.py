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
        self.pic = QLabel()
        self.title_pic = QLabel()

        self.title_pic.setPixmap(QPixmap("title_lessons"))

        self.pic.setPixmap(QPixmap("lesson_topic_menu_pic"))
        self.pic.setAlignment(Qt.AlignCenter)

        self.t1.setMinimumWidth(90)
        self.t1.setMinimumHeight(110)
        self.t1.setFont(QFont("Courier", 40))

        self.t2.setMinimumWidth(90)
        self.t2.setMinimumHeight(110)
        self.t2.setFont(QFont("Courier", 40))
##        self.t2.move(0, -200)

        self.pyt.setMinimumWidth(90)
        self.pyt.setMinimumHeight(110)
        self.pyt.setFont(QFont("Courier", 40))

        self.pytrig.setMinimumWidth(90)
        self.pytrig.setMinimumHeight(110)
        self.pytrig.setFont(QFont("Courier", 30))
##        self.pytrig.move(0, 300)

        self.sum.setMinimumWidth(90)
        self.sum.setMinimumHeight(110)
        self.sum.setFont(QFont("Courier", 40))

        self.back.setMinimumWidth(90)
        self.back.setMinimumHeight(110)
        self.back.setFont(QFont("Courier", 40))

        self.lesson_label.setFont(QFont("Courier", 40))
        self.picture.setFont(QFont("Courier", 25))
        self.select.setFont(QFont("Courier", 25))

        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue; font-size: 20;}")

        self.layout = QGridLayout()
        
##        self.layout.addWidget(self.lesson_label, 1, 0)
        self.layout.addWidget(self.t1, 1, 1)
        self.layout.addWidget(self.t2, 2, 1)
        self.layout.addWidget(self.pyt, 3, 1)
        self.layout.addWidget(self.pytrig, 4, 1)
        self.layout.addWidget(self.sum, 5, 1)
        self.layout.addWidget(self.pic, 0, 0)
        self.layout.addWidget(self.back, 5, 0)
        self.layout.addWidget(self.title_pic, 0, 1)
##        self.layout.addWidget(self.select, 2, 0)

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
