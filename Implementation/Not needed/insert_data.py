import sqlite3
#
def insert_data(values):
    with sqlite3.connect("student_names.db") as db:
        cursor = db.cursor()
        sql = "insert into Student (StudentName, Surname) values (?, ?)"
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    new = ("Indi", "Loombands")
    insert_data(new)
