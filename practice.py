from sys import argv
from os.path import exists

script, fromfile , tofile = argv

listtest = [1,5,7,2,3,4]
listtest.sort()
print(listtest)
list3 = list()


for i in range(1,15):
    list3.append(i)

for k in listtest:
    print(list3[k])


listtest2=["a","b"]
listtest.append(listtest2)
print(listtest[6])

for i in range(0,6):
    print(listtest[i])
j = 0
while j < 6:
    print("Akash")
    j+=1

def editfile(fromfile,tofile):
    print(exists(tofile))
    fl = open(fromfile)
    tf=open(tofile,'a')
    tf.write(fl.read())
    fl.close()
    tf.close()

editfile(fromfile, tofile)
