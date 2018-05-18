def get_quadrant_number(x, y):
		if x > 0:
			if y > 0:
				return 1
			else:
				return 4
		elif x < 0:
			if y > 0:
				return 2
			else:
				return 3
		else:
			raise ValueError()
