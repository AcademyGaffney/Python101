inString = input("Please enter a string: ")
resultDict = {}
for char in inString:
    if char in resultDict:
        resultDict[char] += 1
    else:
        resultDict[char] = 1

for key, val in resultDict.items():
    print("Character: {} occurs {} times(s)".format(key, val))