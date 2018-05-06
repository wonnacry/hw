'''
Модуль непосредственного взаимодействия с самой базой данных
'''

import os.path as Path
import sqlite3

D_INSERT_TASK = '''
	INSERT INTO my_diary(task, deadline)
	VALUES (?, ?)
'''

D_SELECT_D_NOTD = '''
	SELECT id, task, status_of_t, deadline
	FROM my_diary
	WHERE status_of_t=?
'''

D_SELECT_ALL = '''
	SELECT id, task, status_of_t, deadline
	FROM my_diary
'''

D_EDIT = '''
	UPDATE my_diary SET task=?, deadline=? WHERE id=?
'''

D_DONE = '''
	UPDATE my_diary SET status_of_t='Done' WHERE id=?
'''

D_NOT_DONE = '''
	UPDATE my_diary SET status_of_t='Not done' WHERE id=?
'''

D_DEL_TASK = '''
	DELETE FROM my_diary WHERE id=?
'''

D_DEL_ALL = '''
	DELETE FROM my_diary
'''

def connect(db_name):
	if db_name is None:
		db_name = ':memory:'
	conn = sqlite3.connect(db_name)
	return conn

def initialize(conn):
	script_path = Path.join(Path.dirname(__file__), 'schema.sql')
	
	with conn, open(script_path) as f:
		conn.executescript(f.read())


def add_task(conn, task, deadline):
	if not task:
		raise RuntimeError('Задача не может быть пустой')
	
	with conn:
		cursor = conn.execute(D_INSERT_TASK, (task, deadline))

def show_all(conn, a):
	with conn:
		cursor = conn.execute(D_SELECT_ALL) if a == '3' else conn.execute(D_SELECT_D_NOTD, (a,))
		lot =  cursor.fetchall()
		if lot == []:
			print()
			print('Такие задачи отсутствуют')
		else:
			print('''
  id | task info
------------------''')
			for i in lot:
				print(' ', i[0], ' |', i[1])
				for j in i[3], i[2]:
					print('     |',j)
				print('----------------')

def edit_task(conn, n_id, n_task, n_deadline):
	with conn:
		cursor = conn.execute(D_EDIT, (n_task, n_deadline, n_id))

def done_task(conn, n_id):
	with conn:
		cursor = conn.execute(D_DONE, (n_id))

def not_done_task(conn, n_id):
	with conn:
		cursor = conn.execute(D_NOT_DONE, (n_id))

def del_task(conn, n_id):
	with conn:
		cursor = conn.execute(D_DEL_TASK, (n_id))

def del_all(conn):
	with conn:
		cursor = conn.execute(D_DEL_ALL)












