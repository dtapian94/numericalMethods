import numpy as np
import math as m

def linearFunc(x):
    result = a0 + a1*x
    return result

print("Exponential Regression Method")

numPoints = int(input("Enter the number of points to evaluate\n"))

x = []
y = []
lny = []
xlny = []
x2= []

sumX = 0
sumY = 0
sumXlnY = 0
sumlnY = 0
sumX2 = 0

for i in range(numPoints):
    x.append(float(input("Enter x" + str(i) + "\t")))
    sumX += x[i]

    y.append(float(input("Enter y" + str(i) + "\t")))
    sumY += y[i]

    lny.append(m.log(y[i]))
    sumlnY += lny[i]

    xlny.append(x[i]*lny[i])
    sumXlnY += xlny[i]

    x2.append(x[i] * x[i])
    sumX2 += x2[i]

# Calculation of the linear formula begins
a1 = ((numPoints*sumXlnY)-(sumlnY*sumX))/((numPoints*sumX2) - np.power(sumX, 2))
a0 = (sumlnY/numPoints) - a1*(sumX/numPoints)

# Calculation of error begins
e2 = 0
st = 0
for i in range(numPoints):
    e2 += np.power(lny[i] - linearFunc(x[i]), 2)
    st += np.power((lny[i]-sumlnY/numPoints), 2)

r2 = (st-e2)/st
r = np.power(r2, 1/2)

normA0 = m.exp(a0)
print("f(x) = " + str(a0) + " + " + str(a1) + "x")
print("r2 = " + str(r2))
print("r = " + str(r))
print("Real equation: " + str(normA0)+ "exp("+str(a1)+"x)")