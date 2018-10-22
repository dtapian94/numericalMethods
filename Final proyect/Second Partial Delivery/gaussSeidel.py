import numpy as np

numOfEquations = 2
squareMatrix = np.zeros((numOfEquations, numOfEquations))
variables = ["x", "x1", "mivariable", "y"]
results = np.zeros(numOfEquations)

def gauss(matrix, variables, results):
    print("")
