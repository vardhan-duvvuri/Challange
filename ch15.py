def isInAlphabeticalOrder(word):
	for i in range(1,len(word)):
                if ord(word[i])<ord(word[i-1]):
                        return False
                else:
                        continue
        return True
if __name__ == "__main__":
	print isInAlphabeticalOrder('app')
