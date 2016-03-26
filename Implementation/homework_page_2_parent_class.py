from PyQt4.QtCore import *
from PyQt4.QtGui import *

import random

from database_class import * #This contains the methods used to add to the database
from error_messages import * #This contains the default error message classes used when the user makes an error

#This is the template for the parent class which all 24 child classes inherit their default attributes from
class HomeworkPage2ParentClass(QWidget):
    #Constructor
    def __init__(self, parent = None):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This is the parent variable which allows the child classes to inherit the connections to the second widget in the stacks
        self.parent = parent

        #This is overridden in each child class so the user will know which task goes with the score
        self.task = ""

        #This maximises the screen - each child class will be maximised when opened
        self.showMaximized()

        #This sets the background colour of each child class to white
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #These 6 buttons are used in every child class, so they are created here - they
        #are always the same size and have the same style (overridden from the style of the other buttons)
        #They are the multiple choice buttons for question 4
        self._button_1 = QPushButton()
        #Sets the size of the buttons so they fit in amongst the many other widgets
        self._button_1.setMaximumWidth(200)
        self._button_1.setMinimumWidth(110)
        self._button_1.setMinimumHeight(110)
        #Sets the background colour and font colour of the button - override from the style sheet of the whole widget
        self._button_1.setStyleSheet("QPushButton {background-color: white; font-color: black;}")
        
        self._button_2 = QPushButton()
        self._button_2.setMaximumWidth(200)
        self._button_2.setMinimumWidth(110)
        self._button_2.setMinimumHeight(110)
        self._button_2.setStyleSheet("QPushButton {background-color: white; font-color: black;}")
  
        self._button_3 = QPushButton()
        self._button_3.setMaximumWidth(200)
        self._button_3.setMinimumWidth(110)
        self._button_3.setMinimumHeight(110)
        self._button_3.setStyleSheet("QPushButton {background-color: white; font-color: black;}")
        
        self._button_4 = QPushButton()
        self._button_4.setMaximumWidth(200)
        self._button_4.setMinimumWidth(110)
        self._button_4.setMinimumHeight(110)
        self._button_4.setStyleSheet("QPushButton {background-color: white; font-color: black;}")
        
        self._button_5 = QPushButton()
        self._button_5.setMaximumWidth(200)
        self._button_5.setMinimumWidth(110)
        self._button_5.setMinimumHeight(110)
        self._button_5.setStyleSheet("QPushButton {background-color: white; font-color: black;}")
        
        self._button_6 = QPushButton()
        self._button_6.setMaximumWidth(200)
        self._button_6.setMinimumWidth(110)
        self._button_6.setMinimumHeight(110)
        self._button_6.setStyleSheet("QPushButton {background-color: white; font-color: black;}")

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

        #This is the combo box which provides the value to check to see if the input for the answer is right or not
        self.answer_2 = QComboBox()
        self.answer_2.setMinimumWidth(60)
        self.answer_2.setMinimumHeight(110)
        self.answer_2.setFont(QFont("Courier", 40))
        self.answer_2.setStyleSheet("QComboBox {background-color: lavender; color: purple;}")

        #This button is connected to the method to check if the contents of the above combo box is right or not
        self.mark_2 = QPushButton("Mark it  |  2")
        self.mark_2.setMinimumWidth(60)
        self.mark_2.setMinimumHeight(110)
        self.mark_2.setFont(QFont("Courier", 40))
        self.mark_2.setStyleSheet("QPushButton {background-color: yellow; color: black; font-size: 20;}")
        
        self.answer_3 = QComboBox()
        self.answer_3.setMinimumWidth(60)
        self.answer_3.setMinimumHeight(110)
        self.answer_3.setFont(QFont("Courier", 40))
        self.answer_3.setStyleSheet("QComboBox {background-color: lavender; color: purple;}")
        
        self.mark_3 = QPushButton("Mark it  |  2")
        self.mark_3.setMinimumWidth(60)
        self.mark_3.setMinimumHeight(110)
        self.mark_3.setFont(QFont("Courier", 40))
        self.mark_3.setStyleSheet("QPushButton {background-color: yellow; color: black; font-size: 20;}")

        #Switches to the first widget in the stack
        self.previous = QPushButton("Previous")
        self.previous.setMinimumWidth(60)
        self.previous.setMinimumHeight(110)
        self.previous.setFont(QFont("Courier", 40))
        self.previous.setStyleSheet("QPushButton {background-color: red; color: white; font-size: 20;}")

        #Close the stack
        self.finish = QPushButton("Finish")
        self.finish.setMinimumWidth(60)
        self.finish.setMinimumHeight(110)
        self.finish.setFont(QFont("Courier", 40))
        self.finish.setStyleSheet("QPushButton {background-color: green; color: white; font-size: 20;}")

        #Tells the user how many attempts they have left at question 4
        self.attempts_button = QPushButton("3 Attempts left")
        self.attempts_button.setMinimumHeight(60)
        self.attempts_button.setMinimumWidth(90)
        self.attempts_button.setMaximumWidth(200)
        self.attempts_button.setStyleSheet("QPushButton {background-color: white; font-color: black;}")
        self.attempts_button.setEnabled(False)          

        #Sets the layout to a QGridLayout so the widgets can be positioned easily
        self.layout = QGridLayout()

        #Adds all of the widgets to the layout
        self.layout.addWidget(self.question_2, 0, 0)
        self.layout.addWidget(self.shape_2, 0, 1)
        self.layout.addWidget(self.answer_2, 1, 0)
        self.layout.addWidget(self.mark_2, 1, 1)
        self.layout.addWidget(self._button_1, 1, 2)
        self.layout.addWidget(self._button_2, 1, 3)
        self.layout.addWidget(self._button_3, 2, 2)
        self.layout.addWidget(self.question_3, 2, 0)
        self.layout.addWidget(self._button_4, 2, 3)
        self.layout.addWidget(self._button_5, 3, 2)
        self.layout.addWidget(self._button_6, 3, 3)
        self.layout.addWidget(self.shape_3, 2, 1)
        self.layout.addWidget(self.attempts_button, 4, 2)
        self.layout.addWidget(self.answer_3, 3, 0)
        self.layout.addWidget(self.mark_3, 3, 1)
        self.layout.addWidget(self.question_4, 0, 2)
        self.layout.addWidget(self.previous, 5, 0)
        self.layout.addWidget(self.finish, 5, 3)

        #Sets layout as the layout to be used in the window
        self.setLayout(self.layout)

        #All of the connections for checking the inputs and navigating the stack
        self.mark_2.clicked.connect(self.selected_mark_2)
        self.mark_3.clicked.connect(self.selected_mark_3)
        self.previous.clicked.connect(self.selected_previous)
        self.finish.clicked.connect(self.selected_finish)
        self._button_1.clicked.connect(self.check_button_1)
        self._button_2.clicked.connect(self.check_button_2)
        self._button_3.clicked.connect(self.check_button_3)
        self._button_4.clicked.connect(self.check_button_4)
        self._button_5.clicked.connect(self.check_button_5)
        self._button_6.clicked.connect(self.check_button_6)

        #The variables used to measure how many attempts the user has for each question, so the sytem knows when to disable the appropriate buttons
        self.attempts_remaining_a = 2
        self.attempts_remaining_b = 2
        self.attempts_remaining_c = 3
        #These are the counts which represent the number of marks the user has, and these values are saved in the database
        self.correct_count_2 = 0
        self.correct_count_3 = 0
        self.correct_count_4 = 0
        #This is overridden in each child class - it is the value to check the multiple choice buttons answer against
        self.answer_question_4 = None

    #These are the methods to check if the selected button is the correct button for question 4
    def check_button_1(self, attempts_remaining_c):
        #Resets the correct count so that it doesn't increment across tasks
        self.correct_count_4 = 0
        #The value to check is taken from the text on the QPushButton
        #If it is the same then the user is awarded a mark and all of the buttons are disabled so they can't keep changing the answer and clicking aimlessly,
        #or risk crashing the program
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
        #If they are wrong then an attempt is removed and the button they clicked is disabled so they can't waste an attempt when they know it's wrong
        else:
            self._button_1.setText("Incorrect")
            self._button_1.setEnabled(False)
            self.attempts_remaining_c -= 1
            #Changes the text of the mark it button so the user knows how many attempts they have left
            self.attempts_button.setText("{0} attempts remaining".format(self.attempts_remaining_c))
            #If they have used all of their attempts all of the buttons are disabled and they cannot do anything more with this question
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
        self.correct_count_4 = 0
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
        self.correct_count_4 = 0
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
        self.correct_count_4 = 0
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
        self.correct_count_4 = 0
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
        self.correct_count_4 = 0
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

    #These check the input in the combo boxes for questions 2 and 3 to see if the user is correct
    def selected_mark_2(self, attempts_remaining_a):
        #Resets the correct count so that it doesn't increment across tasks
        self.correct_count_2 = 0
        #Takes the value to be checked from the content of the combo box and compares it to the hard-coded answer
        if self.answer_2.currentText() == "20":
            #If they are right they are awarded marks and the buttons are disabled as they have no further need of them (they can't get the same marks twice)
            self.correct_count_2 += 1
            self.mark_2.setText("Correct!")
            self.mark_2.setEnabled(False)
            self.answer_2.setEnabled(False)
        else:
            #If they are wrong they lose an attempt until they have none left
            self.attempts_remaining_a -= 1
            self.mark_2.setText("Mark it|{0}".format(self.attempts_remaining_a))
            if self.attempts_remaining_a == 0:
                #When they run out of attempts everything is disabled so they cannot continue with the question
                self.mark_2.setEnabled(False)
                self.answer_2.setEnabled(False)
            #This error message informs the user that they are wrong
            error_message = ErrorMessage5()
            error_message.show()
            error_message._raise()
        #Returns the attempts remaining so that it isn't reset every time the method is run, and the correct_count to be saved to the database
        return self.attempts_remaining_a, self.correct_count_2
                                         
    def selected_mark_3(self, attempts_remaining_b):
        self.correct_count_3 = 0
        if self.answer_3.currentText() == "20":
            self.correct_count_3 += 1
            self.mark_3.setText("Correct!")
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

    def selected_previous(self):
        #Switches to the first screen in the stack
        self.parent.stack.setCurrentIndex(0)

    def selected_finish(self):
        #This checks to see whether or not all of the answers have been given
        if self.attempts_button.text() != "1 mark!" and self.attempts_button.text() != "No more attempts":
            error_message_2 = ErrorMessage8()
            error_message_2.show()
            error_message_2._raise()
        elif self.mark_2.text() != "Correct!" and self.mark_2.text() != "Mark it|0":
            error_message_2 = ErrorMessage8()
            error_message_2.show()
            error_message_2._raise()
        elif self.mark_3.text() != "Correct!" and self.mark_3.text() != "Mark it|0":
            error_message_2 = ErrorMessage8()
            error_message_2.show()
            error_message_2._raise()
        else:
            #This method is in the database class and it updates all of the pre-recorded 0 values in the record for this task with the actual scores
            g_database.insert_data_second(self.task, self.correct_count_2, self.correct_count_3, self.correct_count_4)
            #Closes the stack widget
            self.parent.close()
