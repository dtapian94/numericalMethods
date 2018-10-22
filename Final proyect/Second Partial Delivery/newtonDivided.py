import numpy as np
def newtonDivided(numPoints, xs, ys, xToEval):
    table = np.zeros((numPoints, numPoints + 1))
    ys1 = ys
    for i in range(numPoints):
        table[i][0] = xs[i]
        table[i][1] = ys[i]

    for iteration in range(1, numPoints - 1):
        for i in range(0, numPoints - iteration):
            table[i][iteration + 1] = (ys1[i + 1] - ys1[i]) / (xs[i + 1] - xs[i])
            print(str(ys1[i + 1]) + " - " + str(ys1[i]) + " / " + str(xs[i + 1]) + " - " + str(xs[i]) + " = " + str(table[i][iteration + 1]))
        for i in range(numPoints):
            ys1[i] = table[i][iteration]
    toprint = "\n"
    for i in table:
        for j in i:
            toprint += str(j) + "\t"
        toprint += "\n"
    print(toprint)

def newtonDivided2(numPoints, xs, ys, xToEval):
    table = np.zeros((10, 10))
    for i in range(numPoints):
        table[i][1] = ys[i]
    toprint = ""
    for i in table:
        for j in i:
            toprint += str(j) + " "
        toprint += "\n"
    print(toprint)
    for i in range(1, numPoints):
        k = i
        for j in range(0, numPoints - i):
            table[i][j] = (table[i - 1][j + 1] - table[i - 1][j]) / (xs[k] - xs[j])
            k += 1
    returnString = ""
    for i in range(0, numPoints):
        returnString += "\n " + str(xs[i])
        for j in range(0, numPoints - i):
            returnString += "   " + str(table[j][i])
        returnString += "\n"
    i = 0
    while(1):
        if xs[i] < xToEval and xToEval < xs[i + 1]:
            k = 1
        else:
            i += 1
        if k != 1:
            break
    f = i
    accum = 0
    for i in range(0, numPoints - 1):
        k = f
        temp = 1
        for j in range(0, i):
            temp *= xToEval - xs[k]
            k += 1
        accum = accum + temp * int(table[i][f])
    returnString += "\n\n " + str(xToEval) + str(accum)
    return returnString

print(newtonDivided(5, [2.5, 3, 4.5, 4.75, 6], [8.85, 11.45, 20.66, 22.85, 38.60], 3.5))
