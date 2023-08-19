'''
 Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.
'''

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
#------------------------------------
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
#--------------------------------
class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.bonificacion
    
    def set_bonificacion(self, nueva_bonificacion):
        if nueva_bonificacion >= 0:
            self.bonificacion = nueva_bonificacion
    
    def es_titular_valido(self):
        # Verifico que el titular sea mayor de edad y menor de 25 años
        edad = self.titular.edad
        return 18 <= edad < 25
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("No es posible retirar dinero. Titular no válido.")
    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print(f"Bonificación: {self.get_bonificacion()}%")

# Clase para representar al titular de la cuenta
class Titular:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Prueba 1:
titular_joven = Titular("Juan", 22)
cuenta_joven = CuentaJoven(titular_joven, 1000, 5)
cuenta_joven.mostrar()
cuenta_joven.retirar(200)
cuenta_joven.mostrar()

print("-----------------")
# Prueba 2:
titular_joven = Titular("Pepe", 29)
cuenta_joven = CuentaJoven(titular_joven, 700, 5)
cuenta_joven.mostrar()
cuenta_joven.retirar(200)
cuenta_joven.mostrar()