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

twoDA = oneDArray.reshape(3,5)

print(twoDA)
print(twoDArray.reshape(-1))

