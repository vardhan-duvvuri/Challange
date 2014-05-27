# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(raw_input())
for i in range (0,T):
	A,B,C1 = [int(x) for x in raw_input().split(' ')]
	answer = 0
	# write code to compute answer
	k = A/B
	answer += k
	while k >= C1:
		#print answer
		a = k/C1
		#print a
		b = k%C1
		#print b
		answer += a
		k = b+a
	print answer
