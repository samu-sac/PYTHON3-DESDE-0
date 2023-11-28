#!/usr/bin/python3
a = int(input("Introduce el valor de la variable a:"))
b = int(input("Introduce el valor de la variable b:"))
aux = a
a = b
b = aux
print("Nuevo valor de a:", a)
print("Nuevo valor de b:", b)
