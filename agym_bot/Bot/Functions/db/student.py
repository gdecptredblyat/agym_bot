from .utilities.connection import *

def add(student_data):
    student_data = tuple(student_data)

    cmd.execute("INSERT INTO students VALUES (?,?,?,?,?)", student_data)
    connection.commit()

def delete(student_id):
    student_id = (student_id, )
    cmd.execute("DELETE FROM students WHERE telegram_id=?", student_id)
    connection.commit()
