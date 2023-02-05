from save_read_file import save_file


def create_tittle():
    title = input('Введите название Заметки: ')
    return title


def create_msg():
    msg = input('Введите заметку: ')
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

# def del_note(id):


# def save_note(data): # под вопросом
#     save_file(data)
#     return 'Данные сохранены'

