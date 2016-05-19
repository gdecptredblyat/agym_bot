import datetime
from ..utilities import json_file
from .utilities import path


def read(class_name, day, ):
    schedule_path = path.AG + class_name + "/schedule"
    schedule = json_file.read(schedule_path)
    return schedule[day]


def parse(schedule, for_today):
    total = 0
    responce = {
        "day": "",
        "header": "",
        "schedule": ""
    }
    endtime = {
        1: "10:30",
        2: "12:20",
        3: "14:00",
        4: "16:00",
        5: "17:40",
    }
    templates = {
        "1 subject": " "*4 + "{n} пара - {subject} \n",
        "2 subjects": " "*4 + "{n} пара: \n",
        "subject": " "*8 + "{n} полка - {subject} \n",
        "header": "Всего пар - {total} (Кончается в {endtime}) \n"
    }

    for lesson in schedule:
        total += 1
        if len(lesson) == 1:
            responce["schedule"] += templates["1 subject"].format(
                n=total,
                subject=lesson[0]
            )
        else:
            responce["schedule"] += templates["2 subjects"].format(n=total)
            for i in range(len(lesson)):
                responce["schedule"] += templates["subject"].format(
                    n=i + 1,
                    subject=lesson[i]
                )
    responce["header"] = templates["header"].format(
        total=total,
        endtime=endtime[total]
    )

    if for_today:
        responce["day"] = "На сегодня \n\n"
    else:
        responce["day"] = "На завтра \n\n"

    return "".join(responce.values())


def get(class_name):
    now = datetime.datetime.now()
    schedule = {}
    if now.hour <= 16:
        schedule = read(class_name, now.strftime("%A"))
        for_today = True
    else:
        schedule = read((now+datetime.timedelta(days=1)).strftime("%A"))
        for_today = False

    return parse(schedule, for_today)
