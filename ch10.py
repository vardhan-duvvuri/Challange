def getCommonLetters(word1, word2):
	li1=[]
	li2=[]
	for i in word1:
		li1.append(i)
	for j in word2:
		li2.append(j)
	return "".join(x for x in list(set(li1).intersection(set(li2))))

if __name__ == "__main__":
	print getCommonLetters('microsoft','apple')
