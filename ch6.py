def is_prime(x):
	count = 0
	for i in range(2,(x/2)+1):
		if x%i == 0:
			count += 1
	if count == 0:
		return True
	else:
		return False
		

def primeFactorization(num):
	li = []
	if num < 2:
		return li
	i = 2
	while i <= (num/2):
		if num%i == 0:
			#print num,i
			if is_prime(i):
				li.append(i)
				num = num/i
				i = 2
				#print num
			else:
				i+=1
				#continue
		else:
			i+=1
	if is_prime(num):
		li.append(num)
	return li

if __name__ == "__main__":
	num = int(raw_input("Enter : "))
	print primeFactorization(num)
