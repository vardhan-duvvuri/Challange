i = 1
n = 3
num = 1
pi = 1
while i < num:
	#print n
	if i % 2 == 0:
		#print pi
		pi = pi + (float(1)/float(n))
		n += 2
		#print pi
	else:
		#print pi
		pi = pi - (float(1) /float(n))
		n += 2
		#print pi
	i = i + 1
pi = 4 * pi
print float(pi)
