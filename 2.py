#Escribir una función que calcule el mínimo común múltiplo entre dos números

def calcular_mcm(a, b):
    def calcular_mcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    return abs(a * b) // calcular_mcd(a, b)

# Pedir al usuario dos números enteros
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Calcular y mostrar el mcm
mcm = calcular_mcm(num1, num2)
print(f"El Mínimo Común Múltiplo de {num1} y {num2} es: {mcm}")
