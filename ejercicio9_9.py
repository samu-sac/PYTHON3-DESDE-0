#!/usr/bin/python3
#Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos cadenas se introducen por teclado.
cad = input("Introduce la cadena:")
subcad = input("Introduce la subcadena:")

if cad.fin(subcad) > -1:
	print("La cadena contiene la subcadena.")
else:
	print("La cadena no contiene la subcadena")
#Otra forma de comprobarlos
if subcad in cad:
	print("La cadena contiene al subcadena.")
else:
	print("La cadena no contiene la subcadena.")
