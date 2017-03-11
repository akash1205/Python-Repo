tenthings = "one two three four five"
stuff=tenthings.split(" ")
mystuff=["one","two","three","four","five","six","seven","eight","nine","ten"]

while len(stuff) <=10:
    temp=mystuff.pop(0)
    print("adding",temp)
    stuff.append(temp)

print("completed", stuff)
print(stuff[-1])
print(" ".join(stuff))
print("#".join(stuff[2:5]))
print(mystuff)
