from ..connection import *

def by_last_or_first_name(last_name, first_name):
    cmd.execute("SELECT * FROM students \
                WHERE last_name=? AND first_name=?",
        [last_name, first_name])
    fetch_all = cmd.fetchall()
    if fetch_all:
        return fetch_all[0]

    #none with both, trying last_name
    last_name = (last_name, )
    cmd.execute("SELECT * FROM students \
                WHERE last_name=?", last_name)
    fetch_all = cmd.fetchall()
    if fetch_all:
        return fetch_all[0]

    #none with this last_name, trying name
    first_name = (first_name, )
    cmd.execute("SELECT * FROM students \
                WHERE first_name=?", first_name)
    fetch_all = cmd.fetchall()
    if fetch_all:
        return fetch_all[0]

    #none at all
    else:
        return False
