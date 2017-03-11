import random
import math
akash=[]
y=open("abc.txt")
for line in y:
	t = line.split()
	for p in t:
		if p not in akash:
			akash.append(p)

akash.sort()
print(akash)
print('done')
