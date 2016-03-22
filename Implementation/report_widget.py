from PyQt4.QtGui import * #These two lines import all of the built in PyQt code
from PyQt4.QtCore import *

from database_widget import * #This contains the data currently being displayed to the user
from database_class import * #This contains the methods which fetch the information from the database

#This is the template for the widget which is used to query the database
class ReportWidget(QWidget):
    #Constructor
    def __init__(self):
        #Return a proxy object that delegates method calls to a parent or sibling class of type.
        super().__init__()

        #Maximises the screen
        self.showMaximized()

        #These four lines of code make the background of the widget white
        pal = QPalette()
        #Sets the chosen colour to white
        pal.setColor(QPalette.Background, Qt.white)
        #The screen will automatically be filled with the chosen colour
        self.setAutoFillBackground(True)
        self.setPalette(pal)

        #This is just a label with the title of the window
        self.header = QLabel("Report")
        #Sets the font size and house style of the label
        self.header.setFont(QFont("Courier", 30))

        self.task_box_label = QLabel("Please select a task\nto query: ")
        self.task_box_label.setFont(QFont("Courier", 25))

        #This combo box contains all of the options which can be chosen from when
        #querying the database for a task name
        self.task_box = QComboBox()
        #Sets the size of the combo box
        self.task_box.setMinimumWidth(60)
        self.task_box.setMinimumHeight(100)
        #Sets the font size and house style of the text in the combo box
        self.task_box.setFont(QFont("Courier", 30))
        #Sets the background colour of the combo box
        self.task_box.setStyleSheet("QComboBox {background-color: lavender; color: purple;}")
        #Adds the data which can be queried as options
        self.task_box.addItem("")
        self.task_box.addItem("Sides Easy")
        self.task_box.addItem("Sides Medium")
        self.task_box.addItem("Sides Hard")
        self.task_box.addItem("SOHCAHTOA Easy")
        self.task_box.addItem("SOHCAHTOA Medium")
        self.task_box.addItem("SOHCAHTOA Hard")
        self.task_box.addItem("Finding Angles Easy")
        self.task_box.addItem("Finding Angles Medium")
        self.task_box.addItem("Finding Angles Hard")
        self.task_box.addItem("3D Trigonometry Easy")
        self.task_box.addItem("3D Trigonometry Medium")
        self.task_box.addItem("3D Trigonometry Hard")
        self.task_box.addItem("Pythagoras' Theorem Easy")
        self.task_box.addItem("Pythagoras' Theorem Medium")
        self.task_box.addItem("Pythagoras' Theorem Hard")
        self.task_box.addItem("3D Pythagoras Easy")
        self.task_box.addItem("3D Pythagoras Medium")
        self.task_box.addItem("3D Pythagoras Hard")
        self.task_box.addItem("Vectors Easy")
        self.task_box.addItem("Vectors Medium")
        self.task_box.addItem("Vectors Hard")
        self.task_box.addItem("Easy Summary")
        self.task_box.addItem("Medium Summary")
        self.task_box.addItem("Hard Summary")
        
        self.score_box_label = QLabel("Please input the maximum\nscore you would like\nto query: ")
        self.score_box_label.setFont(QFont("Courier", 25))

        #Essentially the same as the other combo box except with score ranges to select from
        self.score_box = QComboBox()
        self.score_box.setMinimumWidth(60)
        self.score_box.setMinimumHeight(100)
        self.score_box.setFont(QFont("Courier", 30))
        self.score_box.setStyleSheet("QComboBox {background-color: lavender; color: purple;}")
        self.score_box.addItem(None)
        self.score_box.addItem("6")
        self.score_box.addItem("5")
        self.score_box.addItem("4")
        self.score_box.addItem("3")
        self.score_box.addItem("2")
        self.score_box.addItem("1")
        self.score_box.addItem("0")

        #This button closes the window
        self.back = QPushButton("Return")
        self.back.setMinimumWidth(60)
        self.back.setMinimumHeight(100)
        self.back.setFont(QFont("Courier", 30))
        self.back.setStyleSheet("QPushButton {background-color: red; color: white; font-size: 20;}")
        
        #This button initiates the query method - fetches all the relevant data
        self.submit = QPushButton("Query")
        self.submit.setMinimumWidth(60)
        self.submit.setMinimumHeight(100)
        self.submit.setFont(QFont("Courier", 30))
        self.submit.setStyleSheet("QPushButton {background-color: green; color: white;}")

        #This is the table which displays the data which the user has queried when it is found
        self.db = QTableWidget()
        #Sets the number of rows in the table - only 24 possible tasks to find
        self.db.setRowCount(24)
        #Sets the number of columns in the table - there are 5 headers
        self.db.setColumnCount(5)
        #Sets the headers so that they match the database
        self.db_header = ("TaskName", "Question 1", "Question 2", "Question 3", "Question 4")
        #Applies the header to the table
        self.db.setHorizontalHeaderLabels(self.db_header)
        self.db.setStyleSheet("QTableWidget {selection-background-color: #A3C1DA;}")

        #Sets the layout to a QGridLayout so that the widgets can be positioned easily
        self.layout = QGridLayout()

        ##Sets layout as the layout to be used
        self.setLayout(self.layout)

        #Adds all of the widgets to the layout
        self.layout.addWidget(self.db, 0, 0) #These numbers position the widget in the layout
        self.layout.addWidget(self.task_box_label, 0, 1)
        self.layout.addWidget(self.task_box, 1, 1)
        self.layout.addWidget(self.score_box_label, 2, 1)
        self.layout.addWidget(self.score_box, 3, 1)
        self.layout.addWidget(self.back, 4, 0)
        self.layout.addWidget(self.submit, 4, 1)

        #The connections for returning to the previous screen or querying the database
        self.back.clicked.connect(self.selected_back)
        self.submit.clicked.connect(self.selected_submit)

    #Closes the window
    def selected_back(self):
        self.close()

    #This method takes the input in the combo boxes are uses it to search the database
    def selected_submit(self):
        _count = 0
        #data is the combo box selection and is passed into the database method
        data = self.task_box.currentText()
        score_data = self.score_box.currentText()
        #This method is in the database_class
        report = g_database.get_query(data, score_data)
        #This clears the contents of the table with each new query so it does'nt continue to
        #display data that is no longer relevant
        for count in range(24):
            self.db.setItem(count, 0, QTableWidgetItem(None))
            self.db.setItem(count, 1, QTableWidgetItem(None))
            self.db.setItem(count, 2, QTableWidgetItem(None))
            self.db.setItem(count, 3, QTableWidgetItem(None))
            self.db.setItem(count, 4, QTableWidgetItem(None))
        #The report variable represents all that was fetched from the database
        for record in report:
            #Each piece of information is displayed in the QTableWidget under the right headers
            #so that it looks exactly the same as the actual database would
            self.db.setItem(_count, 0, QTableWidgetItem(record[0]))
            self.db.setItem(_count, 1, QTableWidgetItem(str(record[1])))
            self.db.setItem(_count, 2, QTableWidgetItem(str(record[2])))
            self.db.setItem(_count, 3, QTableWidgetItem(str(record[3])))
            self.db.setItem(_count, 4, QTableWidgetItem(str(record[4])))
            _count += 1

