import numpy as np
from math import *
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

numPoints = 5
x = [0, 10, 20, 30, 40]
y = [39284, 23984, 23948, 2039, 23120209]

matrix = np.zeros((numPoints, numPoints))

for i in range(numPoints):
    matrix[i][0] = 1
power = 1
for i in range(numPoints):
    for j in range(1, numPoints):
        matrix[i][j] = pow(x[i], power)
        power += 1
    power = 1

print(matrix)
print('')
inverse = np.linalg.inv(matrix)
print(inverse)
print('')
result = np.matmul(inverse, y)
print(result)
