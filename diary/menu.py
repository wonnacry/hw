def menu():
	a = -1
	while a != 0:
		af = (list_of_t, add_t, edit_t, close_t, restart_t, get_out)
		print("""
1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
6. Выйти
		""")
		try:
			h = af[int(input('Выберите функцию: ')) - 1]
			print()
			h()
		except ValueError:
			print('Некорректный ввод. Введите число: ')
		except IndexError:
			print('Некорректный ввод. Выберите существующий номер функции')

		
def list_of_t():
	print('Тут список существующих задач со статусами')


def add_t():
	print('Тут добавляем новую задачу')

def edit_t():   #тут слово редактировать напиши нормально
	print('Тут редактируем существующую задачу')

def close_t():
	print('Тут закрываем задачу')

def restart_t():
	print('Тут начинаем задачу заного')

def get_out():
	exit()

menu()
