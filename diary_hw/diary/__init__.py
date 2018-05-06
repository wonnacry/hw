'''
Модуль вызова меню
'''

from m_func import (action_find_all,
	action_add,
	action_edit,
	action_done_task,
	action_not_done_task,
	action_delete,
	action_exit,
	action_show_time)

get_connection = lambda: storage.connect('my_diary.sqlite')

def action_show_menu():
	print("""
---------------------------------
1. Вывести список задач          |
2. Добавить задачу               |
3. Отредактировать задачу        |
4. Завершить задачу              |
5. Начать задачу сначала         |
6. Удалить задачу                |
---------------------------------
m. Показать меню                 |
t. Показать текущую дату и время |
q. Выйти                         |
---------------------------------
""")


def main():
	with get_connection() as conn:
		storage.initialize(conn)
	
	actions = {
	'1': action_find_all,
	'2': action_add,
	'3': action_edit,
	'4': action_done_task,
	'5': action_not_done_task,
	'6': action_delete,
	'q': action_exit,
	'm': action_show_menu,
	't': action_show_time
	}
	action_show_menu()
	while 1:
		cmd = input('\nВведите команду: ')
		print()
		action = actions.get(cmd)
		
		if action:
			action()
		else:
			print('Не известная команда')
