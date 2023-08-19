#Escribir una función que calcule el máximo común divisor entre dos números.
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def maxComunDivisor(num1, num2):
    if num1 == 0 or num2 == 0:
        return None  # No esta definida para cero
    return mcd(abs(num1), abs(num2))

#procedo a hacer las pruebas
num1 = int(input("Ingresar el primer numero: "))
num2 = int(input("Ingresar el segundo numero: "))
mcdF = maxComunDivisor(num1, num2)

print(f"El maximo comun divisor de {num1} y {num2} es {mcdF}")
