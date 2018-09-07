import math

# Sample function that corresponds to f(a)=(e^-a)-a
def sampleFunction(a):
    result = math.exp(-a)-a
    return result


# PARAMETERS: 
# func = method that returns a numerical value
# x0 = first root of secant
# x1 = second root of secant 
# tol = relative error tolerance 
# maxAttempts = number of iterations that the method will attempt
def normalSecant(func, x0, x1, tol, maxAttempts):
    ctr = 0
    while ctr < maxAttempts:
        x2 = x1 - ((func(x1)*(x0-x1))/(func(x0)-func(x1)))
        print (x2)
        rError = ((x2-x1)/x2)*100
        rError = abs(rError)
        if rError <= tol:
            return x2
        else:
            x0 = x1
            x1 = x2
    return False



# PARAMETERS 
# dif = constant that will render 2nd secant root
def altSecant(func, x, dif, tol, maxAttempts):
    ctr = 0
    while ctr < maxAttempts:
        xI = x - (dif*x*func(x))/(func(x+(dif*x))-func(x))
        print (xI)
        rError = ((xI-x)/xI)*100
        rError = abs(rError)
        if rError <= tol:
            return xI
        else:
            x = xI
    return False

print ("Normal Secant method")
print (normalSecant(sampleFunction, 0, 1, 0.0005, 50))

print ("Modified Secant method")
print (altSecant(sampleFunction, 1, 0.5, 0.0005, 50))
