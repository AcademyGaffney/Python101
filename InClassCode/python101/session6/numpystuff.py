import numpy as np

oneDArray = np.array([4,6,5,8,9,7,4,2,3,5,1,6,12,9,4])
twoDArray = np.array([[3,6,2],[5,8,3],[9,2,3]])
zeroDArray = np.array(30)
tenDArray = np.array([[3,4],[2], [[3,4,5],[3,2]]], ndmin=10, dtype=object)
zeroedOneDArray = np.zeros(10)

print(oneDArray)
print(twoDArray)
print(zeroDArray)
print(tenDArray)
print(zeroedOneDArray)


print(oneDArray[3])
print(twoDArray[1][2])
print(twoDArray[:2])


# Create a 3x5 array out of our 15 element array
# reshape(3,-1) will do the same, making the second dimension
# whatever size it needs to be
twoDA = oneDArray.reshape(3,5)

print(twoDA)
print(twoDArray.reshape(-1))

print(np.concatenate((twoDArray, twoDArray), axis=0))

