def convertDictionary(dictionary):
	size = max(dictionary.keys())+1
	out = [0]*size
	for key,value in dictionary.iteritems():
		out[key] = value
	return out

if __name__ == "__main__":
	print convertDictionary({0: 1, 3: 2, 7: 3, 12: 4})
