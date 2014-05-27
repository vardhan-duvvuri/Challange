t = int(raw_input())

if t < 1 or t > 10:
	exit(0)

l = []

for i in range(t):
        k = int(raw_input())
        if k >= 2 or  k <= (10**7):
                l.append(k)

for n in l:
	if  n%2 == 0:
		print (n/2)*(n/2)
	else:
		print (n/2)*((n/2)+1)
