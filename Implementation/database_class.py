import sqlite3
#
from database_gui import *
from homework_parent_class import *
##from add_names_widget import *

class Database:
    def __init__(self, db_name):
        self._db_name = db_name
        self.table_name = "Student"
        self.create_table(self.table_name)
##        self.insert_data("DownloadMoreROM")

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
                Score integer,
                primary key(StudentID))"""
                cursor.execute(sql)
                db.commit()
                
    def insert_data_first(self, first_name, last_name):
        with sqlite3.connect(self._db_name) as db:
##            sql = """insert into Student values
##                  ((SELECT max(StudentID) From Student) + 1,
##                  '{0}')""".format(first_name)
            sql = "insert into Student(StudentID, FirstName, Surname) values ((SELECT max(StudentID) FROM Student)+1, '{0}', '{1}')".format(first_name, last_name)
##            cursor = db.cursor()
            self.execute_sql(sql)
##            cursor.execute(values)
##            db.commit()

##    def insert_data_last(self, last_name):
##        with sqlite3.connect(self._db_name) as db:
##            sql = "insert into Student(Surname) values ((WHERE FirstName == first_name, '{0}')".format(last_name)
##            sql = """insert into Student values
##                  ((SELECT max(Surname) From Student) + 1,
##                  '{0}')""".format(last_name)
##            self.execute_sql(sql)

    def insert_data_score(self, score):
        with sqlite3.connect(self._db_name) as db:
            sql = """insert into Student(Score) values
                  ((SELECT max(Score) From Student) + 1,
                  '{0}')""".format(score)
            self.execute_sql(sql)

    def GetAllNames(self):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute("select * from Student")
            students = cursor.fetchall()
            return students

g_database = Database("student_database.db")
