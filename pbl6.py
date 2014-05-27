try:
	T = int(raw_input())
	if T < 1 or T > 10**5:
		exit(0)

	for i in xrange (0,T):
		l = []
		N,K = [int(x) for x in raw_input().split(' ')]
		if N < 1 or K > 10**9:
			exit(0)
		if N > K:
			for i in xrange(1,N):
				#print i
				if long(i*(N-i)) <= long(N*K) and i < N:
					l.append(i)
		else:
			for i in xrange(1,K):
				if long(i*(N-i)) <= long(N*K) and i < N:
					l.append(i)
		print len(l)

except Exception,e:
	print "Memory Exception Occured"
