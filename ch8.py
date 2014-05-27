def removeVowels(word):
	excepted = []
	out = ""
	for letter in word:
		if letter.lower() not in "aeiou":
			excepted.append(letter)
	return "".join(X for X in excepted)
if __name__ == "__main__":
	print removeVowels("people")
