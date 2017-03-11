from sys import argv
script,filename =argv
def printall(f):
    print(f.read())

def summing(a,b):
    c=a+b
    return c

print(summing(1,2))

def rewind(f):
    f.seek(0)

def printaline(linecount,f):
    print(linecount,f.readline())

current = open(filename)
printall(current)

rewind(current)

line=1
printaline(line,current)


line=2
printaline(line,current)

rewind(current)
current = open(filename)
count = 0
for lines in current:
    count = count + 1
    print(lines,count)
