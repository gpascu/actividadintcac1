'''
Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.
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

def palabra_mas_repetida(frecuencia_palabras):
    if not frecuencia_palabras:
        return None, 0
    
    palabra_max_frecuencia = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frecuencia_maxima = frecuencia_palabras[palabra_max_frecuencia]
    
    return (palabra_max_frecuencia, frecuencia_maxima)

# Realizo la prueba :
cadena = input("Ingrese una cadena de caracteres: ")
diccionario_frecuencias = contar_palabras(cadena)
resultado = palabra_mas_repetida(diccionario_frecuencias)
print("Palabra más repetida y su frecuencia:", resultado)
