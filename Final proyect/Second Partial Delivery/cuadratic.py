import numpy as np
from math import *

# np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

def quadFunc(x):
    result = v2[0] + v2[1]*x + (v2[2]*np.power(x, 2))
    return result


print("Polynomial Regression Method")

numPoints = int(input("Enter the number of points to evaluate\n"))

x = []
y = []
xy = []
x2 = []
x3 = []
x4 = []
x2y = []

sumX = 0
sumY = 0
sumXY = 0
sumX2 = 0
sumX3 = 0
sumX4 = 0
sumX2Y = 0

for i in range(numPoints):
    x.append(float(input("Enter x" + str(i) + "\t")))
    sumX += x[i]

    y.append(float(input("Enter y" + str(i) + "\t")))
    sumY += y[i]

    xy.append(x[i] * y[i])
    sumXY += xy[i]

    x2.append(x[i] * x[i])
    sumX2 += x2[i]

    x3.append(np.power(x[i], 3))
    sumX3 += x3[i]

    x4.append(np.power(x[i], 4))
    sumX4 += x4[i]

    x2y.append(x2[i]*y[i])
    sumX2Y += x2y[i]
# matrix of coefficients
matrix = np.zeros((3, 3))
vector = np.zeros(3)

matrix[0, 0] = numPoints
matrix[0, 1] = sumX
matrix[0, 2] = sumX2

for r in range(1, 3):
    for c in range(0, 2):
        matrix[r, c] = matrix[r-1, c+1]

matrix[1, 2] = sumX3
matrix[2, 2] = sumX4
matrix[2, 1] = matrix[1, 2]

vector[0] = sumY
vector[1] = sumXY
vector[2] = sumX2Y

# inverse matrix multiplication
inverse = np.linalg.inv(matrix)
v2 = np.zeros(3)
v2 = np.matmul(inverse, vector)


# Calculation of error begins
e2 = 0
st = 0
for i in range(numPoints):
    e2 += np.power(y[i] - quadFunc(x[i]), 2)
    st += np.power((y[i]-sumY/numPoints), 2)

r2 = (st-e2)/st
r = np.power(r2, 1/2)

print("f(x)= " + str(v2[0]) + " + " + str(v2[1]) + "x  + " + str(v2[2]) + "x2 ")
print("r2 = " + str(r2))
print("r = " + str(r))

