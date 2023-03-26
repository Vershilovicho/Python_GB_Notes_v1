import json


def save_file(data):
    
    try:
        primary_data = json.load(open('notes.json', encoding='utf-8'))
    except FileNotFoundError:
        primary_data = []

    primary_data.append(data)

    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(primary_data, file, indent=2, ensure_ascii=False)


def rewrite_file(data):
   
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def read_file(open_file='notes.json'):

    with open(f'{open_file}', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        result = []
        for i in data:
            result.append(i)
        return result
