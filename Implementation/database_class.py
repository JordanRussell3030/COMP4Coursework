import sqlite3

from database_gui import *
from homework_parent_class import *
from homework_widgets import *
from homework_widgets_page_2 import *
##from add_names_widget import *

class Database:
    def __init__(self, db_name):
        self._db_name = db_name
        self.table_name = "Student"
        self.create_table(self.table_name)

    def execute_sql(self, sql):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute(sql)

    def create_table(self, table_name):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute("select name from sqlite_master where name=?",(table_name,))
            result = cursor.fetchall()
            keep_table = True
            if len(result) == 1:
                response = input("The table {0} already exists, do you wish to recreate it (y/n): ".format(table_name))
                if response == "y":
                    keep_table = False
                    print("The {0} table will be recreated - all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                else:
                    print("The existing table was kept")
            else:
                keep_table = False
            if not keep_table:
                sql = """create table Student
                (StudentID integer,
                FirstName text,
                Surname text,
                Task text,
                Score integer,
                primary key(StudentID))"""
                cursor.execute(sql)
                db.commit()
                
    def insert_data_first(self, first_name, last_name, score):
        with sqlite3.connect(self._db_name) as db:
            sql = "insert into Student(StudentID, FirstName, Surname, Score) values ((SELECT max(StudentID) FROM Student)+1, '{0}', '{1}', '{2}')".format(first_name, last_name, str("0"))
##            cursor = db.cursor()
            self.execute_sql(sql)
##            cursor.execute(values)
##            db.commit()

    def insert_data_score(self, task):
        with sqlite3.connect(self._db_name) as db:
##            sql = """insert into Student(Score) values (('{0}'))""".format(score)
##            sql = """update Student set Score = '{0}' where Score = null""".format(score)
##            sql = """insert into Student(Score) values ((WHERE FirstName != NULL, ('{0}')))""".format(score)
##            sql = "UPDATE Student SET Score = '{0}' WHERE Score = 0".format(score)
            sql = "insert into Student(StudentID, Task) values ((SELECT max(StudentID) FROM Student)+1, '{0}')".format(task) #, self.correct_count
            self.execute_sql(sql)

    def GetAllNames(self):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute("select * from Student")
            students = cursor.fetchall()
            return students

g_database = Database("student_database.db")
