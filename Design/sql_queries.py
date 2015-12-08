"""insert into
Student(FirstName, LastName, UserID) values
('{0}', '{1}', '{2}')
""".format(FirstName, LastName, UserID)


    sql = """create table Student
          (UserID integer,
          FirstName text,
          LastName text,
          primary key(UserID))"""

"""select * from Student
    where TaskName = '{0}' and UserID = '{1}'""".format(TaskName, UserID)

"""select * from Class
    where TaskName = '{0}' and ClassID = '{1}'""".format(TaskName, ClassID)

"""select * from Class
    where StudentID = '{0}'""".format(StudentID)

"""select * from Class
    where TaskName = '{0}' and Rating = '{1}'""".format(TaskName, Rating)

"""select * from Student
    where StudentID = '{0}' and Rating = '{1}'""".format(StudentID, Rating)

"""update Student
    OverallPercentScore = '{0}'
    IndividualPercentScore = '{1}'
    Rating = '{2}'
    where StudentID = '{3}' and TaskName = '{4}'
    """.format(OverallPercentScore, IndividualPercentScore, Rating, StudentID, TaskName)

"""update Student
    Feedback = '{0}'
    where StudentID = '{1}' and TaskName = '{2}'
    """.format(Feedback, StudentID, TaskName)
