filename=raw_input("input filename to read")
test=dict()
file1 = open(filename)
#text = file1.read()
for line in file1:
    print(line)
    s=line.split()
    for i in s:
        if i in test:
            test[i] = test[i] + 1
        else:
            test[i] = 1

print(test)
