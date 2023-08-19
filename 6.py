'''
Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

'''

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def get_edad(self):
        return self.edad
    
    def set_edad(self, nueva_edad):
        if nueva_edad >= 0:
            self.edad = nueva_edad
    
    def get_dni(self):
        return self.dni
    
    def set_dni(self, nuevo_dni):
        self.dni = nuevo_dni
    
    def mostrar(self):
        print(f"Nombre: {self.get_nombre()}")
        print(f"Edad: {self.get_edad()}")
        print(f"DNI: {self.get_dni()}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18


# Creo una instancia de Persona
persona1 = Persona("Guille Pascu", 33, "34856323")

# Muestro los datos de la persona
persona1.mostrar()

# Verifico si es mayor de edad
if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
