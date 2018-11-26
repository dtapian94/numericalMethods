import numpy as np

def func(x):
    f = 0.2 + 25 * x - 200 * np.power(x, 2) + 675 * np.power(x, 3) - 900 * np.power(x, 4) + 400 * np.power(x, 5)
    return (f)

# a & b = limits of integration
# n = number of "trapezoids"
def trapezoidal(a, b, n):

    h = (b - a) / n
    sum = (func(a) + func(b))

    for i in range(0, n):
        sum += 2 * func(a + i * h)

    return ((h / 2) * sum)


# n = int(input("Indice number of trapezoids\n"))
# a = float(input("provide a bound\n"))
# b = float(input("provide b bound\n"))

print("Approximate value for  " + str(n) + " segments is %.4f" % trapezoidal(a, b, n))
