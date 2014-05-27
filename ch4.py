def cmpqn(a, b):
	for i,j in a,b:
		print i,j
		#if ord(i)>ord(j):
			#return 1
		#elif ord(i)<ord(j):
			#return -1
		#else:
			#return 0
def sortqns(qnlist):
	return sorted(qnlist, cmp=cmpqn) 

if __name__ == "__main__":
	print sortqns(["s12q1", "s1q2", "s1q1"])
