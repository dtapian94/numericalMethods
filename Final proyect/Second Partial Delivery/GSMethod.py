""""
Created on Tue Oct 9 7:17:12

@author: Eduardo Badillo Á
"""
import numpy

print('Gauss Seidel Method')
print('Type in the size of the matrix')

# Matrix Creation
m = int(input('input number of rows'))
n = int(input('input number of columns'))
matrix = numpy.zeros((m, n))
x = numpy.zeros(m)  # vector that holds each x reflection once it is completely calculated
vector = numpy.zeros(n)  # vector that holds each equation's result

# Auxiliary matrix
error = numpy.zeros((m, 2))  # matrix to store x error for past iterations

# Fill the matrix
print('Introduce the matrix coefficients')

for row in range(0, m):
    for col in range(0, n):
        matrix[row, col] = float(input("M[" + str(row+1) + "," + str(col+1) + "]"))
    vector[row] = float(input("N[" + str(row+1) + "]"))


# Method begins
t = float(input("Input tolerance"))
it = int(input("Input max number of iterations"))

i = 0
err = 0
tError = 0
while i < it:
    tError = 0
    clearForXRes = 0
    i += 1
    for row in range(0, m):
        clearForXRes = 0
        for col in range(0, n):
            if col != row:  # this if st. prevents the denominator coef. of the current row to be subtracting from  o
                            # its own reflection
                clearForXRes += matrix[row, col] * x[col]  # the other coefs. are added to the reflection
        x[row] = (vector[row] - clearForXRes) / matrix[row, row]
        # when clearForXRes contains every other coef. it is divided by the current coef. number equal to the row num
        # Error calculation starts
        error[row, 1] = x[row]
        err = (abs(((error[row, 1] - error[row, 0])/error[row, 1])*100))
        print("Error x" + str(row + 1) + ":" + str(err))
        error[row, 0] = error[row, 1]
        tError += err
        if tError < t and row == m-1:
            break
    else:
        print("The total error for iteration " + str(i) + " is :" + str(tError))
        print("\n")
        continue
    print("The total error for iteration " + str(i) + " is :" + str(tError))
    print("\n")
    break

if t < tError:
    print("The number of max iterations was reached but the tolerance wasn't met. ")
    print("Suggestion: Rearrange equations in matrix so they are diagonally dominant.")
print("Results:")
for row in range(0, m):
    print("x" + str(row + 1) + " " + str(x[row]))