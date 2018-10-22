import numpy as np
x = [0] * 10
y = np.zeros((10, 10))
accum = None
p = None
u = None
temp = None
k = 0
f = None
m = None
n = int(input("how many points: "))
for i in range(0, n):
    val = input("value of x" + str(i))
    x[i] = float(val)
    val = input("enter value of f(x" + str(i) + "):")
    y[k][i] = float(val)
p = float(input("evaluate f(x) at x:"))
for i in range(1, n):
    k = i
    for j in range(0, n - i):
        y[i][j] = (y[i - 1][j + 1] - y[i - 1][j]) / (x[k] - x[j])
        k += 1

for i in range(0, n):
    print("\n " + str(x[i]), end='')
    for j in range(0, n - i):
        print("\t" + str(y[j][i]), end='')
    print('')
i = 0
while(1):
    if x[i] < p and p < x[i + 1]:
        k = 1
    else:
        i += 1
    if k != 1:
        break
f = i

accum = 0
for i in range(0, n - 1):
    k = f
    temp = 1
    for j in range(0, i):
        temp *= p - x[k]
        k += 1
    accum = accum + float(temp) * float(y[i][f])
print("\n\n f(" + str(p) + ") = " + str(accum))
