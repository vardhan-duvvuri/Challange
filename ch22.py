def countLetters(word):
	letters = []
	for i in word:
		letters.append(i)
	letters = set(letters)
	output = {}
	for i in letters:
		output[i] = word.count(i)
	return output

if __name__ == "__main__":
	print countLetters('google')
