def fibonacci(n):
	f1 = 0
	f2 = 1
	yield 1
	for i in range(n-1):
		a = f1 + f2
		yield a
		f1 = f2
		f2 = a
