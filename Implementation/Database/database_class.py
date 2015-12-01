import sqlite3

class Database:
    def __init__(self, db_name):
        self._db_name = db_name

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
                (StudentName text,
                Surname text,
                primary key(StudentName))"""
                cursor.execute(sql)
                db.commit()
                
    def insert_data(self, values):
        with sqlite3.connect(self._db_name) as db:
            cursor = db.cursor()
            sql = "insert into Student (StudentName, Surname) values (?, ?)"
            cursor.execute(values)
            db.commit()

    def GetAllNames(self):
        with sqlite3.connect(self._db_name) as db:
            cursor - db.cursor()
            cursor.execute("select * from Student")
            students = cursor.fetchall()
            return students

g_database = Database("student_database.db")
g_database.create_table("Student")
values = ("Jordan", "Russell")
g_database.insert_data(values)
