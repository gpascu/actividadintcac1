'''
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.
'''

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad
    
    def get_titular(self):
        return self.titular.nombre
    
    def set_titular(self, nuevo_titular):
        self.titular = nuevo_titular
    
    def get_cantidad(self):
        return self.cantidad
    
    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.cantidad = nueva_cantidad
    
    def mostrar(self):
        print(f"Titular: {self.get_titular()}")
        print(f"Cantidad: {self.get_cantidad()}")
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad
    
    def retirar(self, cantidad):
        self.cantidad -= cantidad


# Creo una instancia de Persona
titular_persona = Persona("Guillermo Pascu")
# Creo una instancia de Cuenta
cuenta_juan = Cuenta(titular_persona, 1000.0)
# Muestro los datos iniciales de la cuenta
cuenta_juan.mostrar()
# Ingreso dinero en la cuenta
cuenta_juan.ingresar(500.0)
# Muestro los datos después de ingresar dinero
cuenta_juan.mostrar()
# Retiro dinero de la cuenta
cuenta_juan.retirar(200.0)
# Muestro los datos después de retirar dinero
cuenta_juan.mostrar()
