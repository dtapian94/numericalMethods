# Daniel Tapia Nava
# Metodos numericos en ingenieria
# LU Decomposition

import numpy as np

print ("LU Decomposition para matrices cuadradas")
print ("Cuadradas quiere decir que el numero de renglones sera el mismo que el de columnas ")

m = int(input("Introduzca el numero de renglones: "))
matriz = np.zeros([m,m])
u = np.zeros([m,m])
l = np.zeros([m,m])
vector = np.zeros((m))


print ("Introduzca los elementos de la matriz: ")
for r in range (0,m):
	for c in range (0,m):
		matriz[r,c] = (input("Elemento a["+str(r+1)+","+str(c+1)+"] : "))
		matriz[r,c] = float (matriz[r,c])
		u[r,c] = matriz[r,c]

#print ("Introduzca los valores del vector solucion: ")
#for i in range (0,m):
	#vector[(i)]  = (input('V['+str(i +1)+']: '))

#Operaciones para obtener ceros debajo de la diagonal principal

for k in range (0,m):
	for r in range (0,m):
		if (k == r):
			l[k,r] = 1
		if (k < r):
			factor = (matriz[r,k] / matriz [k,k])
			l[r,k] = factor
			for c in range (0,m):
				matriz[r,c] = matriz [r,c] - (factor*matriz[k,c])
				u[r,c] = matriz [r,c]

print ("Resultados: ")
print ("Matriz L")
print (l)

print ("Matriz U")
print (u)

#print("Pruebas: ")
#print("\n")

#print("Primer renglon:")
#print("\n")
#print (l[0])
#x1 = {sum(l[i]) for i in range(1)}
#x2 = next(iter(x1))
#v1 = vector[0]
#resX1 = x2 + v1
#print (resX1)


#print ("Segundo renglon: ")
#print("\n")
#print (l[1])
#x3 = [sum(l[i+1]) for i in range(1)]
#x4 = next(iter(x3))
#v2 = vector[1]
#resx2 = x4 + v2
#print (resx2)


#print ("tercer renglon: ")
#print ("\n")
#print (l[2])
#x5 = [sum(l[i+2]) for i in range(1)]
#x6 = next(iter(x5))
#v3 = vector[2]
#resx3 = x6 + v3
#print (resx3)




#Comprobacion
print ("Comprobacion")
matrizr = np.zeros([m,m])
for r in range (0,m):
	for c in range (0,m):
		for k in range (0,m):
			matrizr[r,c] += (l[r,k] * u[k,c])
print (matrizr)
