def mixedList(mlist):
	ilist = []
	for i in mlist:
		if type(i) != int:
			ilist.append(int(i))
		else:
			ilist.append(i)
	print ilist
	return (min(ilist),max(ilist))

if __name__ == "__main__":
	print mixedList(['4', 7, '3', 9])
