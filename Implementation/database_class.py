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
                (TaskID text,
                Qone integer,
                Qtwo integer,
                Qthree integer,
                Qfour integer,
                primary key(TaskID))"""
                cursor.execute(sql)
                db.commit()
                #Total real,

    def insert_data_first(self, task, correct_count):
        sql = "insert into Student(TaskID, Qone, Qtwo, Qthree, Qfour) values ('{0}', '{1}', '{2}', '{3}', '{4}')".format(task, correct_count, str(0), str(0), str(0), str(0)) #Total
        #GET MAX TASKID CODE FROM HOME!!!
        self.execute_sql(sql)

    def insert_data_second(self, task, count_2, count_3, count_4):
        with sqlite3.connect(self._db_name) as db:
            sql = "UPDATE Student SET Qtwo = '{0}' WHERE TaskID = '{1}'".format(count_2, task)
            self.execute_sql(sql)
            sql_2 = "UPDATE Student SET Qthree = '{0}' WHERE TaskID = '{1}'".format(count_3, task)
            self.execute_sql(sql_2)
            sql_3 = "UPDATE Student SET Qfour = '{0}' WHERE TaskID = '{1}'".format(count_4, task)
            self.execute_sql(sql_3)
##            sql_4 = "UPDATE Student SET Total = '{0}%' WHERE TaskID = '{1}'".format(total, task)
##            self.execute_sql(sql_4)

    def GetAllNames(self):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            cursor.execute("select * from Student")
            students = cursor.fetchall()
            return students

g_database = Database("student_database.db")
