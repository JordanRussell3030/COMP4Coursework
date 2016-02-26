from PyQt4.QtGui import * #These two lines import the built in PyQt code
from PyQt4.QtCore import *

from database_class import * #Needed to fetch all of the information from the database
from report_widget import * #Needed to connect to the report screen which opens when the report button is clicked

#This class is the template for the screen with the database view and the button for the report widget
class DatabaseWidget(QWidget):
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

        #This QLabel is the title on the screen
        self.title = QLabel("Progress")
        #This line sets the title font size and house style
        self.title.setFont(QFont("Courier", 40))

        #This QPushButton closes the screen
        self.back = QPushButton("Return")
        #Sets the minimum width of the QPushButton so that it will take up at least the required portion of the screen
        self.back.setMinimumWidth(60)
        #Sets the minimum height of the QPushButton so that it will take up at least the required portion of the screen
        self.back.setMinimumHeight(100)
        #Sets the font size and house style of the text in the button
        self.back.setFont(QFont("Courier", 40))
        #This overrides the background and text colour for the return button
        self.back.setStyleSheet("QPushButton {background-color: red; color: white; font-size: 20;}")

        #This button connects to the report window
        self.report = QPushButton("Report")
        self.report.setMinimumWidth(60)
        self.report.setMinimumHeight(100)
        self.report.setFont(QFont("Courier", 40))
        
        #This QTableWidget is the table which the data from the database is presented in
        self.database = QTableWidget()
        #Sets the number of rows in the table - there are only 24 possible tasks, rach of which can only be recorded once and overwritten upon improvement
        self.database.setRowCount(24)
        #Sets the number of columns in the table - there are 5 headings, 5 attributes to record
        self.database.setColumnCount(5)
        #This is the header which appears in each column in the database
        self.database_header = ("Task Name", "Question 1", "Question 2", "Question 3", "Question 4")#"Total"
        #This applies the header to the QTableWidget
        self.database.setHorizontalHeaderLabels(self.database_header)

        #This sets the background colour and text colour for all of the QPushButtons on the page
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue;}")

        #This sets the colour of the selected boxes in the QTableWidget
        self.database.setStyleSheet("QTableView {selection-background-color: #A3C1DA;}")
        #This overrides the background and text colour for the return button

        #This calls a method in database_class which fetches all of the data in the database
        students = g_database.GetAllNames()
        
        #Every bit of data fetched from the database is allocated to the corresponding column in the QTableWidget
        count = 0
        for student in students:
            #The TaskNames are put in the first column
            self.database.setItem(count, 0, QTableWidgetItem(student[0]))
            #The first question scores are put in the second column, etc.
            self.database.setItem(count, 1, QTableWidgetItem(str(student[1])))
            self.database.setItem(count, 2, QTableWidgetItem(str(student[2])))
            self.database.setItem(count, 3, QTableWidgetItem(str(student[3])))
            self.database.setItem(count, 4, QTableWidgetItem(str(student[4])))
            count += 1

        #Sets the layout of the page to a QGridLayout() so that every widget can be positioned where I want them easily
        self.layout = QGridLayout()

        #These four lines add the four widgets to the layout so they will appear when the screen is displayed.
        self.layout.addWidget(self.title, 0, 0) #These numbers are for positioning the widgets e.g This one will be in the top left of the screen
        self.layout.addWidget(self.database, 0, 1)
        self.layout.addWidget(self.back, 4, 0)
        self.layout.addWidget(self.report, 4, 1)

        #Sets the layout as the layout to be displayed
        self.setLayout(self.layout)

        #When back is clicked the selected_back method will be executed
        self.back.clicked.connect(self.selected_back)
        #When report is clicked the selected_report method will be executed
        self.report.clicked.connect(self.selected_report)

    #Executed when back is clicked
    def selected_back(self):
        #The entire progress screen disappears
        self.close()

    #Executed when report is clicked
    def selected_report(self):
        #Assigns a variable to the ReportWidget() class
        report_widget = ReportWidget()
        #The report widget will appear in front of the progress window
        report_widget.show()
        report_widget._raise()
