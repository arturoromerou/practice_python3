import math
"""Mostrar en pantalla la cantidad de segundos que tiene un lustro."""
anio = 31536000
lustro = 5 * anio
print(lustro, "segundos")

"""Mostrar en pantalla la cantidad de segundos que le toma a la luz viajar del sol a marte y mostrar
en pantalla el resultado"""
distancia = 225000000
velocidad = 299792
tiempo = distancia / velocidad
print(tiempo, "segundos")

"""Calcular el numero de vueltas que da una llanta en 1km, dado que el diametro de la llanta es de 50cm,
mostrar el resultado en pantalla"""
l = 1000
diametro = 0.5
vuelta_kilometro = l / diametro
print(vuelta_kilometro, "vueltas")

"""Calcular la longitud de la sombra de un edificio de 20 metros de altura, cuando el angulo que forman
los rayos del sol con el suelo es de 22 grados"""

co = 20
angulo = 22
hipotenusa = co * math.sin(math.radians(angulo))
sombra = hipotenusa * math.cos(math.radians(angulo))
print(sombra)

"""Mostrar en pantalla True o False si la edad ingresada por dos usuarios es la misma."""

person_1 = 20
person_2 = 20

iguales = person_1 == person_2
print(iguales)


