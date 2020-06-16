"""Mostrar en pantalla la cantidad de vocales que existen en una frase dada por el usuario"""

text = input("Introduzca una palabra o frase")
text = text.lower()
print('\nlas vocales que se repiten son: \n') 

for i in range(0, len(text)):
    count = 1 # Se le asigna el valor 1 a la variable count porque minimo debe exister 1 vez la palabra
    # Se establece un nuevo rango de inicio en la nueva variable
    for j in range(i+1, len(text)):
        # Si las palabras en i y j son iguales se le suma 1 a count
        if(text[i] == (text[j])):
            count = count + 1
            text[j] = False
# Muestra la palabras duplicadas si count es mayor que 1  
    if(count >= 1 and text[i] != "0" and text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u'):
        print(text[i], 'se repite', count, 'veces')

"""Mostrar en pantalla la frecuencia de aparicion de vocales en una frase dada por el usuario"""

"""Eliminar todas las vocales de una frase dada por el usuario y mostrar el nuevo string"""

"""Listar todos los numeros pares del 0 al 100"""
