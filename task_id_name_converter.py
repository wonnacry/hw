def camel_to_snake(name):
	k = []
	for i in name:
		if i.isupper():
			k.append('_')
		k.append(i.lower())
	if k[0] == '_':
		k.remove(k[0])
	return(''.join(k))

def snake_to_camel(name):
	q = []
	for i in name:
		q.append(i)
	while '_' in q:
		q[q.index('_')+1] = q[q.index('_')+1].upper()
		q.remove('_')
	q[0] = q[0].upper() 
	return("".join(q))
