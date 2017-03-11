filename = i=raw_input("file")
ofile = open(filename)
a=dict()
for line in ofile:
    words = line.split()
    for word in words:
        if word not in a:
            a[word] = 1
        else:
            a[word] = a[word] + 1

print(a)
