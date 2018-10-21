import numpy

print('Gauss Seidel Method')

# matrix = the squared equation matrix
# n = number of equations in matrix
# vector = Y matrix
# t = tolerance
# it = max iterations
def gaussSeidelMethod(matrix, n, vector, t, it):
    print("Your equations must be diagonally greater than 0 and heavy.")
    print("Otherwise convergence won't occur.")
    x = numpy.zeros(n)  # vector that holds each x reflection once it is completely calculated
    error = numpy.zeros((n, 2))  # matrix to store x error for past iterations
    i = 0
    while i < it:
        tError = 0
        i += 1
        for row in range(0, n):
            clearForXRes = 0
            for col in range(0, n):
                if col != row:  # this if st. prevents the denominator coef. of the current row to be subtracting from o
                                # its own reflection
                    clearForXRes += matrix[row, col] * x[col]  # the other coefs. are added to the reflection
            x[row] = (vector[row] - clearForXRes) / matrix[row, row]
            # when clearForXRes contains every other coef. it is divided by the current coef. number equal to the row num
            # Error calculation starts
            error[row, 1] = x[row]
            err = (abs(((error[row, 1] - error[row, 0]) / error[row, 1]) * 100))
            print("Error x" + str(row + 1) + ":" + str(err))
            error[row, 0] = error[row, 1]
            tError += err
            if tError < t and row == n - 1:
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

    resFinal = ""
    for row in range(0, n):
        resFinal += ("x" + str(row+1) + " " + str(x[row]))
        resFinal += " "

    resFinal += ("# iterations : " + str(i) + " error: " + str(tError))

    return resFinal


# Matrix Creation
n = int(input('input number of equations'))
matrix = numpy.zeros((n, n))
# results = numpy.zeros(n)  # vector that holds results once obtained in the method
vector = numpy.zeros(n)  # vector that holds each equation's result


# Fill the matrix
print('Introduce the matrix coefficients')

for row in range(0, n):
    for col in range(0, n):
        matrix[row, col] = float(input("M[" + str(row+1) + "," + str(col+1) + "]"))
    vector[row] = float(input("N[" + str(row+1) + "]"))


results = gaussSeidelMethod(matrix, n, vector, 0.005, 100)

print(results)





