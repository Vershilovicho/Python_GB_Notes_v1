import csv

def save_file(data):
    '''
    Записывает данные формата list в txt файл.
    :param data: Данные типа list
    :return: записывает в формат *.txt значения (в одну строрку)
    '''
    with open('Notes.txt', 'w', encoding='UTF-8', newline='') as file:
        for item in data:
            print(f'{item}; ', file=file, end='')

