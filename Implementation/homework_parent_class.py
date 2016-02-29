from PyQt4.QtCore import * #These two lines import the built in PyQt code
from PyQt4.QtGui import *

from database_class import * #Contains all of the methods required to manipulate the database
from error_messages import * #Contains all of the error message classes for when the user makes a mistake

#The parent template for the first page of all homeworks - all homework child classes inherit their default attributes from here
class ParentHomeworkPage1Class(QWidget):
    #Constructor
    def __init__(self, parent = None):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #This is the parent variable which allows the child classes to inherit the connections to the second widget in the stacks
        self.parent = parent
        
        #This maximises the screen
        self.showMaximized()

        #This variable is overridden in each child class - it is the task name string value which is stored in the database
        self.task = ""

        #Decides whether or not the user has actually submitted answers to question 1
        #and authorises access to the next page
        self.allow_cont = False

        #Sets the background colour of each child window to white
        pal = QPalette()
        pal.setColor(QPalette.Background, Qt.white)
        self.setAutoFillBackground(True)
        self.setPalette(pal)     

        #All of these buttons appear in all of the child classes - they are created here then the text is set in the child classesso htey can all be different
        self.next = QPushButton("Next")
        #Sets the size of the button
        self.next.setMinimumHeight(110)
        self.next.setMinimumWidth(60)
        #Sets the font size and house style of the text in the button
        self.next.setFont(QFont("Courier", 40))

        self.cancel = QPushButton("Cancel")
        self.cancel.setMinimumHeight(110)
        self.cancel.setMinimumWidth(60)
        self.cancel.setFont(QFont("Courier", 40))
        self.cancel.setStyleSheet("QPushButton {background-color: red; color: white; font-size: 20;}")
        
        self.check = QPushButton("Check Answers")
        self.check.setMinimumHeight(110)
        self.check.setMinimumWidth(60)
        self.check.setFont(QFont("Courier", 40))
        self.check.setStyleSheet("QPushButton {background-color: yellow; color: black; font-size: 20;}")
        
        self.reset = QPushButton("Reset Answers")
        self.reset.setMinimumHeight(110)
        self.reset.setMinimumWidth(60)
        self.reset.setFont(QFont("Courier", 40))
        self.reset.setStyleSheet("QPushButton {background-color: yellow; color: black; font-size: 20;}")

        self.title = QLabel()
        self.title.setFont(QFont("Courier", 40))

        self.question_1 = QLabel()
        self.question_1.setFont(QFont("Courier", 20))

        self.question_1_shape = QLabel()
        self.question_1_shape.setFont(QFont("Courier", 40))
        
        self.answer_a = QLineEdit()
        self.answer_a.setMinimumHeight(70)
        self.answer_a.setMinimumWidth(60)
        self.answer_a.setFont(QFont("Courier", 30))
        
        self.answer_b = QLineEdit()
        self.answer_b.setMinimumHeight(70)
        self.answer_b.setMinimumWidth(60)
        self.answer_b.setFont(QFont("Courier", 30))
        
        self.answer_c = QLineEdit()
        self.answer_c.setMinimumHeight(70)
        self.answer_c.setMinimumWidth(60)
        self.answer_c.setFont(QFont("Courier", 30))
        
        self.answer_d = QLineEdit()
        self.answer_d.setMinimumHeight(70)
        self.answer_d.setMinimumWidth(60)
        self.answer_d.setFont(QFont("Courier", 30))
        
        self.answer_e = QLineEdit()
        self.answer_e.setMinimumHeight(70)
        self.answer_e.setMinimumWidth(60)
        self.answer_e.setFont(QFont("Courier", 30))
        
        self.answer_f = QLineEdit()
        self.answer_f.setMinimumHeight(70)
        self.answer_f.setMinimumWidth(60)
        self.answer_f.setFont(QFont("Courier", 30))

        self.q1a = QLabel("")
        self.q1a.setFont(QFont("Courier", 20))
        
        self.q1b = QLabel("")
        self.q1b.setFont(QFont("Courier", 20))
        
        self.q1c = QLabel("")
        self.q1c.setFont(QFont("Courier", 20))
        
        self.q1d = QLabel("")
        self.q1d.setFont(QFont("Courier", 20))
        
        self.q1e = QLabel("")
        self.q1e.setFont(QFont("Courier", 20))
        
        self.q1f = QLabel("")
        self.q1f.setFont(QFont("Courier", 20))
        
        self.score_box = QLabel("Score: X/X")
        self.score_box.setFont(QFont("Courier", 30))

        #Sets the background colour and font colour of all the buttons in each child window
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        #Sets the layout of the window to a QGridLayout so the widgets can all be positioned easily
        self.layout = QGridLayout()

        #These add all of the widgets to the layout
        self.layout.addWidget(self.title, 0, 0) #These numbers position the widgets in the window
        self.layout.addWidget(self.question_1, 1, 0)
        self.layout.addWidget(self.q1a, 1, 1)
        self.layout.addWidget(self.reset, 1, 2)
        self.layout.addWidget(self.question_1_shape, 2, 0)
        self.layout.addWidget(self.answer_a, 2, 1)
        self.layout.addWidget(self.q1b, 3, 1)
        self.layout.addWidget(self.answer_b, 4, 1)
        self.layout.addWidget(self.q1c, 5, 1)
        self.layout.addWidget(self.answer_c, 6, 1)
        self.layout.addWidget(self.q1d, 7, 1)
        self.layout.addWidget(self.answer_d, 8, 1)
        self.layout.addWidget(self.q1e, 9, 1)
        self.layout.addWidget(self.answer_e, 10, 1)
        self.layout.addWidget(self.q1f, 11, 1)
        self.layout.addWidget(self.answer_f, 12, 1)
        self.layout.addWidget(self.cancel, 13, 0)
        self.layout.addWidget(self.check, 13, 1)
        self.layout.addWidget(self.next, 13, 2)

        #Sets layout as the layout to be used
        self.setLayout(self.layout)

        #The connections for the buttons which have the same purpose in each child class - some will be in the child classes if they have any unique purposes
        self.check.clicked.connect(self.check_selected)
        self.reset.clicked.connect(self.reset_selected)
        self.cancel.clicked.connect(self.cancel_selected)
        self.next.clicked.connect(self.next_selected)

        #Adds each answer to a list so that whenever each of the 6 variables needs the same thing to happen to them only 1 line
        #of code in a for loop is needed rather than 6 lines on their own
        self.answers = []
        self.answers.append(self.answer_a)
        self.answers.append(self.answer_b)
        self.answers.append(self.answer_c)
        self.answers.append(self.answer_d)
        self.answers.append(self.answer_e)
        self.answers.append(self.answer_f)

    #This method checks the contents of all 6 line edits to see if the user's answers are correct
    def check_selected(self):
        #Sets the correct count to 0 so that it is reset if the user does more than 1 homework in one sitting
        #The buttons are disabled so they cannot reset the score after completing the question
        self.allow_cont = False
        self.correct_count = 0
##        raise Exception("Need to override check_selected from ParentHomeworkPage1Class")
        #For each line edit, if the user's answer is the same as the hard-coded correct answer then they get a mark
        if self.answer_a.text() == self.answer_1_a:
            self.answer_a.setText("{0} Correct".format(self.answer_a.text()))
            self.correct_count += 1
        #If they are wrong they are told they are wrong
        else:
            self.answer_a.setText("Incorrect")
        if self.answer_b.text() == self.answer_1_b:
            self.answer_b.setText("{0} Correct".format(self.answer_b.text()))
            self.correct_count += 1
        else:
            self.answer_b.setText("Incorrect")
        if self.answer_c.text() == self.answer_1_c:
            self.answer_c.setText("{0} Correct".format(self.answer_c.text()))
            self.correct_count += 1
        else:
            self.answer_c.setText("Incorrect")
        if self.answer_d.text() == self.answer_1_d:
            self.answer_d.setText("{0} Correct".format(self.answer_d.text()))
            self.correct_count += 1
        else:
            self.answer_d.setText("Incorrect")
        if self.answer_e.text() == self.answer_1_e:
            self.answer_e.setText("{0} Correct".format(self.answer_e.text()))
            self.correct_count += 1
        else:
            self.answer_e.setText("Incorrect")
        if self.answer_f.text() == self.answer_1_f:
            self.answer_f.setText("{0} Correct".format(self.answer_f.text()))
            self.correct_count += 1
        else:
            self.answer_f.setText("Incorrect")
        #When all answers have been checked all of the line edits, the check button and the reset button are disabled to they have to accept their score
        for a in self.answers:
            a.setReadOnly(True)
        self.check.setEnabled(False)
        self.reset.setEnabled(False)
        #Allows the program to continue to page 2
        self.allow_cont = True

    #This method switches to the second screen in the stack after checking that the question has been answered and saving the score to the database
    def next_selected(self):
        #if cont is false then a question has been missed
        cont = False
        while not cont:
            #Checks to see if any answer has been put in the line edit
            for a in self.answers:
                #If the text is blank then it has been missed
                if a.text() == "":
                    #Displays an error message asking the user to enter a value
                    error_message = ErrorMessage8()
                    error_message.show()
                    error_message._raise()
                    cont = False
            #If all of the answers have been entered the correct count is saved to the database and the second page is set to the top of the stack
            cont = True
            if self.allow_cont:
                g_database.insert_data_first(self.task, self.correct_count)
                self.open_page_2()
                self.hide()
            else:
                error_message_2 = ErrorMessage8()
                error_message_2.show()
                error_message_2._raise()

    #Resets all of the answers in the line edits immediately rather than the user deleting each wrong answer individually, before they check the answers
    def reset_selected(self):
        self.answer_a.setText(None)
        self.answer_b.setText(None)
        self.answer_c.setText(None)
        self.answer_d.setText(None)
        self.answer_e.setText(None)
        self.answer_f.setText(None)

    #Closes the stack widget and returns the user to the homework menu
    def cancel_selected(self):
        self.parent.close()

    #Switches to the second window in the stack
    def open_page_2(self):
        self.parent.stack.setCurrentIndex(1)
