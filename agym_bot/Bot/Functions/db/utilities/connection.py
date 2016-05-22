import sqlite3
connection = sqlite3.connect("../Agym/students.db", check_same_thread=False)
cmd = connection.cursor()
