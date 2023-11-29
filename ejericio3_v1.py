#!/usr/bin/python3
# algoritmo que pida numeros hasta que se introduzca cero
# debe imprimir la suma y la edia de todos los numero introducidos
suma = 0
cont = 0

num = int(input("Número (0 para salir):"))
while num != 0:
	suma = suma + num
	cont = cont + 1
	num= int(input("Número (0 para salir):"))

if cont > 0:
	media =  suma / cont
else:
	media = 0

print("Suma:", suma)
print("Media:", media)
