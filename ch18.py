def splitWord(word, numOfChar):
	output = []
	for i in range(0,len(word),numOfChar):
		output.append(word[i:i+numOfChar])
	return output

if __name__ == "__main__":
	print splitWord('google', 3)
