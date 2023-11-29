#!/usr/bin/python3
resultado = 1
num = int(input("Dime un numero:"))
for contador in range(2, num+1):
	resultado = resultado * contador
print("El resultado es", resultado)
