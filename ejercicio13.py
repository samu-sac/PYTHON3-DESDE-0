#!/usr/bin/python3
#Escribe un programa que pda una fecha (día, mes y año) y diga si la fecha es correcta o no
# fecha correcta = dia < que los dias q tiene ese mes ese año

dia = int(input("Introduce el dia:"))
mes = int(input("Introduce el mes:"))
anio = int(input("Introduce el año:"))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
	dias_del_mes = 31;
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
	dias_mes_año = 30;
elif mes == 2:
	if (anio % 4 == 0 and not (anio % 100 == 0)) or anio % 400 == 0:
		dias_del_mes = 29;
	else:
		dias_del_mes = 28;
else:
	print("Fecha incorrecta")

if dia < 0 or dia > dias_del_mes:
	print("Fecha incorrecta")
else:
	print("Fecha correcta")
