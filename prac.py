  l = list(string)
    k = list()
    s=list()
    for i in range(len(l)):
        if l[i] in vowels:
            j = i
            if (string[i]) not in k:
                k.append(string[i])
            while j < len(l):
                if (string[i:j+1]) not in k:
                    k.append(string[i:j+1])
                    j+=1
                else:
                    j+=1
        else:
            if (string[i]) not in s:
                s.append(string[i])
            j = i
            while j < len(l):
                if (string[i:j+1]) not in s:
                    s.append(string[i:j+1])
                    j+=1
                else:
                    j+=1
    print(k)
    print(s)
    countk = counts=0
    for i in range(len(s)):
        j = string.find(s[i])
        counts+=1
        while j < len(string):
            j = string[(j+len(s[i])):].find(s[i])
            if j == -1:
                break
            else:
                counts+=1
    print(counts)
    if len(s) > len(k):
        print("Stuart",len(s))
    else:
        print("Kevin",len(k))
