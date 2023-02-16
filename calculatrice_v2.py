#coding:utf-8

from calcul import *

print("\n===== Calculatrice v2 =====")
print("\n 1. Addition\n 2. Soustraction\n 3. Multiplication\n 4. Division\n\n 00. Quitter\n")

ouvert = True 
while ouvert:
	try:
		choix=input("Choix > ")
		choix=int(choix)

		assert 0 <= choix <= 4

	except AssertionError:
		print("===== Tapez un chiffre entre 1 et 4 ! =====")
		continue
	except ValueError:
		print("===== Tapez un chiffre ! =====")
		continue
	except KeyboardInterrupt:
		print("\n\n===== Au revoir ... =====")
		quit()

	if choix==1:
		ouvert = True
		while ouvert:
			try:
				a = int(input("a = "))
				break
			except ValueError:
				print("===== Entrez un chiffre ! =====")
				continue
			except KeyboardInterrupt:
				print("\n\n===== Au revoir ... =====")
				quit()

		ouvert = True
		while ouvert:
			try:
				b = int(input("b = "))
				break
			except ValueError:
				print("===== Entrez un chiffre ! =====")
				continue
			except KeyboardInterrupt:
				print("\n\n===== Au revoir ... =====")
				quit()

		addition( a , b )

	elif choix==2:
		ouvert = True
		while ouvert:
			try:
				a = int(input("a = "))
				break
			except ValueError:
				print("===== Entrez un chiffre ! =====")
				continue
			except KeyboardInterrupt:
				print("\n\n===== Au revoir ... =====")
				quit()

		ouvert = True
		while ouvert:
			try:
				b = int(input("b = "))
				break
			except ValueError:
				print("===== Entrez un chiffre ! =====")
				continue
			except KeyboardInterrupt:
				print("\n\n===== Au revoir ... =====")
				quit()

		soustraction( a , b )

	elif choix==3:
		ouvert = True
		while ouvert:
			try:
				a = int(input("a = "))
				break
			except ValueError:
				print("===== Entrez un chiffre ! =====")
				continue
			except KeyboardInterrupt:
				print("\n\n===== Au revoir ... =====")
				quit()

		ouvert = True
		while ouvert:
			try:
				b = int(input("b = "))
				break
			except ValueError:
				print("===== Entrez un chiffre ! =====")
				continue
			except KeyboardInterrupt:
				print("\n\n===== Au revoir ... =====")
				quit()

		multiplicateur( a , b )

	elif choix==4:
		ouvert = True
		while ouvert:
			try:
				a = int(input("a = "))
				break
			except ValueError:
				print("===== Entrez un chiffre ! =====")
				continue
			except KeyboardInterrupt:
				print("\n\n===== Au revoir ... =====")
				quit()

		ouvert = True
		while ouvert:
			try:
				b = int(input("b = "))
				assert b != 0
				break
			except AssertionError:
				print("===== La division par 0 est Impossible ! =====")
				continue
			except ValueError:
				print("===== Entrez un chiffre ! =====")
				continue
			except KeyboardInterrupt:
				print("\n\n===== Au revoir ... =====")
				quit()

		division( a , b )
		
	elif choix==00: 
		oui_non()