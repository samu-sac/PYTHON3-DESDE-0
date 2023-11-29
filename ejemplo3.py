#!/usr/bin/python3
indicador = False
for var in range(1,6):
        num = int(input("Dime un numero:"))
        if num % 2 == 0:
                indicador = True
if indicador:
	print("has introducido algun numero par")
else:
	print("NO has introducido numeros pares")
