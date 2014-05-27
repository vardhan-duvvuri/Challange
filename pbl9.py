N = int(raw_input())
if N < 0 or N > 20:
    exit(0)
    
text = raw_input()

words = ['am','are','were','was','is','been','being','be']

text = text.replace("----","fillblank")

#print text

import nltk
list = nltk.sent_tokenize(text)
for i in list:
	print i
