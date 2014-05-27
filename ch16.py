def isAllLettersUsed(word, required):
	letters = []
	requiredlist = []
	for i in required:
		letters.append(i)
	letters = set(letters)
	for i in word:
		requiredlist.append(i)
	requiredlist = set(requiredlist)

	if len(letters.intersection(requiredlist)) == len(letters):
		return True
	else:
		return False
	

if __name__ == "__main__":
	print isAllLettersUsed('apple', 'apple')
