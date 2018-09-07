#A01022285
# Numerical Methods
# August '18'

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - np.cos(x)
def Df(x):
    return 3* x**2 + np.sin(x)

x0 = 1;
i = 1;
error = 10;
while error > 1e-6:
    x1 = x0 - f(x0) / Df(x0)
    error = abs(x1 - x0)
    x0 = x1
    print("Iteracion", i, ", raiz aproximada: ",x0)
    i = i + 1
    
