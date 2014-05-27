t = int(raw_input())
if t <= 0 or t > 10:
	exit(0)

l = []

for i in range(t):
	k = int(raw_input())
	if k >= 0 or  k < 61:
		l.append(k)

for i in l:
	m = 1
	for p in range(i):
		if p%2 == 0:
			m = m*2
		else:
			m = m+1
	print m

