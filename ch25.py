def convertVector(numbers):
	out = {}
	for i in range(len(numbers)):
		if numbers[i] != 0:
			out[i] = numbers[i]
	return out

if __name__ == "__main__":
	print convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4])
