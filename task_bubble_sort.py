def bubble_sort(lst): #Называем функцию
	for i in range(len(lst)-1):  #Необходимо пройти по каждому элементу
		for i in range(len(lst)-1): #Проход одного элемента
			if lst[i] > lst[i+1]:	#Элемент должен быть больше последующего
				lst[i], lst[i+1] = lst[i+1], lst[i] #Тогда они меняются местами
	return(lst) #Выводим полученный результат
