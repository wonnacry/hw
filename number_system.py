def dec2bin(number):
	cc = 2
	return(dec2boh(number,cc))

def dec2oct(number):
	cc = 8
	return(dec2boh(number,cc))
	
def dec2hex(number):
	cc = 16
	return(dec2boh(number,cc))

def bin2dec(number):
	cc = 2
	return(boh2dec(number,cc))

def oct2dec(number):
	cc = 8
	return(boh2dec(number,cc))

def hex2dec(number):
	cc = 16
	return(boh2dec(number,cc))



def boh2dec(number,cc):
	ans = 0
	number = str(number)
	alph = 'abcdef'
	for n, i in enumerate(number[::-1]):
		if i in alph:
			ans +=(alph.index(i) + 10) * cc ** n
		else:
			ans += int(i) * cc ** n
	return(ans)

def dec2boh(number,cc):
	ans = ''
	alph = 'abcdef'
	while number >= 1:
		if number % cc > 9:
			ans += alph[(number % cc) - 10]
		else:
			ans += str(number % cc)
		number //= cc
	return(ans[::-1])
