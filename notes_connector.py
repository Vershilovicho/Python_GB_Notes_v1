from user_commands import save_note_to_data, create_tittle, create_msg
from user_interface import Notes
from save_read_file import save_file, load_file
from user_commands import save_note_to_data
from user_commands import create_new_note, show_all_notice


def start_note():
    print('*** Добро пожаловать в програму заметки! *** \n')
    while True:
        program = input(str.lower(f'{"*" * 40} \n Вы в меню\n {"*" * 40} \n'
                        f'{"-" * 15}Введите{"-" * 15}\n'
                                  f'1 - Создать новую заметку\n'
                                  f'2 - Выйти\n'
                                  f'3 - Показать все заметки\n'
                                  f'Вводите сюда --->: '))
        menu = {
            '1': 'start',
            '2': 'quit',
            '3': 'show_all'
        }

        try:
            program = menu[program]
            if program == 'quit':
                break
            elif program == 'start':
                start = create_new_note()
                save_file(start)
            elif program == 'show_all':
                show_all_notice()
        except KeyError as e:
            print('Введено неверное значение, возврат в меню!')







# def create_new_note():
#     '''
#     Коннектор, принимает input данных title, msg от пользователя,
#     подставляет автоматом id, date.
#     :return:
#     '''
#     title = create_tittle()
#     msg = create_msg()
#     new_notes = Notes(title, msg)
#     ready_note = save_note_to_data(new_notes.get_id(), title, msg, new_notes.get_change_date())
#     return ready_note
