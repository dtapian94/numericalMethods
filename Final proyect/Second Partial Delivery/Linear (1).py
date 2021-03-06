import numpy as np


def linearFunc(x):
    result = a0 + a1*x
    return result

print("Linear Regression Method")

numPoints = int(input("Enter the number of points to evaluate\n"))

x = []
y = []
xy = []
x2 = []

sumX = 0
sumY = 0
sumXY = 0
sumX2 = 0


for i in range(numPoints):
    x.append(float(input("Enter x" + str(i) + "\t")))
    sumX += x[i]

    y.append(float(input("Enter y" + str(i) + "\t")))
    sumY += y[i]

    xy.append(x[i] * y[i])
    sumXY += xy[i]

    x2.append(x[i] * x[i])
    sumX2 += x2[i]

# Calculation of the linear formula begins
a1 = ((numPoints*sumXY)-(sumX*sumY))/((numPoints*sumX2) - np.power(sumX, 2))
a0 = (sumY/numPoints) - a1*(sumX/numPoints)


# Calculation of error begins
e2 = 0
st = 0
for i in range(numPoints):
    e2 += np.power(y[i] - linearFunc(x[i]), 2)
    st += np.power((y[i]-sumY/numPoints), 2)

r2 = (st-e2)/st
r = np.power(r2, 1/2)


print("f(x) = " + str(a0) + " + " + str(a1) + "x")
print("r2 = " + str(r2))
print("r = " + str(r))


