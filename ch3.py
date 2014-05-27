def lowercase(x):
	r = ""
	for i in x:
		if i.islower():
			r=r+i
	return r
def fn1(word):
   return filter(lowercase, word)

def fn2(word):
   #a = ""
   return filter(lambda x:x if ord(x)>47 and ord(x)<57 else "",word)

if __name__ == "__main__":
	print fn1('aBcXyZ')
	#print fn1('abcDEF1')
	print fn2('a2+%0yZ11')
	#print fn2('13a@b24&z') 
