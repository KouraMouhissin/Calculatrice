#coding:utf-8

import calcul

try :
	a = input("Entrer un nombre >")
	b = input("Entrer un autre nombre >")

	cal = calcul.Calculatrice(int(a), int(b))

	print(f"l'addition de ces deux est {cal.addition()}")
	print(f"la soustration de ces deux est {cal.soustraction()}")
	print(f"la multiplication de ces deux est {cal.multiplicateur()}")
	print(f"la division de ces deux est {cal.division()}")
	print(f"le modulo de ces deux nombre est {cal.modulo()}")
except:
	print("une erreur c'est produite")




