#!/usr/bin/python3
#Suponiendo que hemos introducido una cadena por teclado
#que representa una frase (palabras separadas por espacios),
#realiza un programa que cuente cuantas palabras tiene.

cont = 0
posicion = 0
cad = input("Introduce una cadena:")
#Eliminar posibles espacios al principio o al final
cad = cad.strip()
#Buscando espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
	cont = cont + 1
	#tener en cuenta los espacios entre las palabras
	while cad[posicion + 1] == " ":
		posicion = posicion + 1
	posicion = cad.find(" ", posicion + 1)
print("La frase tiene",cont + 1,"palabras.")
