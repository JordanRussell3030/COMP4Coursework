from PyQt4.QtCore import *
from PyQt4.QtGui import *

from homework_widgets_page_2 import *
from homework_widgets import *
from error_messages import *
from homework_parent_class import *
from homework_widgets import *

class HomeworkPage2ParentClass(QWidget):
    def __init__(self, parent = None):
        super().__init__()
        self.parent = parent

        self.task = "Sides Easy"
        
        self.showMaximized()

        self._button_1 = QPushButton()
        self._button_2 = QPushButton()
        self._button_3 = QPushButton()
        self._button_4 = QPushButton()
        self._button_5 = QPushButton()
        self._button_6 = QPushButton()

        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

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
        
        self.answer_2 = QComboBox()
        self.mark_2 = QPushButton("Mark it  |  2")
        self.answer_3 = QComboBox()
        self.mark_3 = QPushButton("Mark it  |  2")
        self.previous = QPushButton("Previous")
##        self.mark_4 = QPushButton("Mark it  |  2")
##        self.answer_4 = QLineEdit()
        self.finish = QPushButton("Finish")

        self.mark_2.setMinimumWidth(60)
        self.mark_2.setMinimumHeight(110)
        self.mark_2.setFont(QFont("Courier", 40))

        self.mark_3.setMinimumWidth(60)
        self.mark_3.setMinimumHeight(110)
        self.mark_3.setFont(QFont("Courier", 40))

        self.previous.setMinimumWidth(60)
        self.previous.setMinimumHeight(110)
        self.previous.setFont(QFont("Courier", 40))

##        self.mark_4.setMinimumWidth(60)
##        self.mark_4.setMinimumHeight(110)
##        self.mark_4.setFont(QFont("Courier", 40))

        self.finish.setMinimumWidth(60)
        self.finish.setMinimumHeight(110)
        self.finish.setFont(QFont("Courier", 40))

        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        self.answer_2.setMinimumWidth(60)
        self.answer_2.setMinimumHeight(110)
        self.answer_2.setFont(QFont("Courier", 40))
        self.answer_2.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")

        self.answer_3.setMinimumWidth(60)
        self.answer_3.setMinimumHeight(110)
        self.answer_3.setFont(QFont("Courier", 40))
        self.answer_3.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")

##        self.answer_4.setMinimumWidth(60)
##        self.answer_4.setMinimumHeight(110)
##        self.answer_4.setFont(QFont("Courier", 40))
##        self.answer_4.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue;}")

        self.layout = QGridLayout()

        self.answer_question_4 = None

        self._button_1.setMaximumWidth(60)
        self._button_1.setMaximumHeight(60)
        self._button_1.setMinimumWidth(60)
        self._button_1.setMinimumHeight(60)

        self._button_2.setMaximumWidth(60)
        self._button_2.setMaximumHeight(60)
        self._button_2.setMinimumWidth(60)
        self._button_2.setMinimumHeight(60)

        self._button_3.setMaximumWidth(60)
        self._button_3.setMaximumHeight(60)
        self._button_3.setMinimumWidth(60)
        self._button_3.setMinimumHeight(60)

        self._button_4.setMaximumWidth(60)
        self._button_4.setMaximumHeight(60)
        self._button_4.setMinimumWidth(60)
        self._button_4.setMinimumHeight(60)

        self._button_5.setMaximumWidth(60)
        self._button_5.setMaximumHeight(60)
        self._button_5.setMinimumWidth(60)
        self._button_5.setMinimumHeight(60)

        self._button_6.setMaximumWidth(60)
        self._button_6.setMaximumHeight(60)
        self._button_6.setMinimumWidth(60)
        self._button_6.setMinimumHeight(60)

        self.attempts_button = QPushButton("3 Attempts left")
        self.attempts_button.setEnabled(False)

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
##        self.layout.addWidget(self.mark_4, 5, 3)
##        self.layout.addWidget(self.answer_4, 6, 3)
        self.layout.addWidget(self.finish, 7, 3)
        self.layout.addWidget(self._button_1, 2, 2)
        self.layout.addWidget(self._button_2, 2, 3)
        self.layout.addWidget(self._button_3, 2, 4)
        self.layout.addWidget(self._button_4, 3, 2)
        self.layout.addWidget(self._button_5, 3, 3)
        self.layout.addWidget(self._button_6, 3, 4)
        self.layout.addWidget(self.attempts_button, 4, 3)

        self.setLayout(self.layout)

        self.mark_2.clicked.connect(self.selected_mark_2)
        self.mark_3.clicked.connect(self.selected_mark_3)
##        self.mark_4.clicked.connect(self.selected_mark_4)
        self.previous.clicked.connect(self.selected_previous)
        self.finish.clicked.connect(self.selected_finish)
        self._button_1.clicked.connect(self.check_button_1)
        self._button_2.clicked.connect(self.check_button_2)
        self._button_3.clicked.connect(self.check_button_3)
        self._button_4.clicked.connect(self.check_button_4)
        self._button_5.clicked.connect(self.check_button_5)
        self._button_6.clicked.connect(self.check_button_6)

        self.attempts_remaining_a = 2
        self.attempts_remaining_b = 2
        self.attempts_remaining_c = 3
        self.correct_count_2 = 0
        self.correct_count_3 = 0
        self.correct_count_4 = 0

    def check_button_1(self, attempts_remaining_c):
        if self._button_1.text() == self.answer_question_4:
            self._button_1.setText("Correct")
            self._button_1.setEnabled(False)
            self._button_2.setEnabled(False)
            self._button_3.setEnabled(False)
            self._button_4.setEnabled(False)
            self._button_5.setEnabled(False)
            self._button_6.setEnabled(False)
            self.attempts_button.setText("1 mark!")
            self.correct_count_4 += 1
        else:
            self._button_1.setText("Incorrect")
            self._button_1.setEnabled(False)
            self.attempts_remaining_c -= 1
            self.attempts_button.setText("{0} attempts remaining".format(self.attempts_remaining_c))
            if self.attempts_remaining_c == 0:
                self._button_1.setEnabled(False)
                self._button_2.setEnabled(False)
                self._button_3.setEnabled(False)
                self._button_4.setEnabled(False)
                self._button_5.setEnabled(False)
                self._button_6.setEnabled(False)
                self.attempts_button.setText("No more attempts")
            return self.attempts_remaining_c

    def check_button_2(self, attempts_remaining_c):
        if self._button_2.text() == self.answer_question_4:
            self._button_2.setText("Correct")
            self._button_1.setEnabled(False)
            self._button_2.setEnabled(False)
            self._button_3.setEnabled(False)
            self._button_4.setEnabled(False)
            self._button_5.setEnabled(False)
            self._button_6.setEnabled(False)
            self.attempts_button.setText("1 mark!")
            self.correct_count_4 += 1
        else:
            self._button_2.setText("Incorrect")
            self._button_2.setEnabled(False)
            self.attempts_remaining_c -= 1
            self.attempts_button.setText("{0} attempts remaining".format(self.attempts_remaining_c))
            if self.attempts_remaining_c == 0:
                self._button_1.setEnabled(False)
                self._button_2.setEnabled(False)
                self._button_3.setEnabled(False)
                self._button_4.setEnabled(False)
                self._button_5.setEnabled(False)
                self._button_6.setEnabled(False)
                self.attempts_button.setText("No more attempts")
            return self.attempts_remaining_c
                
    def check_button_3(self, attempts_remaining_c):
        if self._button_3.text() == self.answer_question_4:
            self._button_3.setText("Correct")
            self._button_1.setEnabled(False)
            self._button_2.setEnabled(False)
            self._button_3.setEnabled(False)
            self._button_4.setEnabled(False)
            self._button_5.setEnabled(False)
            self._button_6.setEnabled(False)
            self.attempts_button.setText("1 mark!")
            self.correct_count_4 += 1
        else:
            self._button_3.setText("Incorrect")
            self._button_3.setEnabled(False)
            self.attempts_remaining_c -= 1
            self.attempts_button.setText("{0} attempts remaining".format(self.attempts_remaining_c))
            if self.attempts_remaining_c == 0:
                self._button_1.setEnabled(False)
                self._button_2.setEnabled(False)
                self._button_3.setEnabled(False)
                self._button_4.setEnabled(False)
                self._button_5.setEnabled(False)
                self._button_6.setEnabled(False)
                self.attempts_button.setText("No more attempts")
            return self.attempts_remaining_c
                
    def check_button_4(self, attempts_remaining_c):
        if self._button_4.text() == self.answer_question_4:
            self._button_4.setText("Correct")
            self._button_1.setEnabled(False)
            self._button_2.setEnabled(False)
            self._button_3.setEnabled(False)
            self._button_4.setEnabled(False)
            self._button_5.setEnabled(False)
            self._button_6.setEnabled(False)
            self.attempts_button.setText("1 mark!")
            self.correct_count_4 += 1
        else:
            self._button_4.setText("Incorrect")
            self._button_4.setEnabled(False)
            self.attempts_remaining_c -= 1
            self.attempts_button.setText("{0} attempts remaining".format(self.attempts_remaining_c))
            if self.attempts_remaining_c == 0:
                self._button_1.setEnabled(False)
                self._button_2.setEnabled(False)
                self._button_3.setEnabled(False)
                self._button_4.setEnabled(False)
                self._button_5.setEnabled(False)
                self._button_6.setEnabled(False)
                self.attempts_button.setText("No more attempts")
            return self.attempts_remaining_c
                
    def check_button_5(self, attempts_remaining_c):
        if self._button_5.text() == self.answer_question_4:
            self._button_5.setText("Correct")
            self._button_1.setEnabled(False)
            self._button_2.setEnabled(False)
            self._button_3.setEnabled(False)
            self._button_4.setEnabled(False)
            self._button_5.setEnabled(False)
            self._button_6.setEnabled(False)
            self.attempts_button.setText("1 mark!")
            self.correct_count_4 += 1
        else:
            self._button_5.setText("Incorrect")
            self._button_5.setEnabled(False)
            self.attempts_remaining_c -= 1
            self.attempts_button.setText("{0} attempts remaining".format(self.attempts_remaining_c))
            if self.attempts_remaining_c == 0:
                self._button_1.setEnabled(False)
                self._button_2.setEnabled(False)
                self._button_3.setEnabled(False)
                self._button_4.setEnabled(False)
                self._button_5.setEnabled(False)
                self._button_6.setEnabled(False)
                self.attempts_button.setText("No more attempts")
            return self.attempts_remaining_c
                
    def check_button_6(self, attempts_remaining_c):
        if self._button_6.text() == self.answer_question_4:
            self._button_6.setText("Correct")
            self._button_1.setEnabled(False)
            self._button_2.setEnabled(False)
            self._button_3.setEnabled(False)
            self._button_4.setEnabled(False)
            self._button_5.setEnabled(False)
            self._button_6.setEnabled(False)
            self.attempts_button.setText("1 mark!")
            self.correct_count_4 += 1
        else:
            self._button_6.setText("Incorrect")
            self._button_6.setEnabled(False)
            self.attempts_remaining_c -= 1
            self.attempts_button.setText("{0} attempts remaining".format(self.attempts_remaining_c))
            if self.attempts_remaining_c == 0:
                self._button_1.setEnabled(False)
                self._button_2.setEnabled(False)
                self._button_3.setEnabled(False)
                self._button_4.setEnabled(False)
                self._button_5.setEnabled(False)
                self._button_6.setEnabled(False)
                self.attempts_button.setText("No more attempts")
            return self.attempts_remaining_c

    def selected_mark_2(self, attempts_remaining_a):
        if self.answer_2.currentText() == "20":
            self.correct_count_2 += 1
            self.mark_2.setText(" Correct!  ")
            self.mark_2.setEnabled(False)
            self.answer_2.setEnabled(False)
        else:
            self.attempts_remaining_a -= 1
            self.mark_2.setText("Mark it|{0}".format(self.attempts_remaining_a))
            if self.attempts_remaining_a == 0:
                self.mark_2.setEnabled(False)
                self.answer_2.setEnabled(False)
            error_message = ErrorMessage5()
            error_message.show()
            error_message._raise()
        return self.attempts_remaining_a, self.correct_count_2
                                         
    def selected_mark_3(self, attempts_remaining_b):
        if self.answer_3.currentText() == "20":
            self.correct_count_3 += 1
            self.mark_3.setText(" Correct!")
            self.mark_3.setEnabled(False)
            self.answer_3.setEnabled(False)
        else:
            self.attempts_remaining_b -= 1
            self.mark_3.setText("Mark it|{0}".format(self.attempts_remaining_b))
            if self.attempts_remaining_b == 0:
                self.mark_3.setEnabled(False)
                self.answer_3.setEnabled(False)
            error_message = ErrorMessage5()
            error_message.show()
            error_message._raise()
        return self.attempts_remaining_b, self.correct_count_3

##    def selected_mark_4(self, attempts_remaining_c):
##        if self.answer_4.text() == "20":
##            self.correct_count_4 += 1
##            self.mark_4.setText(" Correct!")
##            self.mark_4.setEnabled(False)
##            self.answer_4.setEnabled(False)
##        else:
##            self.attempts_remaining_c -= 1
##            self.mark_4.setText("Mark it|{0}".format(self.attempts_remaining_c))
##            if self.attempts_remaining_c == 0:
##                self.mark_4.setEnabled(False)
##                self.answer_4.setEnabled(False)
##            error_message = ErrorMessage5()
##            error_message.show()
##            error_message._raise()
##        return self.attempts_remaining_c, self.correct_count_4

    def selected_previous(self):
        self.parent.stack.setCurrentIndex(0)

    def selected_finish(self): #correct_count?
##        total_score = self.correct_count_2 + self.correct_count_3 + self.correct_count_4
##        total_temp = self.correct_count_2 + self.correct_count_3 + self.correct_count_4
##        total_percent = (100 / 3) * total_temp
##        if total_percent == 99.9:
##            total = 100
##        else:
##            total = round(total_percent, 1)
##        print(total)
##        print(self.correct_count_2)
##        print(self.correct_count_3)
##        print(self.correct_count_4)
        g_database.insert_data_second(self.task, self.correct_count_2, self.correct_count_3, self.correct_count_4)  
        self.parent.close()
