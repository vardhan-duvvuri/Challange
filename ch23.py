def reverseLookup(dictionary, value):
	output = []
	for key,val in dictionary.iteritems():
		if val == value:
			output.append(key)
	return sorted(output)

if __name__ == "__main__":
	print reverseLookup({'a':1, 'b':2, 'c':2}, 2)
