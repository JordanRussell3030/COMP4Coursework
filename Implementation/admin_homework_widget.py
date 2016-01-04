from PyQt4.QtCore import *
from PyQt4.QtGui import *
#
from admin_account_home import *
from derived_homework_menus import *

class AdminHomeworkMenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = QLabel("Homework")
        self.select = QLabel("Recently set by teacher\nto be reviewed: ")
        self.set_1 = QPushButton("Set 1")
        self.set_2 = QPushButton("Set 2")
        self.set_3 = QPushButton("Set 3")
        self.set_4 = QPushButton("Set 4")
        self.back = QPushButton("Return")
        self.trig_1 = QPushButton("Trigonometry 1")
        self.trig_2 = QPushButton("Trigonometry 2")
        self.pyth = QPushButton("Pythagoras")
        self.pythtrig = QPushButton("Pythagoras and Trigonometry Problems")
        self.summ = QPushButton("Summary")

        self.layout = QGridLayout()

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.select, 1, 0)
        self.layout.addWidget(self.set_1, 2, 0)
        self.layout.addWidget(self.set_2, 3, 0)
        self.layout.addWidget(self.set_3, 4, 0)
        self.layout.addWidget(self.set_4, 5, 0)
        self.layout.addWidget(self.back, 6, 0)
        self.layout.addWidget(self.trig_1, 2, 1)
        self.layout.addWidget(self.trig_2, 3, 1)
        self.layout.addWidget(self.pyth, 4, 1)
        self.layout.addWidget(self.pythtrig, 5, 1)
        self.layout.addWidget(self.summ, 6, 1)

        self.setLayout(self.layout)

        self.set_1.clicked.connect(self.selected_set_1)
        self.set_2.clicked.connect(self.selected_set_2)
        self.set_3.clicked.connect(self.selected_set_3)
        self.set_4.clicked.connect(self.selected_set_4)
        self.back.clicked.connect(self.selected_back)
        self.trig_1.clicked.connect(self.selected_trig_1)
        self.trig_2.clicked.connect(self.selected_trig_2)
        self.pyth.clicked.connect(self.selected_pyth)
        self.pythtrig.clicked.connect(self.selected_pythtrig)
        self.summ.clicked.connect(self.selected_summ)


    def selected_set_1(self):
        pass

    def selected_set_2(self):
        pass

    def selected_set_3(self):
        pass

    def selected_set_4(self):
        pass

    def selected_back(self):
        pass

    def selected_trig_1(self):
        self.trig_1_widget = Trigonometry1HW()
        self.trig_1_widget.show()
        self.trig_1_widget._raise()

    def selected_trig_2(self):
        self.trig_2_widget = Trigonometry2HW()
        self.trig_2_widget.show()
        self.trig_2_widget._raise()

    def selected_pyth(self):
        self.pyth_widget = PythagorasHW()
        self.pyth_widget.show()
        self.pyth_widget._raise()

    def selected_pythtrig(self):
        self.pythtrig_widget = PythagTrigonometryHW()
        self.pythtrig_widget.show()
        self.pythtrig_widget._raise()

    def selected_summ(self):
        self.summ_widget = SummaryHW()
        self.summ_widget.show()
        self.summ_widget._raise()
