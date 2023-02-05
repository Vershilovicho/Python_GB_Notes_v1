from user_interface import Notes
from save_read_file import save_file
import user_commands

test1 = Notes('Hello kitty', 'This is very interesting')
test2 = Notes('Добрый день', 'Нам очень весело')
print(test1)
print(test2)

ready_data = user_commands.save_note_to_data(test1.get_id(), test1.get_title(),
                                             test1.get_msg(), test1.get_change_date())
print(ready_data)

save_file(ready_data)
