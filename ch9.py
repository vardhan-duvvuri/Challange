def rev(word):
	return "".join(word[i] for i in xrange(len(word)-1,-1,-1))
def isReverse(word1, word2):
	if len(word1) != len(word2):
		return False
	elif rev(word1) == word2:
		return True
	else:
		return False

if __name__ == "__main__":
	print isReverse("apple","elppa")
