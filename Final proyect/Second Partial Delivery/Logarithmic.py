import numpy as np
import math as m

def linearFunc(x):
    result = a0 + a1*x
    return result

print("Power Regression Method")

numPoints = int(input("Enter the number of points to evaluate\n"))

x = []
y = []
lnx = []
lny = []
lnxlny = []
lnx2 = []

sumX = 0
sumY = 0
sumlnY = 0
sumlnx = 0
sumlxly = 0
sumlnx2 = 0

for i in range(numPoints):
    x.append(float(input("Enter x" + str(i) + "\t")))
    sumX += x[i]

    y.append(float(input("Enter y" + str(i) + "\t")))
    sumY += y[i]

    lny.append(m.log(y[i], 10))
    sumlnY += lny[i]

    lnx.append(m.log(x[i], 10))
    sumlnx += lnx[i]

    lnxlny.append(lnx[i] * lny[i])
    sumlxly += lnxlny[i]

    lnx2.append(lnx[i]*lnx[i])
    sumlnx2 += lnx2[i]

# Calculation of the linear formula begins
a1 = ((numPoints*sumlxly)-(sumlnx*sumlnY))/((numPoints*sumlnx2) - np.power(sumlnx, 2))
print(sumlnY)
print(sumlnx)
a0 = (sumlnY/numPoints) - a1*(sumlnx/numPoints)

# Calculation of error begins
e2 = 0
st = 0
for i in range(numPoints):
    e2 += np.power(lny[i] - linearFunc(lnx[i]), 2)
    st += np.power((lny[i]-sumlnY/numPoints), 2)

r2 = (st-e2)/st
r = np.power(r2, 1/2)

print("f(x) = " + str(a0) + " + " + str(a1) + "x")
print("r2 = " + str(r2))
print("r = " + str(r))