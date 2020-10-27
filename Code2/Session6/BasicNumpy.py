import numpy as np

oneDArray = np.array([4,6,8,3,4,2,7,6,4,9,3,4])
twoDArray = np.array([[3,6,2],[5,8,3],[9,2,3]])
zeroDArray = np.array(30)
tenDArray = np.array([3,4], ndmin=10)
zeroedOneDArray = np.zeros(10)

print(oneDArray)
print(twoDArray)
print(zeroDArray)
print(tenDArray)
print(zeroedOneDArray)

print(twoDArray[:2])

twoD2 = oneDArray.reshape(4,3)

print(twoD2)

oneD2 = twoDArray.reshape(-1)
print(oneD2)

print(np.concatenate((twoDArray, twoDArray), axis=0))
a, b, c = np.split(oneDArray, 3)
print(a)

print(np.where(oneDArray % 2 == 1))

randArr1 = np.random.randint(100, size=(4,3,2))
print(randArr1)

print(np.random.choice([1,2,3,4], p=(.3, .2, .1, .4), size = 100))

print(np.sort(np.random.normal(loc = 5, scale = 1, size=(50))))