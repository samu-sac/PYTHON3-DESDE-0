#!/usr/bin/python3
#Realizar una tabla de multiplicar de un numero introducido por teclado

tabla = int(input("¿De que numero quieres mostar la tabla de multiplicar?"))
for num in range(1, 11):
	print("%d * %d = %d" % (num,tabla,num*tabla))
