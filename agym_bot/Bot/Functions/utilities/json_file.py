import json


def read(path):
    json_file = open(path, "r", encoding="utf-8")
    json_data = JSON.parse(json_file.read())

    return json_data


def write(path, data):
    json_data = JSON.dumps(data)
    json_file = open(path, "w", encoding="utf-8")
    json_file.write(json_data)
