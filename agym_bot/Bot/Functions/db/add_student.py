from .connection import *

def add_student(student_data):
    student_data = tuple(student_data)

    cmd.execute("INSERT INTO students VALUES (?,?,?,?,?)", student_data)
    connection.commit()
