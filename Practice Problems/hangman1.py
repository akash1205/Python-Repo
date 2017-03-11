#filename = i=raw_input("file")
from random import randint
ofile = open("abc.txt")
for line in ofile:
    words = line.split()
ran = randint(0,len(words)-1)
print(ran)
#word = list(words[ran])
word = words[ran]
print(word)
field = list(len(word)*'_ ')
print(''.join(field))
wrong = 0
count = 0
while wrong < 5:
    inp = raw_input("enter a letter")
    if len(inp) > 1 or len(inp) == 0:
        print("enter letter")
    else:
        for i in word:
            if i == inp:
                if count == 0:
                    field[count] = inp
                    count= count + 1
                else:
                    field[2*count] = inp

            else:
                wrong= wrong + 1
        print(field)
if wrong == 5:
    print("lost")
else:
    print("won")
