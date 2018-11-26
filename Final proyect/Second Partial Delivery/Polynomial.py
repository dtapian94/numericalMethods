import numpy as np
from math import *

# np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

def quadFunc(x):
    result = v2[0] + v2[1] * x + (v2[2] * np.power(x, 2))
    return result

def cubFunc(x):
    result = v2[0] + v2[1] * x + (v2[2] * np.power(x, 2)) + (v2[3] * np.power(x, 3))
    return result

def quartFunc(x):
    result = v2[0] + v2[1] * x + (v2[2] * np.power(x, 2)) + (v2[3] * np.power(x, 3)) + (v2[4] * np.power(x, 4))
    return result


print("Polynomial Regression Method")

numPoints = int(input("Enter the number of points to evaluate\n"))

x = []
y = []
xy = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x2y = []
x3y = []
x4y = []

sumX = 0
sumY = 0
sumXY = 0
sumX2 = 0
sumX3 = 0
sumX4 = 0
sumX5 = 0
sumX6 = 0
sumX7 = 0
sumX8 = 0
sumX2Y = 0
sumX3Y = 0
sumX4Y = 0

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
    x5.append(np.power(x[i], 5))
    sumX5 += x5[i]
    x6.append(np.power(x[i], 6))
    sumX6 += x6[i]
    x7.append(np.power(x[i], 7))
    sumX7 += x7[i]
    x8.append(np.power(x[i], 8))
    sumX8 += x8[i]
    x2y.append(x2[i] * y[i])
    sumX2Y += x2y[i]
    x3y.append(x3[i] * y[i])
    sumX3Y += x3y[i]
    x4y.append(x4[i] * y[i])
    sumX4Y += x4y[i]

# QUADRATIC
# matrix of coefficients
matrix = np.zeros((3, 3))
vector = np.zeros(3)

matrix[0, 0] = numPoints
matrix[0, 1] = sumX
matrix[0, 2] = sumX2

for r in range(1, 3):
    for c in range(0, 2):
        matrix[r, c] = matrix[r - 1, c + 1]

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
    st += np.power((y[i] - sumY / numPoints), 2)

r2 = (st - e2) / st
r = np.power(r2, 1 / 2)

print("f(x)= " + str(v2[0]) + " + " + str(v2[1]) + "x  + " + str(v2[2]) + "x2 ")
print("r2 = " + str(r2))
print("r = " + str(r))


#       CUBIC
# matrix of coefficients
matrix2 = np.zeros((4, 4))
vector2 = np.zeros(4)
matrix2[0, 0] = numPoints
matrix2[0, 1] = sumX
matrix2[0, 2] = sumX2
matrix2[0, 3] = sumX3


for c in range(0, 3):
    matrix2[1, c] = matrix2[0, c + 1]

matrix2[1, 3] = sumX4

for c in range(0, 3):
    matrix2[2, c] = matrix2[1, c + 1]

matrix2[2, 3] = sumX5

for c in range(0, 3):
    matrix2[3, c] = matrix2[2, c + 1]

matrix2[3, 3] = sumX6


vector2[0] = sumY
vector2[1] = sumXY
vector2[2] = sumX2Y
vector2[3] = sumX3Y

# inverse matrix multiplication
inverse2 = np.linalg.inv(matrix2)
v2 = np.zeros(4)
v2 = np.matmul(inverse2, vector2)

# Calculation of error begins
e2 = 0
st = 0
for i in range(numPoints):
    e2 += np.power(y[i] - cubFunc(x[i]), 2)
    st += np.power((y[i] - sumY / numPoints), 2)

r2 = (st - e2) / st
r = np.power(r2, 1 / 2)

print("f(x)= " + str(v2[0]) + " + " + str(v2[1]) + "x  + " + str(v2[2]) + "x2 + " + str(v2[3]) + "x3 ")
print("r2 = " + str(r2))
print("r = " + str(r))

#       QUARTIC
# matrix of coefficients
matrix3 = np.zeros((5, 5))
vector2 = np.zeros(5)
matrix3[0, 0] = numPoints
matrix3[0, 1] = sumX
matrix3[0, 2] = sumX2
matrix3[0, 3] = sumX3
matrix3[0, 4] = sumX4

for c in range(0, 4):
    matrix3[1, c] = matrix3[0, c + 1]

matrix3[1, 4] = sumX5

for c in range(0, 4):
    matrix3[2, c] = matrix3[1, c + 1]

matrix3[2, 4] = sumX6

for c in range(0, 4):
    matrix3[3, c] = matrix3[2, c + 1]

matrix3[3, 4] = sumX7

for c in range(0, 4):
    matrix3[4, c] = matrix3[3, c + 1]

matrix3[4, 4] = sumX8

print(matrix3)
vector2[0] = sumY
vector2[1] = sumXY
vector2[2] = sumX2Y
vector2[3] = sumX3Y
vector2[4] = sumX4Y

# inverse matrix multiplication
inverse2 = np.linalg.inv(matrix3)
v2 = np.zeros(5)
v2 = np.matmul(inverse2, vector2)

# Calculation of error begins
e2 = 0
st = 0
for i in range(numPoints):
    e2 += np.power(y[i] - quartFunc(x[i]), 2)
    st += np.power((y[i] - sumY / numPoints), 2)

r2 = (st - e2) / st
r = np.power(r2, 1 / 2)

print("f(x)= " + str(v2[0]) + " + " + str(v2[1]) + "x  + " + str(v2[2]) + "x2 + " + str(v2[3]) + "x3 +" + str(v2[4]) + "x4")
print("r2 = " + str(r2))
print("r = " + str(r))
