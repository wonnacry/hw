def encode(text, a):
	k = []
	for i in range(len(text)):
		k.append(text[i])
		ho = 0
		if k[i].islower():
			ho = 32
			k[i] = chr(ord(k[i]) - ho)
		if k[i].isalpha():
			if a > (90-ord(k[i])):
				k[i] = chr(64 + (a - (90 - ord(k[i]))) + ho)
			else:
				k[i] = chr(ord(k[i]) + a + ho)
	return(''.join(k))

def decode(text, a):
	k = []
	for i in range(len(text)):
		k.append(text[i])
		ho = 0
		if k[i].islower():
			ho = 32
			k[i] = chr(ord(k[i]) - ho)
		if k[i].isalpha():
			if a > 26-(90-ord(k[i])):
					k[i] = chr(91 - (a - (ord(k[i])-65)) + ho)
			else:
					k[i] = chr(ord(k[i]) - a + ho)
	return(''.join(k))
