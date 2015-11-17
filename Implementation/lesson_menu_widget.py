from PyQt4.QtGui import *
from PyQt4.QtCore import *
from login_screen_window import *
from login_widget import *
from student_account_home import *

class LessonMenuWidget(QWidget):
    def __init__(self):
        super().__init__()
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

        self.setLayout(self.layout)

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
        print("et1")

    def selected_et2(self):
        print("et2")

    def selected_et3(self):
        print("et3")

    def selected_mt1(self):
        print("mt1")

    def selected_mt2(self):
        print("mt2")

    def selected_mt3(self):
        print("mt3")

    def selected_ht1(self):
        print("ht1")

    def selected_ht2(self):
        print("ht2")

    def selected_ht3(self):
        print("ht3")

    def selected_ext1(self):
        print("ext1")

    def selected_ext2(self):
        print("ext2")

    def selected_ext3(self):
        print("ext3")

    def selected_ep(self):
        print("ep")

    def selected_mp(self):
        print("mp")

    def selected_hp(self):
        print("hp")

    def selected_tdp1(self):
        print("tdp1")

    def selected_tdp2(self):
        print("tdp2")

    def selected_tdt1(self):
        print("tdt1")

    def selected_tdt2(self):
        print("tdt2")

    def selected_back(self):
        print("Back")
