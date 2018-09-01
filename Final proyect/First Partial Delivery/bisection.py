# Numerical methods final project
# Bisection Method
# August '18'

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return ((668.06 / x) * (1 - (exp(1)**(-0.146843*x)) - 40))
def bisection(a,b,tol):
    xl = a
    xr = b
    while (np.abs(xl-xr) >= tol):
        c = (xl+xr)/2.0
        prod = f(xl)*f(c)
        if prod > tol:
            xl = c
        else:
            if prod < tol:
                xr = c
    return c

answer = bisection(12,16,5e-1)
print(" bisection method gives root at x = ", answer)
x = np.linspace(-2,2,5)
plt.plot(x,f(x))
plt.grid()
plt.show()
