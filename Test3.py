filehand=open("/Users/akashjain/Google Drive/Workplace/Skills/Python/Python-Repo/hey.txt")
count = 0
l=list()
for line in filehand:
    x = line.split()
    for words in x:
        if words in l: continue
        l.append(words)

print(l)
filehand.close()

filehand=open("/Users/akashjain/Google Drive/Workplace/Skills/Python/Python-Repo/hey.txt")
d = dict()
for line in filehand:
    x=line.split()
    for words in x:
        if words not in d:
            d[words] = 1
        else:
            d[words] = d[words] + 1

print(d)
#filehand.close()
filehand.seek(0)
a=filehand.readlines()
print(a[1])
s= "akashjain"
p=list(s)
print(p)

hand1 = open("/Users/akashjain/Google Drive/Workplace/Skills/Python/Python-Repo/hey1.txt", 'w')
hand1.write("test123")
hand1.close()
