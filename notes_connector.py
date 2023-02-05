import user_commands
import user_interface


def create_new_note():
    '''
    Коннектор, принимает input данных title, msg от пользователя,
    подставляет автоматом id, date.
    :return:
    '''
    title = user_commands.create_tittle()
    msg = user_commands.create_msg()
    new_notes = user_interface.Notes(title, msg)
    ready_note = user_commands.save_note_to_data(new_notes.get_id(), title, msg, new_notes.get_change_date())
    return ready_note
