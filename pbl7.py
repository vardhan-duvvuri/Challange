from math import *

T = int(raw_input())
if T < 1 or T > 10**5:
	exit(0)
for i in xrange(T):
	N = int(raw_input())
	if N < 1 or N > 10**10:
		exit(0)
	r1 = sqrt(5*N*N+4)
	r2 = sqrt(5*N*N-4)
	if r1%1 == 0 or r2%1 == 0:
		print "IsFibo"
	else:
		print "IsNotFibo"


