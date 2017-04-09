a=list()
x= input()
t = x.split(",")
for q in t:
    a.append(q.lower())
y=(",".join(sorted(list(set(a)))))
z = y.split(",")
print(len(z))
