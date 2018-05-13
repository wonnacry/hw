with open('data.txt', 'r') as f:
	numbers = f.read().split()
	an = []
	ap = []
	for i in numbers:
		ap.append(str(int(i) ** p))
		if int(i) % n == 0:
			an.append(str(i))
	
with open('out-1.txt', 'w') as q:
	q.write(' '.join(an))

with open('out-2.txt', 'w') as s:
	s.write(' '.join(ap))
