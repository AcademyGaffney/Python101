import numpy as np

oneDArray = np.array([3,4,2,5,6,8,7,9,4,12,1,8])
twoDArray = np.array([[3,4,5],[1,2,3],[6,5,4]])
zeroDArray = np.array(30)
tenDArray = np.array([2,3,4], ndmin=10)
zeroedOneDArray = np.zeros(10)
z3DArray = np.zeros([10,3,4])


print(oneDArray)
print(twoDArray)
print(zeroDArray)
print(tenDArray)
print(zeroedOneDArray)
#print(z3DArray)

z3DArray[3][2][2] = 45
#print(z3DArray)

for i in range(len(oneDArray)):
    oneDArray[i] *= 2
print(oneDArray)

threeDArray = oneDArray.reshape([3,2,2])
print(threeDArray)
oneD2 = twoDArray.reshape(-1)
print(oneD2)

print(np.concatenate((oneDArray, oneD2)))
print(np.concatenate((twoDArray, twoDArray), axis = 1))
a, b, c = np.split(oneDArray, 3)
print(a)

randArr = np.random.randint(100, size=(4,2,3))
print(randArr)

print(np.random.choice([1,2,3,4], p=[.5, .1, .1, .3], size=(10,10)))
print(np.sort(np.random.normal(loc=10, scale=2, size=(50))))