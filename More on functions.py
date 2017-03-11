def splitup(a):
    words=a.split(' ')
    return words

def sort(a):
    #words=a.sort(a)
    return sorted(a)

def firstword(a):
    words=a.pop(0)
    return words

def lastword(a):
    words = a.pop(-1)
    return words

def printfirstlast(a):
    words=splitup(a)
    firstword(words)
    lastword(words)

def sortsentence(a):
    words=splitup(a)
    return sort(words)

b = firstword("akashjain is a good boy")
print(b)
