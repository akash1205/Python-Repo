from random import randint

number = randint(1,100)
print(number)

check = True
while check:
    inp = raw_input("enter number")
    if int(inp) > number:
        print("high")
    elif int(inp) < number:
        print("low")
    else:
        print("got it")
        check = False

print("you won")
