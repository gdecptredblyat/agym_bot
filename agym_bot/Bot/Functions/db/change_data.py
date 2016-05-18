from .utilities.connection import *

def change_data(student_id, new_data):
    sql_query = ""

    def add_to_query(column):
        nonlocal sql_query

        if sql_query:
            sql_query += ","
        if column in new_data:
            sql_query += "{column}='{value}'".format(
                column=column,
                value=new_data[column]
            )

    for column in new_data:
        add_to_query(column)

    print(sql_query)
    cmd.execute("UPDATE students SET {query} WHERE telegram_id={id}".format(
            query=sql_query,
            id=student_id
        ))
    connection.commit()
