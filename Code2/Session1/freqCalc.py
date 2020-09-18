vString = input("Enter a string: ")

resultDict = {}

for e in vString:
    if e in resultDict:
        resultDict[e] += 1
    else:
        resultDict[e] = 1

for key, val in resultDict.items():
    print(key + ": " + str(val))
    