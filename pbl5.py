M,N = [int(x) for x in raw_input().split(' ')]

sum = 0
#print array
for i in range (N):
	A,B,C = [int(x) for x in raw_input().split(' ')]
	sum+=(B-A+1)*C

print int(sum/M)

