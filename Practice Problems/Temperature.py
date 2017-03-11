def c(temp):
    ctemp = int((5.0/9.0)*(temp-32))
    print(ctemp)

def f(temp):
    ftemp = (9/5)*(temp) + 32
    print(ftemp)

choice=raw_input("1 for C/2 for F")
inputtemp=raw_input("enter temp in %s" %choice)
if choice=='1':
    f(int(inputtemp))
elif choice=='2':
    c(int(inputtemp))
else:
    print("check input")
