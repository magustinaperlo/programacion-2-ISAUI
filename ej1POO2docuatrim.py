# Ejercicio 1 
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
# Un constructor, donde los datos pueden estar vacíos.
# Los setters y getters para cada uno de los atributos. 
# Hay que validar las entradas de datos. 
# mostrar(): Muestra los datos de la persona.  
# esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

import os
os.system("cls")

class Persona():
    def __init__ (self, nombre, edad, documento):
        self.nombre = nombre or ""
        self.edad = edad or 0 or " "
        self.documento = documento or ""
    
    @property
    def getNombre(self):
        return self.nombre
    @property
    def getEdad(self):
        return self.edad
    @property
    def getDocumento(self):
        return self.documento
    
    def setNombre(self,nombre):
        self.nombre = nombre
    def setEdad(self,edad):
        self.edad = edad
    def setDocumento(self,documento):
        self.documento = documento
 
    def mostrar(self):
        print(f"Datos ingresados: \nNombre completo: {self.getNombre} \nEdad: {self.getEdad} \nDNI: {self.getDocumento} \n")
    def esMayorDeEdad(getEdad):
        if edad =="":
            pass
        if edad >= 18:
            print("Es mayor de edad")
            return True
        else:
            print("Es menor de edad")
            return False               
finNom = False
while (finNom != True):
    nombre =input("Ingrese su nombre completo: ")
    if nombre == "":
        pass    
    list(nombre)
    if (nombre.isnumeric()):
        print("Dato erroneo, ingreso un numero")
        finNom = False
    elif(len(nombre)<2):
        print("Ingrese una opcion valida")
        finNom = False
    else:
        finNom = True

while True:
    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Debe escribir un número y que no sea decimal")
        continue
    if edad < 0:
        print("Debe escribir un número positivo.")
        continue
    else:    
        break
finDoc = False
while (finDoc != True):
    documento = input("Ingrese su numero de documento: ")
    if documento == "":
        pass
    list(documento)
    if (documento.isnumeric() and len (documento) == 8):
        print("Ingreso correcto")
        finDoc = True
    elif(len(documento)<2):
        print("Ingrese una opcion valida")
        finDoc = False
    else:
        print("Ingreso incorrecto ")
        finDoc = False

    
pers = Persona(nombre,edad,documento)
pers.mostrar()
pers.esMayorDeEdad()