def rightJustify(word):
	string = ""
	i = 0
	while i < 50-len(word):
		print i
		string += " "
		i+=1
	print len(string+word)
	return string+word

if __name__ == "__main__":
	print rightJustify('microsoft')
