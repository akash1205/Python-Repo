akash = dict()
count = 1
x=open("I:\Skills\Python\hey.txt")
for line in x:
	t=line.split()
	for p in t:
		y = akash.get(p,0)
		akash[p] = y+1
		
print(akash.sort())
print("and" in akash)