"""Mostar en pantalla el promedio de un alumno que ha cursado 5 materias(espaniol, matematicas, economia,
programacion, ingles)."""

espaniol = int(input("Nota de espaniol: "))
if espaniol > 20:
    print("Error")
    exit()
matematicas = int(input("Nota de matematicas: "))
if matematicas > 20:
    print("Error")
    exit()
economia = int(input("Nota de economia: "))
if economia > 20:
    print("Error")
    exit()
programacion = int(input("Nota de programacion: "))
if programacion > 20:
    print("Error")
    exit()
ingles = int(input("Nota de ingles: "))
if ingles > 20:
    print("Error")
    exit()

total = espaniol + matematicas + economia + programacion + ingles
promedio = total / 5
print("Tu promedio de notas es:", promedio)

