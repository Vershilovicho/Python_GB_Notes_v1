from user_interface import Notes
from save_read_file import load_file



def create_new_note():
    '''
    Коннектор, принимает input данных title, msg от пользователя,
    подставляет автоматом id, date.
    :return:
    '''
    title = create_tittle()
    msg = create_msg()
    new_notes = Notes(title, msg)
    ready_note = save_note_to_data(new_notes.get_id(), title, msg, new_notes.get_change_date())
    return ready_note


def create_tittle():
    title = input('Введите название Заметки: ')
    # title = 'Новая заметка'
    return title


def create_msg():
    msg = input('Введите заметку: ')
    # msg = 'Вот нужная информация'
    return msg


def save_note_to_data(id, title, msg, date):
    '''
    Принимает значения атрибутов класса, переводит их в словарь.
    :param id:  Атрибут
    :param title: Атрибу
    :param msg: Атрибут
    :param date: Атрибут
    :return: Возвращает словарем значения атрибута класса
    '''
    date_list = {
        'id': id,
        'title': title,
        'msg': msg,
        'date': date
    }
    return date_list


def show_all_notice():
    result = load_file()
    return result

# def del_note(id):


# def save_note(data): # под вопросом
#     save_file(data)
#     return 'Данные сохранены'

