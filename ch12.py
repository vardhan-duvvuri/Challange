def echoWord(word):
	string = ""
	for i in range(len(word)):
		string = string+word
	return string	

if __name__ == "__main__":
	print echoWord("hi")
