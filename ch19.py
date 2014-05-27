def isAnagram(w1, w2):
	w1=w1.lower()
	w2=w2.lower()
	word1=[]
	word2=[]
	for i in w1:
		word1.append(i)
	for i in w2:
		word2.append(i)
	#print word1,word2
	word1.sort()
	word2.sort()
	if word1 == word2:
		return True
	else:
		return False

if __name__ == "__main__":
	print isAnagram('google', 'gogogo')
