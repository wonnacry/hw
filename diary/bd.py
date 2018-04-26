import sqlite3
conn = sqlite3.connect('schema.sql')
cursor = conn.cursor()
sql = '''
	CREATE TABLE IF NOT EXISTS my_diary (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	target TEXT NOT NULL DEFAULT 'Тут название задачи',
	short_url INTEGER NOT NULL DEFAULT 0
	)
'''
cursor.execute(sql)
conn.commit()
conn.close()
