""""
Created on Thu Oct 11 15:01:24

@author: Eduardo Badillo Á
"""

print("Lagrange Interpolation Method")

# Input points and x to be evaluated
n = int(input('Enter number of points to be inserted'))

Xs = []
Ys = []

for i in range(0, n):
    Xs.append(float(input('Input X' + str(i+1))))
    Ys.append(float(input('Input Y' + str(i+1))))

x = float(input('Enter x to be evaluated'))


# Begin method
result = 0
result = float(result)
for i in range(0, n):
    pie = 1
    for j in range(0, n):
        if i != j:  # this if st. prevents the current x to be subtracted by itself in the denominator
            pie *= (x - Xs[j]) / float(Xs[i] - Xs[j])  # This var represents the iterative product notation letter "pi"
    pie *= Ys[i]
    result += pie
    print(result)

print('The value at x = ' + str(x) + " is " + str(result))
print('Suggestion: to improve the result you should try to insert various points')