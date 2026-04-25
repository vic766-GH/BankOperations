import json


def loadJson(path) -> list:
    """Функция чтения финансовых транзакций из файла JSON"""
    with open(path) as json_file:
        data = json.load(json_file)
    if len(data) == 0:
        return []
    else:
        return data

def saveJson(path, data):
    with open(path, 'w') as outfile:
        json.dump(data, outfile)
    return