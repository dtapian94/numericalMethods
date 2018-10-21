""""
Created on Thu Oct 11 15:01:24
@author: Eduardo Badillo Á
"""
# Xs = array of x values
# Ys = array of y values
# n = number of points given
# x = value to be evaluated
# deg = degree of the lagrange poly
def LagrangeMethod(Xs, Ys, n, x, deg):
    print("Lagrange Interpolation Method")

    # Points selection process
    sumC = [None] * (n-deg)
    for j in range(0, n - deg):
        sumC[j] = 0
        for k in range(j, (deg+1+j)):
            sumC[j] += Xs[k]
        sumC[j] /= (deg+1)

    lesser = abs(sumC[0] - x)
    m = 0
    for l in range(1, n - deg):
        if abs(sumC[l]-x) < lesser:
            lesser = abs(sumC[l]-x)
            m = l

    # Method begins
    result = 0
    result = float(result)
    returnVal = ""
    for i in range(m, n):
        pie = 1
        for j in range(m, n):
            if i != j:  # this if st. prevents the current x to be subtracted by itself in the denominator
                pie *= (x - Xs[j]) / float(Xs[i] - Xs[j])  # This var represents the iterative product notation letter "pi"
        pie *= Ys[i]
        result += pie
        print(result)
        returnVal += ("LF" + str(i-m) + ":" + str(result))
        returnVal += " "
    returnVal += ("X: " + str(x) + " f(X): " + str(result))
    print('The value at x = ' + str(x) + " is " + str(result))
    print('Suggestion: to improve the result you should try to insert more points')
    return returnVal


# Input points and x to be evaluated
n = int(input('Enter number of points to be inserted'))

Xs = []  # x values
Ys = []  # y values

for i in range(0, n):
    Xs.append(float(input('Input X' + str(i+1))))
    Ys.append(float(input('Input Y' + str(i+1))))

x = float(input('Enter x to be evaluated'))

res = LagrangeMethod(Xs, Ys, n, x, 3)

print(res)