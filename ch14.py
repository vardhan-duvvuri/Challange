def rev(word):
	return "".join(word[i] for i in xrange(len(word)-1,-1,-1))
def isPalindrome(word):
	if word.lower() == rev(word.lower()):
		return True
	else:
		return False

if __name__ == "__main__":
	print isPalindrome("Racecar")
