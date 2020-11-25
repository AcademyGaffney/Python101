import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#First we'll generate some random data across a normal distribution (so we have something that should reasonably fit a model)

x = np.random.normal(20, 3.5, 1000)
y = np.random.normal(20, .5, 1000) / x

#Now we'll plot it to see what it looks like

#plt.scatter(x, y)
#plt.show()

#Then we'll slice the data into train and test arrays

train_x = x[:800]
train_y = y[:800]
test_x = x[800:]
test_y = y[800:]

#Let's try a linear regression

slope, intercept, r, p, std_err = stats.linregress(train_x, train_y)

def findY(x):
    return slope * x + intercept

model = list(findY(train_x))

#plt.scatter(train_x, train_y)
#plt.plot(train_x, model)
#plt.show()

print("r2 = " + str(r**2))

corr = np.corrcoef(train_y, model)
print("Again: " + str(corr**2))

#Let's check this on our test data

model_test = list(findY(test_x))
corr = np.corrcoef(test_y, model_test)
print(corr **2)

#Let's try a polynomial regression to see if we can fit the curve better

model = np.poly1d(np.polyfit(train_x, train_y, 3))

polyline = np.linspace(0, 35, 1000)

plt.scatter(train_x, train_y, c="r")
plt.plot(polyline, model(polyline), 'g--')
plt.show()

corr = np.corrcoef(train_y, model(train_x))
print(corr ** 2)

#Quite a bit better.  Let's check our test data

corr = np.corrcoef(test_y, model(test_x))
print(corr ** 2)