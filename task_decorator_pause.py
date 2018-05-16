import time

def pause(t):
	def dec(func):
		def wr(*args, **kwargs):
			time.sleep(t)
			return func(*args, **kwargs)
		return wr
	return dec
