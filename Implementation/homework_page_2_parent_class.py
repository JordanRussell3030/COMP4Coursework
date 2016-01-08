from PyQt4.QtCore import *
from PyQt4.QtGui import *
#
from homework_widgets_page_2 import *
from homework_widgets import *

class HomeworkPage2ParentClass(QWidget):
    def __init__(self):
        super().__init__()
        self.showMaximized()

        self.buttons = []

        self.question_2 = QLabel()
        self.question_2.setFont(QFont("Courier", 30))
        self.shape_2 = QLabel()
        self.shape_2.setFont(QFont("Courier", 30))
        self.question_3 = QLabel()
        self.question_3.setFont(QFont("Courier", 30))
        self.shape_3 = QLabel()
        self.shape_3.setFont(QFont("Courier", 30))
        self.question_4 = QLabel()
        self.question_4.setFont(QFont("Courier", 30))
        self.drag_drop = QLabel("Drag and Drop space")
        self.drag_drop.setFont(QFont("Courier", 30))
        
        self.answer_2 = QComboBox() # Add options in each subclass on homework_widgets_page_2
        self.mark_2 = QPushButton("Mark it  |  2") # Swap 2 for number of attempts remaining
        self.answer_3 = QComboBox()
        self.mark_3 = QPushButton("Mark it  |  2")
        self.previous = QPushButton("Previous")
        self.mark_4 = QPushButton("Mark it  |  2")
        self.finish = QPushButton("Finish")

        self.buttons.append(self.mark_2)
        self.buttons.append(self.mark_3)
        self.buttons.append(self.previous)
        self.buttons.append(self.mark_4)
        self.buttons.append(self.finish)

        self.mark_2.setMinimumWidth(60)
        self.mark_2.setMinimumHeight(110)
        self.mark_2.setFont(QFont("Courier", 40))

        self.mark_3.setMinimumWidth(60)
        self.mark_3.setMinimumHeight(110)
        self.mark_3.setFont(QFont("Courier", 40))

        self.previous.setMinimumWidth(60)
        self.previous.setMinimumHeight(110)
        self.previous.setFont(QFont("Courier", 40))

        self.mark_4.setMinimumWidth(60)
        self.mark_4.setMinimumHeight(110)
        self.mark_4.setFont(QFont("Courier", 40))

        self.finish.setMinimumWidth(60)
        self.finish.setMinimumHeight(110)
        self.finish.setFont(QFont("Courier", 40))

        for button in self.buttons:
            self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.answer_2.setMinimumWidth(60)
        self.answer_2.setMinimumHeight(110)
        self.answer_2.setFont(QFont("Courier", 40))
        self.answer_2.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")

        self.answer_3.setMinimumWidth(60)
        self.answer_3.setMinimumHeight(110)
        self.answer_3.setFont(QFont("Courier", 40))
        self.answer_3.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")

        self.layout = QGridLayout()

        self.layout.addWidget(self.question_2, 0, 0)
        self.layout.addWidget(self.shape_2, 1, 0)
        self.layout.addWidget(self.question_3, 3, 0)
        self.layout.addWidget(self.shape_3, 4, 0)
        self.layout.addWidget(self.question_4, 5, 2)
        self.layout.addWidget(self.answer_2, 2, 0)
        self.layout.addWidget(self.mark_2, 2, 1)
        self.layout.addWidget(self.answer_3, 5, 0)
        self.layout.addWidget(self.mark_3, 5, 1)
        self.layout.addWidget(self.previous, 6, 0)
        self.layout.addWidget(self.drag_drop, 0, 2)
        self.layout.addWidget(self.mark_4, 5, 3)
        self.layout.addWidget(self.finish, 6, 3)

        self.setLayout(self.layout)

        self.mark_2.clicked.connect(self.selected_mark_2)
        self.mark_3.clicked.connect(self.selected_mark_3)
        self.mark_4.clicked.connect(self.selected_mark_4)
        self.previous.clicked.connect(self.selected_previous)
        self.finish.clicked.connect(self.selected_finish)

    def selected_mark_2(self):
        pass
    #mark question 2 if answer == algorithm mark += 1

    def selected_mark_3(self):
        pass

    def selected_mark_4(self):
        pass

##    def selected_previous(self):
##        self.close()

    def selected_finish(self):
        self.close()
        #save all answer to database
