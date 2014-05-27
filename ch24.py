def invertDictionary(d):
	out = {}
	temp = []
	for i in d.values():
		#out[i] = []
		temp.append(i)
	temp = set(temp)
	for i in temp:
		temp1 = []
		for key,value in d.iteritems():
			if value == i:
				temp1.append(key)
		out[i] = temp1
	return out
	

if __name__ == "__main__":
	print invertDictionary({'a':1, 'b':2, 'c':3, 'd':2})
