#challenge 1

def sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total

#challenge 2

def strReverser(inString):
    lcString = inString.lower()
    lcList = lcString.split()
    lcList.reverse()
    lcList[0] = lcList[0][0].upper() + lcList[0][1:]
    retString = " ".join(lcList)
    return retString

print(sum(1,2,3,4,5))
myList = [2,3,4,5,6]
print(sum(*myList))
#print(sum("a","b","c"))
print(strReverser("Hello there Mr. Jones"))