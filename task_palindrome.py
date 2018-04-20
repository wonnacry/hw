def is_palindrome(s):
	k = []
	for i in str(s).lower() :
		if i != ' ':
			k.append(i)
	return(k == k[::-1])
