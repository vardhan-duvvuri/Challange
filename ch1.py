# Write a function that returns 4 lists given a postive number.
def createLists(num): 
	l = ()
	a = range(1,num+1)
	b = range(num,0,-1)
	c = range(-num,0,1)
	d = range(-1,-num-1,-1)
	l+=(a,b,c,d)
	return l

if __name__ == "__main__":
	print createLists(5)
