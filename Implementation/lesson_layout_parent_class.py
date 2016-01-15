from PyQt4.QtGui import *
from PyQt4.QtCore import *
#
from easy_trig_widget import *
from derived_lesson_menus import *

class ParentLessonLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.title = QLabel()

        self.back = QPushButton("Return")
        self.next = QPushButton("Next")

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.back.setMinimumHeight(50)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 40))
        self.back.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.next.setMinimumHeight(50)
        self.next.setMinimumWidth(60)
        self.next.setFont(QFont("Courier", 40))
        self.next.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.lesson_1 = QTextEdit()
        self.lesson_2 = QTextEdit()

        self.lesson_1.setMinimumHeight(400)
        self.lesson_1.setMinimumWidth(80)
        self.lesson_1.setFont(QFont("Courier", 20, QFont.Bold))

        self.lesson_2.setMinimumHeight(400)
        self.lesson_2.setMinimumWidth(80)
        self.lesson_2.setFont(QFont("Courier", 20))

        self.layout = QGridLayout()

        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.back, 3, 0)
        self.layout.addWidget(self.next, 3, 1)
        self.layout.addWidget(self.lesson_1, 1, 0)
        self.layout.addWidget(self.lesson_2, 1, 1)

        self.setLayout(self.layout)

        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()


