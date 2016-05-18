from ..utilities import json_file
path_AG = "../Agym/Classes/"


def add(class_name, homework_data):
    homework_path = path_AG + class_name + "/homework"
    homework_json = json_file.read(homework_path)
    if homework_json["assignments"]:
        homework_data["id"] = homework_json["assignments"][-1]["id"] + 1
    else:
        homework_data["id"] = 1
    homework_json["assignments"].append(homework_data)

    json_file.write(homework_path, homework_json)


def delete(class_name, homework_id):
    homework_path = path_AG + class_name + "/homework"
    homework_json = json_file.read(homework_path)

    to_delete = -1
    for i in range(len(homework_json["assignments"])):
        if homework_json["assignments"][i]["id"] == homework_id:
            to_delete = i

    if to_delete + 1:
        del homework_json["assignments"][to_delete]
    json_file.write(homework_path, homework_json)
