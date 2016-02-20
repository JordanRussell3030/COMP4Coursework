import sqlite3 #This imports all of the built in sqlite3 code

#This is the class which generates the database
class Database:
    #Constructor
    def __init__(self, db_name):
        #Assigns the db_name variable to whatever name is passed in when the class is called (in this case "student_database.db")
        self._db_name = db_name
        #The name of the table - will be used to access this database using SQL queries
        self.table_name = "Student"
        #Calls the method which creates the table called Student
        self.create_table(self.table_name)
        
    #This method is called everytime data is saved in the database so the code doesn't have to be written every time
    def execute_sql(self, sql):
        #Opens a connection to student_database.db
        with sqlite3.connect(self._db_name) as db:
            #This line makes any addition to the database remain in the database, rather than just deleting it when the program stops running
            cursor = db.cursor()
            #This line runs the sql query which is passed in each time the method is called
            cursor.execute(sql)

    #This is the method called when the program is run - each time it can be kept or over-written
    def create_table(self, table_name):
        #connects to the student_database.db
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            #Executes the SQL statement to check if the database already exists
            cursor.execute("select name from sqlite_master where name=?",(table_name,))
            #This fetches all of the results from the query (the database called Student) and assigns it to a variable so it can be used elsewhere
            result = cursor.fetchall()
            #Sets a boolean variable used to determine if the table will be deleted or not
            keep_table = True
            #Checks if there is one table already called Student
            if len(result) == 1:
                #Gives the user the option to recreate the table
                response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
                #If they choose yes, the boolean changes and the table will be deleted
                if response == "y":
                    keep_table = False
                    print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                    #This SQL statement deletes the entire table
                    cursor.execute("drop table if exists {0}".format(table_name))
                    #Commits the changes
                    db.commit()
                else:
                    print("The existing table was kept")
            else:
                keep_table = False
            #If the user deleted the previous Student table another one will be created to replace it, exactly the same except for the data inside the table
            if not keep_table:
                #This SQL statement creates the Student table with the following attributes
                sql = """create table Student
                (TaskID text,
                Qone integer,
                Qtwo integer,
                Qthree integer,
                Qfour integer,
                primary key(TaskID))"""
                #Executes the SQL statement by running the method at the top
                cursor.execute(sql)
                #Commits the changes (makes sure they stay)
                db.commit()

    #This method is called in the parent homework widget, and it saves the task name of the homework and the score from the first question,
    #then fills the remaining columns with 0 so that the next method will work
    def insert_data_first(self, task, correct_count):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute("select TaskID from Student where TaskID = '{0}'".format(task))
            info = cursor.fetchall()
            if len(info) != 0:
                sql = "UPDATE Student SET Qone = '{0}' WHERE TaskID = '{1}' AND Qone < '{2}'".format(correct_count, task, correct_count)
            else:
                #Inserts the values
                sql = "insert into Student(TaskID, Qone, Qtwo, Qthree, Qfour) values ('{0}', '{1}', '{2}', '{3}', '{4}')".format(task, correct_count, str(0), str(0), str(0))
                #Executes the SQL statement above by running the method at the top
            self.execute_sql(sql)

    #This method is called in the parent homework page 2 widget, which saves the scores for the remaining questions
    def insert_data_second(self, task, count_2, count_3, count_4):
        #Connects to the student_database.db
        with sqlite3.connect(self._db_name) as db:
            #These statements all update the value of the corresponding question score where the saved task is the same as the current task,
            #so it will only overwrite the task being attempted
            sql = "UPDATE Student SET Qtwo = '{0}' WHERE TaskID = '{1}' AND Qtwo < '{2}'".format(count_2, task, count_2)
            self.execute_sql(sql)
            sql_2 = "UPDATE Student SET Qthree = '{0}' WHERE TaskID = '{1}' AND Qthree < '{2}'".format(count_3, task, count_3)
            self.execute_sql(sql_2)
            sql_3 = "UPDATE Student SET Qfour = '{0}' WHERE TaskID = '{1}' AND Qfour < '{2}'".format(count_4, task, count_4)
            self.execute_sql(sql_3)
##            sql_4 = "UPDATE Student SET Total = '{0}%' WHERE TaskID = '{1}'".format(total, task)
##            self.execute_sql(sql_4)

    #This method fetches all of the relevant data from the database when the user makes a query i.e. searches for all the results for a task or score range
    def get_query(self, data, score_data):
        #Connects to the database
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            #Executes the SQL statement to search the database for anything with the same value as the data or score_data variables
            cursor.execute("select * from Student WHERE TaskID = '{0}' or Qone = '{1}'".format(data, score_data))
            report = cursor.fetchall()
            #Returns the results of the query so that they can be manipulated i.e. displayed in the secondary QTableWidget
            return report

    #This method is used in the database widget to display all data in the database as soon as it is opened
    def GetAllNames(self):
        #Connects to student_database.db
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            #This SQL statement selects everything in the Student table
            cursor.execute("select * from Student")
            #Everything in the cursor from the previous line is fetched and assigned a variable so that the data can be used
            students = cursor.fetchall()
            #Returns all data from the Student table
            return students

#This variable is the database, constructed from the Database class, and is called whenever changes to the database are to be made
g_database = Database("student_database.db")
