from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from homework_menu_widget import *
from student_account_home import *
from derived_homework_menus import *
from homework_widgets import *

class HomeworkMenuWidget(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        self.et1 = QPushButton("Easy Trigonometry 1")
        self.et2 = QPushButton("Easy Trigonometry 2")
        self.et3 = QPushButton("Easy Trigonometry 3")
        self.mt1 = QPushButton("Medium Trigonometry 1")
        self.mt2 = QPushButton("Medium Trigonometry 2")
        self.mt3 = QPushButton("Medium Trigonometry 3")
        self.ht1 = QPushButton("Hard Trigonometry 1")
        self.ht2 = QPushButton("Hard Trigonometry 2")
        self.ht3 = QPushButton("Hard Trigonometry 3")
        self.ext1 = QPushButton("Extended Trigonometry 1")
        self.ext2 = QPushButton("Extended Trigonometry 2")
        self.ext3 = QPushButton("Extended Trigonometry 3")
        self.ep = QPushButton("Easy Pythagoras")
        self.mp = QPushButton("Medium Pythagoras")
        self.hp = QPushButton("Hard Pythagoras")
        self.tdp1 = QPushButton("3D Pythagoras 1")
        self.tdp2 = QPushButton("3D Pythagoras 2")
        self.tdt1 = QPushButton("3D Trigonometry 1")
        self.tdt2 = QPushButton("3D Trigonometry 2")
        self.back = QPushButton("Back")

        self.layout = QGridLayout()

        self.layout.addWidget(self.et1)
        self.layout.addWidget(self.et2)
        self.layout.addWidget(self.et3)
        self.layout.addWidget(self.mt1)
        self.layout.addWidget(self.mt2)
        self.layout.addWidget(self.mt3)
        self.layout.addWidget(self.ht1)
        self.layout.addWidget(self.ht2)
        self.layout.addWidget(self.ht3)
        self.layout.addWidget(self.ext1)
        self.layout.addWidget(self.ext2)
        self.layout.addWidget(self.ext3)
        self.layout.addWidget(self.ep)
        self.layout.addWidget(self.mp)
        self.layout.addWidget(self.hp)
        self.layout.addWidget(self.tdp1)
        self.layout.addWidget(self.tdp2)
        self.layout.addWidget(self.tdt1)
        self.layout.addWidget(self.tdt2)
        self.layout.addWidget(self.back)

        #self.setLayout(self.layout)
        self._centralwidget = QWidget()
        self._centralwidget.setLayout(self.layout)
        self.setCentralWidget(self._centralwidget)

        self.et1.clicked.connect(self.selected_et1)
        self.et2.clicked.connect(self.selected_et2)
        self.et3.clicked.connect(self.selected_et3)
        self.mt1.clicked.connect(self.selected_mt1)
        self.mt2.clicked.connect(self.selected_mt2)
        self.mt3.clicked.connect(self.selected_mt3)
        self.ht1.clicked.connect(self.selected_ht1)
        self.ht2.clicked.connect(self.selected_ht2)
        self.ht3.clicked.connect(self.selected_ht3)
        self.ext1.clicked.connect(self.selected_ext1)
        self.ext2.clicked.connect(self.selected_ext2)
        self.ext3.clicked.connect(self.selected_ext3)
        self.ep.clicked.connect(self.selected_ep)
        self.mp.clicked.connect(self.selected_mp)
        self.hp.clicked.connect(self.selected_hp)
        self.tdp1.clicked.connect(self.selected_tdp1)
        self.tdp2.clicked.connect(self.selected_tdp2)
        self.tdt1.clicked.connect(self.selected_tdt1)
        self.tdt2.clicked.connect(self.selected_tdt2)
        self.back.clicked.connect(self.selected_back)

    def selected_et1(self):
        easy_trig_1_homework = EasyTrigonometry1HW()
        easy_trig_1_homework.show()
        easy_trig_1_homework.raise_()

    def selected_et2(self):
        easy_trig_2_homework = EasyTrigonometry2HW()
        easy_trig_2_homework.show()
        easy_trig_2_homework.raise_()

    def selected_et3(self):
        easy_trig_3_homework = EasyTrigonometry3HW()
        easy_trig_3_homework.show()
        easy_trig_3_homework.raise_()

    def selected_mt1(self):
        medium_trig_1_homework = MediumTrigonometry1HW()
        medium_trig_1_homework.show()
        medium_trig_1_homework.raise_()

    def selected_mt2(self):
        medium_trig_2_homework = MediumTrigonometry2HW()
        medium_trig_2_homework.show()
        medium_trig_2_homework.raise_()

    def selected_mt3(self):
        medium_trig_3_homework = MediumTrigonometry3HW()
        medium_trig_3_homework.show()
        medium_trig_3_homework.raise_()

    def selected_ht1(self):
        hard_trig_1_homework = HardTrigonometry1HW()
        hard_trig_1_homework.show()
        hard_trig_1_homework.raise_()

    def selected_ht2(self):
        hard_trig_2_homework = HardTrigonometry2HW()
        hard_trig_2_homework.show()
        hard_trig_2_homework.raise_()

    def selected_ht3(self):
        hard_trig_3_homework = HardTrigonometry3HW()
        hard_trig_3_homework.show()
        hard_trig_3_homework.raise_()

    def selected_ext1(self):
        extended_trig_1_homework = ExtendedTrigonometry1HW()
        extended_trig_1_homework.show()
        extended_trig_1_homework.raise_()

    def selected_ext2(self):
        extended_trig_2_homework = ExtendedTrigonometry2HW()
        extended_trig_2_homework.show()
        extended_trig_2_homework.raise_()

    def selected_ext3(self):
        extended_trig_3_homework = ExtendedTrigonometry3HW()
        extended_trig_3_homework.show()
        extended_trig_3_homework.raise_()

    def selected_ep(self):
        easy_pythagoras_1_homework = EasyPythagorasHW()
        easy_pythagoras_1_homework.show()
        easy_pythagoras_1_homework.raise_()

    def selected_mp(self):
        medium_pythagoras_1_homework = MediumPythagorasHW()
        medium_pythagoras_1_homework.show()
        medium_pythagoras_1_homework.raise_()

    def selected_hp(self):
        hard_pythagoras_1_homework = HardPythagorasHW()
        hard_pythagoras_1_homework.show()
        hard_pythagoras_1_homework.raise_()

    def selected_tdp1(self):
        threed_pythagoras_1_homework = TDPythagoras1HW()
        threed_pythagoras_1_homework.show()
        threed_pythagoras_1_homework.raise_()

    def selected_tdp2(self):
        threed_pythagoras_2_homework = TDPythagoras2HW()
        threed_pythagoras_2_homework.show()
        threed_pythagoras_2_homework.raise_()

    def selected_tdt1(self):
        threed_trigonometry_1_homework = TDTrigonometry1HW()
        threed_trigonometry_1_homework.show()
        threed_trigonometry_1_homework.raise_()

    def selected_tdt2(self):
        threed_trigonometry_2_homework = TDTrigonometry2HW()
        threed_trigonometry_2_homework.show()
        threed_trigonometry_2_homework.raise_()

    def selected_back(self):
        lessonmenuhomework.close()
        student_home.show()
        student_home.raise_()
