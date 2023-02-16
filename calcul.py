#coding:utf-8

"""
Module de Calcul pour la calculatrice !

choix_q=input("Voulez vous Quitter ? (o/n) ")
		if choix_q=="o" or choix_q=="O":
			print("Au revoir...")
			break
		elif choix_q=="n" or choix_q=="N":
			continue
"""

def multiplicateur(a,b):
	print(a," X ", b, " = ",a*b,"\n")
   
def addition(a,b):
	print(a," + ", b, " = ",a+b,"\n")

def soustraction(a,b):
	print(a," - ", b, " = ",a-b,"\n")

def division(a,b):
	print(a," / ", b," = ", a/b,"\n")

def oui_non():
	ouvert = True
	while ouvert:
		try:
			a=input("Voulez vous Quitter ? (o/n) ")

			if a=="o" or a=="O":
				print("\n\n===== Au revoir ... =====")
				quit()
			elif a=="n" or a=="N":
				pass
			else:
				print("\n===== Choissez o/O ou n/N ! =====\n")
				continue
		except KeyboardInterrupt:
			print("\n\n===== Au revoir ... =====")
			quit()


# POUR TESTER LE MODULE SEULEMENT 
if __name__ == "__main__":
	print("=== Phase de Test ===\n")

	multiplicateur(5,6)
	addition(5,6)
	soustraction(5,6)
	division(5,6)
	oui_non()