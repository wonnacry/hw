'''
Модуль, который взаимодействует с меню, просит ввести
пользователя какие-либо данные
'''

import sys
from datetime import datetime
from diary import storage

get_connection = lambda: storage.connect('my_diary.sqlite')

def action_add():
	task = input('\nВведите текст задачи: ')
	deadline = input('\nВведите дедлайн задачи или нажмите Enter при его отсутствиии: ')
	deadline = 'Without deadline' if deadline == '' else deadline
	if task:
		with get_connection() as conn:
			storage.add_task(conn, task, deadline)
	else:
		print('\nТекст задачи не может быть пустым')
		action_add()

def action_find_all():
	print('''
	1. Завершённые задачи
	2. Незавершённые задачи
	3. Все задачи
	''')
	c = {
	'1':'Done',
	'2':'Not done',
	'3':'3'
	}
	h = c[input('Выберите тип задач: ')]
	with get_connection() as conn:
		storage.show_all(conn, h)

def action_edit():
	n_id = input('\nВведите id задачи для редактирования: ')
	n_task = input('\nВведите новый текст задачи: ')
	n_deadline = input('\nВведите deadline задачи или оставьте поле пустым: ')
	with get_connection() as conn:
		storage.edit_task(conn, n_id, n_task, n_deadline)

def action_done_task():
	n_id = input('\nВведите id задачи для завершения: ')
	with get_connection() as conn:
		storage.done_task(conn, n_id)

def action_not_done_task():
	n_id = input('\nВведите id задачи: ')
	with get_connection() as conn:
		storage.not_done_task(conn, n_id)

def action_delete():
	a = input('''
	1. Удалить одну задачу
	2. Удалить все задачи
	
	Введите команду: ''')
	with get_connection() as conn:
		if a == '1': 
			n_id = input('\nВведите id задачи для удаления: ')
			storage.del_task(conn, n_id)
		else:
			storage.del_all(conn)

def action_exit():
	sys.exit(0)

def action_show_time():
	print(datetime.today())


