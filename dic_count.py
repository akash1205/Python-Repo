akash = dict()
count = 1
x=open("I:\Skills\Python\hey.txt")
for line in x:
	t=line.split()
	for p in t:
		y = akash.get(p,0)
		if y == 0:
			akash[p] = count
		else:
			akash[p] = akash[p] + 1
print(akash)
print("and" in akash)
