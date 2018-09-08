import bisectionEuge as bisection
import falsePosition as fp
import newtonRaphson as nr
import secant as secant



def menu() :
	print("Welcome!")
	userOption = input(" 1) Bisection\n 2) False Position\n 3) Newton Raphson\n 4) Secant\n 5) Exit\n")

	if int(userOption) == 1 :
		bisection.start()
	elif int(userOption) == 2 :
		fp.start()
	elif int(userOption) == 3 :
		nr.start()
	elif int(userOption) == 4 :
		secant.start()
	elif int(userOption) == 5 :
		print("Goodbye!")
		exit()
	else :
		print("nothing happened")

menu()