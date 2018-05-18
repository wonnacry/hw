import random
import string

def password_generator(n):
	while 1:
		a = []
		for i in range(n):
			a.append(random.choice(string.ascii_letters))
		yield ''.join(a)
