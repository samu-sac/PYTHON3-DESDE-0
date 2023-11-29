#!/usr/bin/python3
#Escribe un programa el cual diga si un numero es primo o no

es_primo = True
numero_es_primo = int(input("Dime un numero para ver si es primo:"))
for num in range(2, numero_es_primo):
	if numero_es_primo % num == 0:
		es_primo = False
		break
if es_primo:
	print("Es primo")
else:
	print("No es primo")
