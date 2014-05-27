import collections
N = int(raw_input())
if N < 1 or N > 100:
	exit(0)
list = []
for i in range(N):
	rock = raw_input()
	if not rock.islower() or len(rock) < 1 or len(rock) > 100:
		exit(0)
	list.append(rock)
final = []
for i in list:
	dictionary =  collections.Counter(i)
	for key,value in dictionary.iteritems():
		if value == 1:
			final.append(key)
fill = collections.Counter(final)
out = []
for key,value in fill.iteritems():
	if value > 1:
		out.append(key)
print len(out)
