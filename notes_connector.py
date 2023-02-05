from user_commands import save_note_to_data, create_tittle, create_msg
from user_interface import Notes
from save_read_file import save_file, load_file
from user_commands import save_note_to_data
from user_commands import create_new_note


def start_note():
    print('*** Добро пожаловать в програму заметки! *** \n')
    while True:
        program = input(str.lower(f'{"*" * 40} \nХотите создать новую заметку? \n'
                        'Для ввода, наберите Yes или Y, \n'
                                  f'Для выхода наберите Quit или Q.\n {"*" * 40} \n'
                                  f'Вводите сюда --->: '))
        if program == 'q' or program == 'quit':
            break
        else:
            start = create_new_note()
            save_file(start)




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
