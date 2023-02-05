from user_interface import Notes
from save_read_file import save_file, load_file
from user_commands import save_note_to_data
import notes_connector

#ready_data = save_note_to_data(test1.get_id(), test1.get_title(),
#                                             test1.get_msg(), test1.get_change_date())

ex_1 = notes_connector.create_new_note()

save_file(ex_1)

load_file()