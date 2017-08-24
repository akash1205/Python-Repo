from sys import argv
from os.path import exists
<<<<<<< HEAD
import string
=======
>>>>>>> 27ecebd93dc1976d051edc7ab1ba2926f22eb932

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
<<<<<<< HEAD

print("test" , 3 in listtest)
=======
>>>>>>> 27ecebd93dc1976d051edc7ab1ba2926f22eb932
print(listtest[6])

for i in range(0,6):
    print(listtest[i])
j = 0
while j < 6:
    print("Akash")
    j+=1

def editfile(fromfile,tofile):
    print(exists(tofile))
<<<<<<< HEAD
    dict1 = dict()
    listx = list()
    fl = open(fromfile)
    tf=open(tofile,'a')
    for line in fl:
        line = line.translate(str.maketrans("","",string.punctuation))
        line = line.lower()
        for words in line.split():
            if dict1.get(words,0):
                dict1[words] = dict1[words]+1
            else:
                dict1[words] = 1
    tf.write(fl.read())
    fl.close()
    tf.close()
    print(dict1)
    items = []
    for key,val in dict1.items():
        items.append((val,key))
    print(items.sort(reverse=True))


editfile(fromfile, tofile)

#tuples
ak = ()
print(type(ak))
ak = "Akash"
print(ak[0])
p,q = listtest2
print(p,q)
ak = listtest2
print(ak)
=======
    fl = open(fromfile)
    tf=open(tofile,'a')
    tf.write(fl.read())
    fl.close()
    tf.close()

editfile(fromfile, tofile)
>>>>>>> 27ecebd93dc1976d051edc7ab1ba2926f22eb932
