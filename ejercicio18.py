#!/usr/bin/python3
#Pedir el nombre y los dos apellidos de una persona
# Y mostrar las inciiales.
nombre = input("Dime tu nombre:")
apellido1 = input("Dime tu primer apellido:")
apellido2 = input("Dime tu segundo apellido:")

#Seleccionamos las iniciales
inicial = nombre[0]
inicial = inicial + apellido1[0]
inicial = inicial + apellido2[0]

#Convertimos las iniciales en mayúsuclas mediante upper
inicial = inicial.upper()
print("Las iniciales son:", inicial)
