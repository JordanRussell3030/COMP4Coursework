from PyQt4.QtGui import *
from PyQt4.QtCore import *

from lesson_page_2 import *
from easy_trig_widget import *

class ParentLessonPage2(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()
        
        self.answer = QLineEdit()
        self.previous = QPushButton("Previous")
        self.check = QPushButton("Check Answer")
        self.finish = QPushButton("Finish")
        self.text_1 = QTextEdit()
        self.text_2 = QTextEdit()

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        self.buttons = []

        self.buttons.append(self.previous)
        self.buttons.append(self.check)
        self.buttons.append(self.finish)

        self.previous.setMinimumHeight(110)
        self.previous.setMinimumWidth(60)
        self.previous.setFont(QFont("Courier", 40))

        self.check.setMinimumHeight(110)
        self.check.setMinimumWidth(60)
        self.check.setFont(QFont("Courier", 40))

        self.finish.setMinimumHeight(110)
        self.finish.setMinimumWidth(60)
        self.finish.setFont(QFont("Courier", 40))

        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.answer.setMinimumWidth(80)
        self.answer.setMinimumHeight(110)
        self.answer.setFont(QFont("Courier", 40))

        self.text_1.setMinimumWidth(80)
        self.text_1.setMinimumHeight(110)
        self.text_1.setFont(QFont("Courier", 20))

        self.text_2.setMinimumWidth(80)
        self.text_2.setMinimumHeight(110)
        self.text_2.setFont(QFont("Courier", 20))

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.answer, 3, 1)
        self.layout.addWidget(self.previous, 3, 0)
        self.layout.addWidget(self.check, 4, 1)
        self.layout.addWidget(self.finish, 4, 0)
        self.layout.addWidget(self.text_1, 0, 0)
        self.layout.addWidget(self.text_2, 0, 1)

        self.previous.clicked.connect(self.previous_selected)
        self.check.clicked.connect(self.check_selected)
        self.finish.clicked.connect(self.finish_selected)

    def previous_selected(self):
        self.close()

    def check_selected(self):
        if self.answer.text() == self.answer_lesson:
            self.answer.setText("{0} Correct".format(self.answer_lesson))
        else:
            self.answer.setText("Incorrect")

    def finish_selected(self):
        self.close()
        #open lesson menu window
