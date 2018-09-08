from math import *

formula = ''
x0 = 0
diff = 0.5
maxIterations = 0
tolerance = 0

# Sample function that corresponds to f(a)=(e^-a)-a
def sampleFunction(a):
    result = math.exp(-a)-a
    return result


def f(x) :
    global formula
    return eval(formula)

# PARAMETERS: 
# func = method that returns a numerical value
# x0 = first root of secant
# x1 = second root of secant 
# tol = relative error tolerance 
# maxAttempts = number of iterations that the method will attempt
def normalSecant(func, x0, x1, tol, maxAttempts):
    ctr = 0
    while ctr < maxAttempts:
        x2 = x1 - ((f(x1)*(x0-x1))/(f(x0)-f(x1)))
        print (x2)
        rError = ((x2-x1)/x2)*100
        rError = abs(rError)
        if rError <= tol:
            return x2
        else:
            x0 = x1
            x1 = x2
    return "max iter reached: result:" + str(x2) + "error: " + str(rError)



# PARAMETERS 
# dif = constant that will render 2nd secant root
def altSecant(x, diff, tol, maxAttempts):
    iteration = 1
    rError = 100 # Start with 100% error
    while rError >= tolerance:
        if iteration == maxAttempts :
            break
        xI = x - (diff*x*f(x))/(f(x+(diff*x))-f(x))
        rError = abs((xI-x)/xI) * 100
        x = xI
        iteration += 1
    return "Result: " + str(xI) + " Iteration: " + str(iteration) + "aproximate percent relative error: " + str(rError)

def getUserInputSecant() :
    global formula, derivative, x0, tolerance, maxIterations
    formula = input('Introduce formula with unknown variable x: ')
    print("Guesses for root")
    x0 = float(input('x0: '))
    tolerance = float(input('tolerance percent: '))
    maxIterations = int(input('maximum number of iterations: '))


def start() :
    global x0, diff, tolerance, maxIterations
    print("Welcome to Secant Program")
    getUserInputSecant()
    print(altSecant(x0, diff, tolerance, maxIterations))

# print ("Normal Secant method")
# print (normalSecant(sampleFunction, 0, 1, 0.0005, 50))

# print ("Modified Secant method")
# print (altSecant(sampleFunction, 1, 0.5, 0.0005, 50))
