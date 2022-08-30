import os
os.system("cls")

class Persona():
    def __init__ (self, nombre, edad, documento):
        self.nombre = nombre or ""
        self.edad = edad or 0 or " "
        self.documento = documento or ""
    
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getDocumento(self):
        return self.documento
    
    def setNombre(self,nombre):
        self.nombre = nombre
    def setEdad(self,edad):
        self.edad = edad
    def setDocumento(self,documento):
        self.documento = documento
 
    def mostrar(self):
        print(f"Datos ingresados: \nNombre completo: {self.getNombre()} \nEdad: {self.getEdad()} \nDNI: {self.getDocumento()} \n")
    
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
#permite ingresar nombres de 2 caracteres, nombre apellido y 1 número, "m+" ,"m3"
while (finNom != True):
    nombre =input("Ingrese su nombre completo: ")
    if nombre == "":
        pass    
    list(nombre)
    if (nombre.isnumeric()):
        print("Dato erróneo, Ud ingresó un número")
        finNom = False
    elif(len(nombre)<2):
        print("Ingrese una opcion válida")
        finNom = False
    else:
        finNom = True

while True:
    try:
        edad = int(input("Ingrese su edad: "))
        #permite ingresar espacio y un numero, ejemplo: " 6"
    except ValueError:
        print("Debe escribir un número y que no sea decimal")
        continue
    if edad < 0:
        print("Debe escribir un número positivo.")
        continue
    if edad >=100:
        #sugerir cuál es el límite máx.En este caso vos determinaste que sea menor a 100 pero podrías añadir esa info al msjito de error para guiar al usuario
        print ("Debe ingresar una edad menor")
        continue
    else:    
        break
finDoc = False

while (finDoc != True):
    documento = input("Ingrese su número de documento: ")
    if documento == "":
        pass
    list(documento)
    if (documento.isnumeric() and len (documento) == 8):
        #no admite dni de 6 caracteres como las personas que tienen el valor de su libreta cívica
        #permite que ingreses un espacio y le des enter
        finDoc = True
    elif(len(documento)<6):
        print("Ingrese una opcion válida")
        finDoc = False
    else:
        print("Ingreso incorrecto, debe contener 8 dígitos ")
        finDoc = False

    
pers = Persona(nombre,edad,documento)
print("-" *50)
pers.mostrar()
pers.esMayorDeEdad()
