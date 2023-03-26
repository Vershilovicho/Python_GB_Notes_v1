from save_read_file import save_file
from user_commands import create_new_note, show_all_notis, search_notis, delete_notis, edit_notis
import json


def start_menu():
    print()
    print(f'{"*" * 10} Заметки {"*" * 10}')
    while True:
        program = input(str(f'{"-" * 30} \n           Меню\n{"*" * 30} \n'
                            f'{"-" * 10}Выберете:{"-" * 10}\n'
                            f'1 - Создать новую заметку\n'
                            f'2 - Выйти\n'
                            f'3 - Показать все заметки\n'
                            f'4 - Найти заметку\n'
                            f'5 - Удалить заметку\n'
                            f'6 - Редактировать заметку\n'
                            f'Введите цифру меню: '))
        menu = {
            '1': 'start',
            '2': 'go_out',
            '3': 'show_all',
            '4': 'find',
            '5': 'delete',
            '6': 'edit'
        }

        try:
            program = menu[program]
            if program == 'go_out':
                exit(0)
            elif program == 'start':
                start = create_new_note()
                save_file(start)
                print(f'{"-" * 15}\nЗаметка создана!\n{"-" * 15}')
            elif program == 'show_all':
                show_all_notis()
            elif program == 'find':
                choice = input(f'{"-" * 15}Выберите значение для поиска:{"-" * 15}\n'
                               f'1 - Поиск по id\n'
                               f'2 - Поиск по теме\n'
                               f'3 - Поиск по сообщению в заметке\n'
                               f'4 - Поиск по дате и времени\n'
                               f'Введите номер меню: ')

                search_type = {
                    '1': 'id',
                    '2': 'title',
                    '3': 'msg',
                    '4': 'data'
                }
                try:
                    choice = search_type[choice]
                    us_list = json.load(open('notes.json', encoding='utf-8'))
                    if choice == 'id':
                        search = int(input('Введите id для поиска заметки (Например: 1):'))
                        search_notis(us_list, search, 1)
                    elif choice == 'title':
                        search = str(input('Введите "Тему заметки" для поиска (Например: Понедельник):'))
                        search_notis(us_list, search, 2)
                    elif choice == 'msg':
                        search = str(input('Введите "Текст заметки" для поиска (Например: Сегодня солнечно):'))
                        search_notis(us_list, search, 3)
                    elif choice == 'data':
                        search = str(input('Введите "Полную дату" для поиска (Например: 06-02-2023 18:23:59):'))
                        search_notis(us_list, search, 4)
                except FileNotFoundError:
                    print(f'Вы еще не создали ни одной заметки!')
            elif program == 'delete':
                us_list = json.load(open('notes.json', encoding='utf-8'))
                print('Заметки, которые вы создали:')
                show_all_notis()
                notic_val = int(input(f'\nВведите id заметки, которую хотите удалить: '))
                delete_notis(us_list, 'id', notic_val)
            elif program == 'edit':
                us_list = json.load(open('notes.json', encoding='utf-8'))
                print('Заметки, которые вы создали:')
                show_all_notis()
                notic_val = int(input(f'\nВведите id заметки, которую хотите изменить: '))
                edit_notis(us_list, 'id', notic_val)
        except KeyError:
            print('Вы ввели неверное значение, возврат в меню!')
