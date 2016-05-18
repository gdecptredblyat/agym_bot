from .utilities.connection import *
from .utilities import find


def group(class_name):
    class_name = (class_name, )
    cmd.execute("SELECT last_name, first_name, mobile FROM students \
                WHERE class=?", class_name)

    fetch_all = cmd.fetchall()

    mobiles = []
    for fetch in fetch_all:
        mobiles.append({
            "last_name": fetch[0],
            "first_name": fetch[1],
            "mobile": fetch[2]
        })

    return mobiles


def person(last_name, first_name):
    person = find.by_last_or_first_name(last_name, first_name)

    if person:
        # mobile is last field (#fucksql)
        return person[-1]
    else:
        # return replies.no_student (TODO)
        return False
