from ..utilities import json_file
from .utilities import path


def add(class_name, event_data):
    event_path = path.AG + class_name + "/events"
    event_json = json_file.read(event_path)
    if event_json["events"]:
        event_data["id"] = event_json["events"][-1]["id"] + 1
    else:
        event_data["id"] = 1
    event_json["events"].append(event_data)

    json_file.write(event_path, event_json)


def delete(class_name, event_id):
    event_path = path.AG + class_name + "/events"
    event_json = json_file.read(event_path)

    to_delete = -1
    for i in range(len(event_json["events"])):
        if event_json["events"][i]["id"] == event_id:
            to_delete = i

    if to_delete + 1:
        del event_json["events"][to_delete]
    json_file.write(event_path, event_json)
