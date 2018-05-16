import hashlib

def make_token(username, password):
	s = username + password
	return hashlib.md5(s.encode()).hexdigest()

logined = []

def login_required(func):
	def wr(*args, **kwargs):
		if func.__name__ in logined:
			return(func(*args, **kwargs))
		
		with open('token.txt', 'r') as f:
			logpas = f.read()
			
		for i in range(3):
			log = input('Логин? ')
			pas = input('Пароль? ')
			log_pas = make_token(log, pas)
			
			if log_pas == logpas:
				logined.append(str(func.__name__))
				break
			if i == 2:
				return None	
		return(func(*args, **kwargs))
	return wr

