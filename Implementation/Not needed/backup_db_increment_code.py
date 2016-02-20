((SELECT max(StudentID) FROM Student)+1,


                
    def insert_data_first(self, first_name, last_name, score):
        with sqlite3.connect(self._db_name) as db:
            sql = "insert into Student(StudentID, FirstName, Surname, Score) values ((SELECT max(StudentID) FROM Student)+1, '{0}', '{1}', '{2}')".format(first_name, last_name, str("0"))
##            cursor = db.cursor()
            self.execute_sql(sql)
##            cursor.execute(values)
##            db.commit()