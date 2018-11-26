import numpy as np


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

# Calculation starts
a1 = ((numPoints*sumXY)-(sumX*sumY))/((numPoints*sumX2) - np.power(sumX, 2))
a0 = (sumY/numPoints) - a1*(sumX/numPoints)

print("R1 = " + str(a0) + " + " + str(a1) + " X")

