def sum(*args):
    total = 0
    for i in args:
        total += i

    return total

def reverser(inString):
    print(inString)
    inString = inString.lower()
    print(inString)
    inList = inString.split()
    print(inList)
    inList.reverse()
    print(inList)
    inList[0] = inList[0][0].upper() + inList[0][1:]
    return " ".join(inList)

print(sum(1,2,3,4,5))
print(reverser("Here I go again"))