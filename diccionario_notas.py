"""Dado un diccionario, el cual almacena las calificaciones de un alumno, siendo las llaves los nombres de las
materias y los valores las calificaciones, mostrar en pantalla el promedio del alumno."""
print('lista de materias con sus notas:')
notas = {'matematica': 12, 'fisica': 15, 'ingles': 19}
promedio = sum(notas.values()) / 3

print(notas)
print('\ntu promedio de notas es:', promedio, 'pts')

"""A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio"""
obtener_notas = notas.values()
obtener_materias = notas.keys()
nueva_notas = list(obtener_notas)
nueva_materias = list(obtener_materias)
print('\nla materia con la mayor nota fue', max(nueva_materias), 'con', max(nueva_notas), 'pts')