import numpy as np

def func(x):
    f = 0.2+25*x-200*np.power(x, 2)+675*np.power(x, 3)-900*np.power(x, 4)+400*np.power(x, 5)
    return (f)

# a & b = limits of integration
# n = number of segments
def simpson(a, b, n):

    h = (b - a) / n
    x = []
    y = []

    for i in range(0, n+1):
        x.append(a+i*h)
        y.append(func(x[i]))

# Applying formula fo simpson 1/3
    res = 0
    i = 0
    while i <= n:
        if i == 0 or i == n:  # first term
            res += y[i]
        elif i % 2 != 0:
            res += 4 * y[i]  # second term
        else:
            res += 2 * y[i]  # third term
        i += 1
    res = res * (h / 3)
    return res


n = int(input("Indicate number of segments\n"))
a = float(input("provide a bound\n"))
b = float(input("provide b bound\n"))


print("Approximate value for  " + str(n) + " segments is %.4f" % simpson(a, b, n))