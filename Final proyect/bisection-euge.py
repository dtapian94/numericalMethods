import sys
from math import *

# You can manually set the values for testing
# Make sure to choose lower and upper guesses for root such that function changes sign over the interval
formula = ''
xlow = 0.0
xupper = 0.0
tolerance = 0
maxIterations = 0

def f(x) :
    global formula
    return eval(formula)

def bisection(xlow, xupper, tolerance, imax) :

	aproxRelativeError = 99999999
	iterations = 0

	# First iteration

	# Estimate resultant x with: xres = (xlow + xupper)/2
	xres = (xlow + xupper) / 2.0

	# Make the following evaluations:
	testing = f(xlow) * f(xres)

	# if f(xlow) * f(xres) < 0 # negative
	# root is in lower subinterval so:
	# xupper = xres
	if testing < 0 :
		xupper = xres

	# if f(xlow) * f(xres) > 0 # positive
	# root is in upper subinterval so:
	# xlow = xres
	if testing > 0 :
		xlow = xres

	# if f(xlow) * f(xres) = 0 # solution found
	elif testing == 0 :
		aproxRelativeError = 0

	# Comment used for debugging
	# print("xlow: " + str(xlow) + " xupper: " + str(xupper) + " res: " + str(xres))

	# Starting iterations
	# Loop until tolerance or max number of iterations is reached
	while (aproxRelativeError > tolerance and iterations < imax) :
		# Store old result for aproximate percent relative error
		xresOld = xres

		# Make the same evaluations:
		testing = f(xlow) * f(xres)

		if testing < 0 :
			xupper = xres

		elif testing > 0 :
			xlow = xres

		elif testing == 0 :
			aproxRelativeError = 0

		# Update to new result aproximation
		xres = (xlow + xupper) / 2.0

		# Get aproximate percent relative error
		if xres != 0 :
			aproxRelativeError = abs((xres - xresOld) / xres) * 100

		# Comment used for debugging
		# print("xlow: " + str(xlow) + " xupper: " + str(xupper) + " res: " + str(xres) + " aproxRelativeError: " + str(aproxRelativeError))

		# Done with iteration
		iterations += 1
	return str(iterations) + " iterations. Result: " + str(xres) + " %" + str(aproxRelativeError) + " aproximate percent relative error"

def getUserInput() :
	global formula, xlow, xupper, tolerance, maxIterations
	formula = input('Introduce formula with unknown variable x: ')
	print("Make sure to choose lower and upper guesses for root such that function changes sign over the interval")
	xlow = float(input('xlower: '))
	xupper = float(input('xupper: '))
	tolerance = float(input('tolerance percent: '))
	maxIterations = int(input('maximum number of iterations: '))

# Example formulas

# Formula for the drag coefficient of parachute diver found in Numerical Methods book
# where xlow = 12, xupper = 16, tolerance = 0.5
# formula = '((668.06 / x) * (1 - (exp(1)**(-0.146843*x)) - 40))'

# Where xlow = 5, xupper = 10 tolerance = 0.09
# formula = '(-0.5)*(x**2) + (2.5 * x) + 4.5'

# where xlow = 0.5, xupper = 1.0, tolerance = 0.2
# formula = '((-25) + (82*x) - (90*(x**2)) + (44*(x**3) - (8*(x**4)) + (0.7*(x**5))))'

def main() :
	global formula, xlow, xupper, tolerance, maxIterations

	if(len(sys.argv) == 1) :
		print('Welcome to Bisection Program:\nThis program can work with arguments or it will prompt you to type each value one by one')
		userOption = input("1) Continue and type each value\n2) Exit program and try with arguments\n")
		if(int(userOption) == 1) :
		  getUserInput()
		  print(bisection(xlow, xupper, tolerance, maxIterations))
		else :
		  print("\nMake sure to pass 5 arguments. \n1) Formula with unknown variable 'x' (required) \n2) xlow\n3) xupper\n4) tolerance\n5) maximum number of iterations\n") 
		  exit()
	elif (len(sys.argv) == 6) :
		formula = sys.argv[1]
		xlow = float(sys.argv[2])
		xupper = float(sys.argv[3])
		tolerance = float(sys.argv[4])
		maxIterations = int(sys.argv[5])
		print(bisection(xlow, xupper, tolerance, maxIterations))
	else :
		print("\nError: Missing argument. Make sure to pass 5 arguments. \n1) Formula with unknown variable 'x' (required) \n2) xlow\n3) xupper\n4) tolerance\n5) maximum number of iterations\n")

main()