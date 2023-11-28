#!/usr/bin/python3
horapartida = int(input("Hora de la salida:"))
minpartida = int(input("Minuto de la salida:"))
segpartida = int(input("Segundo de la salida:"))
segviaje = int(input("Tiempo que has tardado en segundos:"))
#Convierto la hora de la salida a segundos
seginicial = horapartida * 3600 + minpartida*60 + segpartida;
#Le sumo los segundos que ha tardado
segfinal = seginicial + segviaje;
#Convierto los segundos totales a hora, minuto y segundo
horallegada = segfinal // 3600;
minllegada = (segfinal % 3600) // 60;
segllegada = (segfinal % 3600) % 60;
#Muestro la hora de llegada
print("Hora de llegada")
print(horallegada, ":", minllegada, ":", segllegada)
