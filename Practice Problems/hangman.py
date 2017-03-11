#filename = i=raw_input("file")
from sys import exit
from random import randint
ofile = open("abc.txt")
for line in ofile:
    words = line.split()
ran = randint(0,len(words)-1)
print(ran)
#word = list(words[ran])
word = words[ran]
print(word)
field = list(len(word)*'_')
print(''.join(field))
wrong = 0
while wrong < 5:
    print(''.join(field),word)
    if (''.join(field)==word):
        print("you won")
        exit(1)
    else:
        inp = raw_input("enter a letter")

    if len(inp) > 1:
        print("enter letter")
    else:
        temp = word.find(inp)
        print(temp)
        if temp >= 0:
            if(temp== 0):
                field[temp] = inp
            else:
                field[temp] = inp
            print(''.join(field))
        else:
            wrong=wrong+1
            print("wrong")
if wrong == 5:
    print("lost")
else:
    print("won")
