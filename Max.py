import math
akash=[]
x=input("Enter number")
akash.append(int(x))
while(x!="done"):
	x=input("Enter number")
	if(x!="done"):
		akash.append(int(x))

print(akash)
print(max(akash))
print(min(akash))
