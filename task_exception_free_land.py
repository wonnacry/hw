def get_free_land(s, lw):
	if s[0] == 0:
		raise ValueError("Не задана площадь участка")
	if 0 in lw:
		raise ValueError("Не задана площадь грядки")
	if s[0] * 100 < (lw[0] * lw[1]):
		raise ValueError("Размер грядки больше размера участка")
	return s[0] * 100 % (lw[0] * lw[1])
