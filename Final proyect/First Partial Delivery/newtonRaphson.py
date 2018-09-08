#A01022285
# Numerical Methods
# August '18'

# import numpy as np
# import matplotlib.pyplot as plt
from math import *

formula = ''
derivative = ''
x0 = 0
maxIterations = 0
tolerance = 0

def f(x) :
    global formula
    return eval(formula)

def Df(x) :
    global derivative
    return eval(derivative)

def getUserInputNR() :
    global formula, derivative, x0, tolerance, maxIterations
    formula = input('Introduce formula with unknown variable x: ')
    derivative = input('Introduce the derivative of the function with unknown variable x: ')
    print("Guesses for root")
    x0 = float(input('x0: '))
    tolerance = float(input('tolerance percent: '))
    maxIterations = int(input('maximum number of iterations: '))

def newtonRaphson(x0, tolerance, maxIterations) :
    i = 1
    error = 100 # Start with 100% error
    while error > tolerance :
        if i == maxIterations :
            break
        x1 = x0 - f(x0) / Df(x0)
        error = abs(x1 - x0) * 100
        x0 = x1
        # print("Iteracion", i, ", raiz aproximada: ",x0)
        i = i + 1
    return "Result: " + str(x0) + " Iteration: " + str(i) + " aproximate percent relative error: " + str(error)
    
def start() :
    global x0, tolerance, maxIterations
    print("Welcome to Newton Raphson program")
    getUserInputNR();
    print(newtonRaphson(x0, tolerance, maxIterations))