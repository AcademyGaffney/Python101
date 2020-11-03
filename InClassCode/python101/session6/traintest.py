import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

#First we'll generate some random data across a normal distribution (so we have something that should reasonably fit a model)

x = np.random.normal(5, 1, 2000)
y = np.random.normal(200, 20, 2000) / x

#Plot it to see what it looks like
#plt.scatter(x, y)
#plt.show()

#Slice the data into train and test arrays
train_x = x[:1600]
train_y = y[:1600]
test_x = x[400:]
test_y = y[400:]

#plt.scatter(train_x, train_y)
#plt.show()
#plt.scatter(test_x, test_y)
#plt.show()

# Calculate a linear regression to see if it fits our data
slope, intercept, r, p, std_err = stats.linregress(train_x, train_y)

def findY(x):
    return slope * x + intercept


# Cool aspect of Python here - we can pass a sequence into a function that accepts a value
# and it'll process the whole sequence and return a list
model = findY(train_x)

#
#plt.scatter(train_x, train_y)
#plt.plot(train_x, model)
#plt.show()

# Output r-squared for our linear regression (calculated by the linregress function)
#print(r**2)

# find and output the r-squared when applying our test data to the same linear regression
model_test = list(findY(test_x))
corr = np.corrcoef(test_y, model_test)
#print(corr**2)

# This generally shows a significant difference between train and test
# Also, a sight test shows this scatter plot isn't linear

# we setted on a cubic function after a square function didn't work well.
# both deviate significantly outside of the range of our actual data
model = np.poly1d(np.polyfit(train_x, train_y, 3))

#Generate a curve that goes beyond our data to see what it does if our X values range further
polyline = np.linspace(0, 10, 400)

plt.scatter(train_x, train_y, c="r")
plt.plot(polyline, model(polyline), 'g--')
plt.show()

corr = np.corrcoef(train_y, model(train_x))
print(corr ** 2)

corr = np.corrcoef(test_y, model(test_y))
print(corr ** 2)

# generate some new data (see if our solution is "predictive" -- which it should be since this is
# a generated correlation)
x = np.random.normal(5, 1, 200)
y = np.random.normal(200, 20, 200) / x


corr = np.corrcoef(y, model(y))
print(corr ** 2)