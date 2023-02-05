from save_read_file import save_file, load_file
from user_commands import create_new_note, show_all_notice, search_notice
import json


def start_note():
    """
    Исполнительный метод - коннектор модулей,
    реализует функционал:
    1) Создания заметки
    2) Выхода из программы
    3) Показывает все заметки
    4) Поиск по заметкам
    :return:
    """
    print('*** Добро пожаловать в програму заметки! *** \n')
    while True:
        program = input(str(f'{"*" * 40} \n             Вы в меню\n {"*" * 40} \n'
                        f'{"-" * 15}Введите{"-" * 15}\n'
                                  f'1 - Создать новую заметку\n'
                                  f'2 - Выйти\n'
                                  f'3 - Показать все заметки\n'
                                  f'4 - Найти заметку\n'
                                  f'Вводите сюда --->: '))
        menu = {
            '1': 'start',
            '2': 'quit',
            '3': 'show_all',
            '4': 'search'
        }

        try:
            program = menu[program]
            if program == 'quit':
                exit(0)
            elif program == 'start':
                start = create_new_note()
                save_file(start)
                print(f'{"-" * 15}\nЗаметка создана!\n{"-" * 15}')
            elif program == 'show_all':
                show_all_notice()
            elif program == 'search':
                choice = input(f'{"-" * 15}Выберите поле для поиска:{"-" * 15}\n'
                                  f'1 - Поиск по id\n'
                                  f'2 - Поиск по Теме\n'
                                  f'3 - Поиск по сообщению в заметке\n'
                                  f'4 - Поиск по дате и времени\n'
                                  f'Вводите сюда --->: ')

                search_type = {
                    '1': 'id',
                    '2': 'title',
                    '3': 'msg',
                    '4': 'data'
                }
                try:
                    choice = search_type[choice]
                    temp_list = json.load(open('notes.json', encoding='utf-8'))
                    if choice == 'id':
                        search = int(input('Введите id для поиска заметки:'))
                        search_notice(temp_list, search, 1)
                    elif choice == 'title':
                        search = input('Введите "Тему заметки" для поиска:')
                        search_notice(temp_list, search, 2)
                    elif choice == 'msg':
                        search = input('Введите "Текст заметки" для поиска:')
                        search_notice(temp_list, search, 3)
                    elif choice == 'data':
                        search = input('Введите "Полную дату" для поиска:')
                        search_notice(temp_list, search, 4)
                except FileNotFoundError as e:
                    print(f'Вы еще не создали ни одной заметки!')
        except KeyError as e:
            print('Введено неверное значение, возврат в меню!')
