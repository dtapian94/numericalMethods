import numpy as np
from math import *
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

numPoints = int(input("Enter the number of points\n"))
x = []
y = []
for i in range(numPoints):
    x.append(float(input("Enter x" + str(i) + "\t")))
    y.append(float(input("Enter y" + str(i) + "\t")))

# numPoints = 5
# x = [0, 10, 20, 30, 40]
# y = [39284, 23984, 23948, 2039, 23120209]

matrix = np.zeros((numPoints, numPoints))

for i in range(numPoints):
    matrix[i][0] = 1
power = 1
for i in range(numPoints):
    for j in range(1, numPoints):
        matrix[i][j] = pow(x[i], power)
        power += 1
    power = 1

print("Resultant Matrix:")
print(matrix)
print('\nInverse Matrix:')
inverse = np.linalg.inv(matrix)
print(inverse)
print('\nResult:')
result = np.matmul(inverse, y)
print(result)
