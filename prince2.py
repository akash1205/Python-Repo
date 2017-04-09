def factors(x):
    count = 0
    if(x>0):
        for i in range(1, x ):
            if x % i == 0:
                count = count + 1
        if count == 3:
            print(x)
    else:
        for i in range(x,abs(x)):
            if(i==0):
                continue
            if x%i == 0:
                count = count + 1
        if count == 3:
            print(x)

y = input().split(",")
for h in y:
    factors(int(h))
