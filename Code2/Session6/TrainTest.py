import numpy as np
import matplotlib.pyplot as plt
from scipy import stats



#First we'll generate some random data across a normal distribution (so we have something that should reasonably fit a model)

x = np.random.normal(5, 1, 400)
y = np.random.normal(200, 20, 400) / x

#Now we'll plot it to see what it looks like

#plt.scatter(x, y)
#plt.show()

#Then we'll slice the data into train and test arrays

train_x = x[:320]
train_y = y[:320]
test_x = x[320:]
test_y = y[320:]


#plt.scatter(train_x, train_y)
#plt.show()
#plt.scatter(test_x, test_y)
#plt.show()

#Let's try a linear regression

slope, intercept, r, p, std_err = stats.linregress(train_x, train_y)

def findY(x):
    return slope * x + intercept

model = list(findY(train_x))

#plt.scatter(train_x, train_y)
#plt.plot(train_x, model)
#plt.show()

#This doesn't look very good.  Let's calculate R-Squared

corr = np.corrcoef(train_y, model)
print(corr **2)

##That's not horrible, but not great.  Let's check the test.

model_test = list(findY(test_x))
corr = np.corrcoef(test_y, model_test)
print(corr **2)

#Consistent, but could be better.  Let's try polynomial regression.

model = np.poly1d(np.polyfit(train_x, train_y, 2))

polyline = np.linspace(0, 10, 400)

#plt.scatter(train_x, train_y, c="r")
#plt.plot(polyline, model(polyline), 'g--')
#plt.show()

#Let's check R-squared on this

corr = np.corrcoef(train_y, model(train_x))
print(corr ** 2)

#Quite a bit better.  Let's check our test data

model = np.poly1d(np.polyfit(test_x, test_y, 2))

#plt.scatter(test_x, test_y)
#plt.plot(polyline, model(polyline))
#plt.show()

corr = np.corrcoef(test_y, model(test_y))
print(corr ** 2)

x = np.random.normal(5, 1, 400)
y = np.random.normal(200, 20, 400) / x

model = np.poly1d(np.polyfit(x, y, 2))

#plt.scatter(x, y)
#plt.plot(polyline, model(polyline))
#plt.show()

corr = np.corrcoef(y, model(y))
print(corr ** 2)