'''
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
'''

def contar_palabras(cadena):
    palabras = cadena.split()
    frecuencia = {}    
    for palabra in palabras:
        palabra = palabra.lower()  # Convierto a minúsculas para evitar distinción entre mayúsculas y minúsculas
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    return frecuencia

# Pedir al usuario una cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")

# Obtener el diccionario de frecuencias de palabras
diccionario_frecuencias = contar_palabras(cadena)
print("Diccionario de frecuencias:", diccionario_frecuencias)
