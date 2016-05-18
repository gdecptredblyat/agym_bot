import json


def read(path):
    json_file = open(path + ".json", "r", encoding="utf-8")
    json_data = json.loads(json_file.read())

    return json_data


def write(path, data):
    json_data = json.dumps(data)
    json_file = open(path + ".json", "w", encoding="utf-8")
    json_file.write(json_data)
