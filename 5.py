'''
Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva.

'''
#en modo iterativo
def get_int_iterativa():
    while True:
        try:
            num1 = input("Ingresa un int: ")
            int1 = int(num1)
            return int1
        except ValueError:
            print("Ingreso inválido. Ingresa un int válido")
# Procedo con la prueba:
res1 = get_int_iterativa()
print("You entered:", res1)


#en modo recursivo
def get_int_recursiva():
    try:
        num2 = input("Ingresa un int: ")
        int2 = int(num2)
        return int2
    except ValueError:
        print("Ingreso inválido. Ingresa un int válido")
        return get_int_recursiva()
# procedo con la prueba
res2 = get_int_recursiva()
print("You entered:", res2)

