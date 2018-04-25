from datetime import datetime, date, time, timedelta
def counter():
	a = datetime.now()
	c = a.replace(a.isocalendar()[0]+1, 1, 1, 00,00,00,00)
	g = str(c - a).split()
	g[2] = g[2].split(':')
	k = []
	for i in g[0], g[2][0],g[2][1]:
		k.append(int(i))
	return(words(k))

def words(k):
	u = ''
	w = ({
		1:'день',
		2:'дня',
		3:'дней'
		},
		{
		1:'час',
		2:'часа',
		3:'часов'
		},
		{
		1:'минута',
		2:'минуты',
		3:'минут'
		})

	for n, i in enumerate(k):
		u += str(i) + ' '
		if i%10 in range(2,5) and i not in range(5,21):
			u += (w[n][2])
		elif i%10 == 1 and i != 11:
			u += (w[n][1])
		else:
			u += (w[n][3])
		u += ' '
	return(u)
