akash = dict()
count = 0
x=open("I:\Skills\Python\hey.txt")
for line in x:
	t=line.split()
	for p in t:
		akash[p] = count
		count= count+1
print(akash)
print(akash["is"])
vals = akash.values()
print(26 in vals)
print("is" in vals)