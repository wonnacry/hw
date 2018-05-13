import json

def http_headers_to_json(a):
	with open(a , 'r') as f:
		f_str = f.readline().split()
		ans = {}
		if '200' in f_str:
			zxc = {
				"status_code":"200",
				"protocol":f_str[0],
				"status_message":f_str[2]
				}
		
		elif '301' in f_str:
			zxc = {
				"protocol":f_str[0],
				"status_code":"301"
				}
		else:
			zxc = {
				"method":f_str[0],
				"uri":f_str[1],
				"protocol":f_str[2]
				}
		
		for line in f:
			#line = line.replace(':', '')
			line = line.split()
			g = line[0]
			g = g.replace(':', '')
			h = (line[1:])
			j = ' '.join(h)
			qwe = dict.fromkeys([g],j)
			ans.update(qwe)
		ans.update(zxc)
	
	with open('results-1.json', 'w') as f:
		json.dump(ans, f, indent=4)
