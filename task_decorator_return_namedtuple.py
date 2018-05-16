from collections import namedtuple

def return_namedtuple(*name):
	def dec(func):
		def wr(*args, **kwargs):
			
			if isinstance(args, tuple):
				a = namedtuple('asd', ' '.join(name))
				q = a(*func(*args, **kwargs))
				
			return(q)
		return wr
	return dec
