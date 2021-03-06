from PyQt4.QtGui import *
from PyQt4.QtCore import *
import random

##from admin_account_home import *
from add_class_widget import *
from database_class import *

class AddNamesWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.showMaximized()

        self.add_class = QPushButton("Add Class")
        self.select_class = QComboBox()
        self.input_first_name = QLineEdit()
        self.label_1 = QLabel("Please input the student's first name: ")
        self.input_last_name = QLineEdit()
        self.label_2 = QLabel("Please input the student's last name: ")
        self.submit_1 = QPushButton("Add Name")
        self.submit_2 = QPushButton("Add Another")
        self.back = QPushButton("Return")

        self.add_class.setMinimumHeight(110)
        self.add_class.setMinimumWidth(60)
        self.add_class.setFont(QFont("Courier", 40))

        self.back.setMinimumHeight(110)
        self.back.setMinimumWidth(60)
        self.back.setFont(QFont("Courier", 40))

        self.submit_1.setMinimumHeight(110)
        self.submit_1.setMinimumWidth(60)
        self.submit_1.setFont(QFont("Courier", 40))

        self.submit_2.setMinimumHeight(110)
        self.submit_2.setMinimumWidth(60)
        self.submit_2.setFont(QFont("Courier", 40))
        
        self.input_first_name.setMinimumHeight(110)
        self.input_first_name.setMinimumWidth(60)
        self.input_first_name.setFont(QFont("Courier", 40))

        self.input_last_name.setMinimumHeight(110)
        self.input_last_name.setMinimumWidth(60)
        self.input_last_name.setFont(QFont("Courier", 40))

        self.label_1.setFont(QFont("Courier", 20))
        self.label_2.setFont(QFont("Courier", 20))

        self.select_class.setMinimumHeight(110)
        self.select_class.setMinimumWidth(60)
        self.select_class.setFont(QFont("Courier", 40))
        
        self.select_class.setStyleSheet("QComboBox {background-color: #A3C1DA; color: blue}")
        self.setStyleSheet("QPushButton {background-color: #A3C1DA; color: blue}")

        self.layout = QGridLayout()

        self.setLayout(self.layout)

        self.layout.addWidget(self.add_class, 0, 1)
        self.layout.addWidget(self.select_class, 0, 0)
        self.layout.addWidget(self.input_first_name, 1, 1)
        self.layout.addWidget(self.input_last_name, 2, 1)
        self.layout.addWidget(self.label_1, 1, 0)
        self.layout.addWidget(self.label_2, 2, 0)
        self.layout.addWidget(self.submit_1, 3, 0)
        self.layout.addWidget(self.submit_2, 3, 1)
        self.layout.addWidget(self.back, 4, 0)

        self.add_class.clicked.connect(self.selected_add_class)
        self.submit_1.clicked.connect(self.selected_submit_1)
        self.submit_2.clicked.connect(self.selected_submit_2)
        self.back.clicked.connect(self.selected_back)

    def selected_back(self):
        self.close()

    def selected_add_class(self):
        self.close()
        add_class = AddClassWidget()
        add_class.show()
        add_class._raise()

    def selected_submit_1(self):
        character_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        cont = False
        while not cont:
            try:
                username_ = self.input_first_name.text()
                cont = True
            except AttributeError:
                error_message = ErrorMessage8()
                error_message.show()
                error_message._raise()
            password_a = random.choice(character_list)
            password_b = random.randint(0, 9)
            password_c = random.choice(character_list)
            password_d = random.randint(0, 9)
            password_e = random.choice(character_list)
            password_f = random.randint(0, 9)
            password_g = random.choice(character_list)
            password_ = password_a + str(password_b) + password_c + str(password_d) + password_e + str(password_f) + password_g
            g_database.insert_data_first(self.input_first_name.text(), self.input_last_name.text(), 0)
            self.save_login(username_, password_)
            self.close()

    def selected_submit_2(self):
        pass
        #SQL add names to database

    def save_login(self, username_, password_):
        with open("login_details.txt", mode = "w") as logins:
            logins.write(username_)
            logins.write("\n")
            logins.write(password_)
            logins.write("\n")
