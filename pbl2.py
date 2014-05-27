'''n = int(raw_input())
k = int(raw_input())
if (n < 1 or n > 10**5) or (k < 1 or k > n):
	exit(0)
candies = [int(raw_input()) for i in range(0,n)]
candies.sort()
if len(candies) < 0 or len(candies) > 10**9:
	exit(0)
print candies
min_diff = max(candies[:k])-min(candies[:k])## Write code here to compute the answer using (n, k, candies)

print min_diff
'''


#!/usr/bin/python

N = input()
K = input()

assert 1 <= N <= 10**5
assert 1 <= K <= N

lis = []
for i in range(N):
    lis.append(input())

lis.sort()

for i in lis:
    assert 0 <= i <= 10**9

answer = 100000000000000000000

for index in range(N-K+1):
    diff = lis[index+K-1] - lis[index]

    if diff < answer:
        answer = diff

print answer

