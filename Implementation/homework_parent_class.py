from PyQt4.QtCore import *
from PyQt4.QtGui import *
#
from homework_widgets import *
from homework_page_2_parent_class import *
from database_class import *

class ParentHomeworkPage1Class(QWidget):
    def __init__(self):
        super().__init__()

        self.showMaximized()

        self.title = QLabel()
        self.title.setFont(QFont("Courier", 40))

        self.question_1 = QLabel()
        self.question_1.setFont(QFont("Courier", 20))

        self.question_1_shape = QLabel()
        self.question_1_shape.setFont(QFont("Courier", 40))

        self.next = QPushButton("Next")
        
        self.answer_a = QLineEdit()
        self.answer_b = QLineEdit()
        self.answer_c = QLineEdit()
        self.answer_d = QLineEdit()
        self.answer_e = QLineEdit()
        self.answer_f = QLineEdit()

        self.buttons = []

        self.answer_a.setMinimumHeight(70)
        self.answer_a.setMinimumWidth(60)
        self.answer_a.setFont(QFont("Courier", 30))

        self.answer_b.setMinimumHeight(70)
        self.answer_b.setMinimumWidth(60)
        self.answer_b.setFont(QFont("Courier", 30))

        self.answer_c.setMinimumHeight(70)
        self.answer_c.setMinimumWidth(60)
        self.answer_c.setFont(QFont("Courier", 30))

        self.answer_d.setMinimumHeight(70)
        self.answer_d.setMinimumWidth(60)
        self.answer_d.setFont(QFont("Courier", 30))

        self.answer_e.setMinimumHeight(70)
        self.answer_e.setMinimumWidth(60)
        self.answer_e.setFont(QFont("Courier", 30))

        self.answer_f.setMinimumHeight(70)
        self.answer_f.setMinimumWidth(60)
        self.answer_f.setFont(QFont("Courier", 30))
        
        self.score_box = QLabel("Score: X/X")
        self.cancel = QPushButton("Cancel")
        self.check = QPushButton("Check Answers")
        self.reset = QPushButton("Reset Answers")

        self.score_box.setFont(QFont("Courier", 30))

        self.buttons.append(self.cancel)
        self.buttons.append(self.check)
        self.buttons.append(self.reset)

        self.cancel.setMinimumHeight(110)
        self.cancel.setMinimumWidth(60)
        self.cancel.setFont(QFont("Courier", 40))

        self.check.setMinimumHeight(110)
        self.check.setMinimumWidth(60)
        self.check.setFont(QFont("Courier", 40))

        self.reset.setMinimumHeight(110)
        self.reset.setMinimumWidth(60)
        self.reset.setFont(QFont("Courier", 40))

        for button in self.buttons:
            self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.layout = QGridLayout()
        
        self.layout.addWidget(self.title, 0, 0)
        self.layout.addWidget(self.question_1, 1, 0)
        self.layout.addWidget(self.question_1_shape, 2, 0)
        self.layout.addWidget(self.answer_a, 1, 1)
        self.layout.addWidget(self.answer_b, 2, 1)
        self.layout.addWidget(self.answer_c, 3, 1)
        self.layout.addWidget(self.answer_d, 4, 1)
        self.layout.addWidget(self.answer_e, 5, 1)
        self.layout.addWidget(self.answer_f, 6, 1)
        self.layout.addWidget(self.score_box, 7, 1)
        self.layout.addWidget(self.check, 7, 2)
        self.layout.addWidget(self.reset, 8, 2)
        self.layout.addWidget(self.cancel, 8, 1)
        self.layout.addWidget(self.next, 9, 2)

        self.setLayout(self.layout)

        self.check.clicked.connect(self.check_selected)
        self.reset.clicked.connect(self.reset_selected)
        self.cancel.clicked.connect(self.cancel_selected)

    def check_selected(self):
        pass
    #check answers using algorithms

    def reset_selected(self):
        self.answer_a.setText(None)
        self.answer_b.setText(None)
        self.answer_c.setText(None)
        self.answer_d.setText(None)
        self.answer_e.setText(None)
        self.answer_f.setText(None)
    #answer_a.text = None

    def cancel_selected(self):
        self.close()
    
