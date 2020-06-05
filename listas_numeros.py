"""Crear una lista la cual almacene 10 numeros positivos ingresados por el usuario, mostrar en pantalla:
la suma de todos los numeros, el promedio, el numero mayor y el numero menor"""

elemento = int(input("ingrese un valor: "))
if elemento < 0:
        print('Error solo numeros positivos')
        exit()
lista_numeros = [elemento]
cantidad = len(lista_numeros)

while cantidad <= 9:
    elemento = int(input("ingrese un valor: "))
    if elemento < 0:
        print('Error solo numeros positivos')
        exit()
    agregar = lista_numeros.append(elemento)
    cantidad += 1

print('\nlos valores ingresados son:', lista_numeros)
print('\nla suma es:', sum(lista_numeros))
print('el promedio es:', sum(lista_numeros) / 10)
print('el valor maximo es:', max(lista_numeros))
print('el valor minimo es:', min(lista_numeros))