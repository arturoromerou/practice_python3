def suma(a, b):
    """funcion suma"""
    return a + b

def resta(a, b):
    """funcion resta"""
    return a - b

opciones =  {'a': suma, 'b': resta}
print("ingrese la opcion")

for opcion, funcion in opciones.items():
    mensaje = '{}) {}'.format(opcion, funcion.__doc__)
    print(mensaje)

opcion = input("opcion : ")