def average(lst):
	sum = 0
	for i in lst:
		sum += i
	return(round(sum/len(lst),3))
