#Vamos a definir ahora una “Cuenta Joven”, 
# para ello vamos a crear una nueva clase CuantaJoven 
# que deriva de la anterior. Cuando se crea esta nueva 
# clase, además del titular y la cantidad se debe guardar 
# una bonificación que estará expresada en tanto por ciento.
# Construye los siguientes métodos para la clase:
# a)Un constructor.
# b)Los setters y getters para el nuevo atributo.
# c)En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad., 
# por lo tanto hay que crear un método esTitularValido() que devuelve verdadero si 
# el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# d)Además la retirada de dinero sólo se podrá hacer si el titular es válido.
# e)El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación 
# de la cuenta.
# Piensa los métodos heredados de la clase madre que hay que reescribir.


import os
os.system("cls")

class Cuenta: 

    def __init__ (self, titular, cantidad):  
        self.titular = titular or "" 
        self.cantidad = cantidad or ""
       
    @property
    def getTitular(self):
        return self.titular
    def getCantidad(self):
        return self.cantidad

    def titular(self,titular):
        self.titular = titular
    def cantidad(self,cantidad):
        self.cantidad = cantidad
    def mostrar(self):
        print(f"Datos ingresados: \nNombre del titular: {self.titular} \nCantidad: ${self.cantidad} \n")
    

class CuentaJoven (Cuenta):
    def __init__ (self, titular, cantidad, edad, bonificacion):
        super().__init__(titular,cantidad)
        self.edad = edad
        self.bonificacion = bonificacion
          
    def getEdad (self):
        return self.edad
    def getBonificacion(self):
        return self.bonificacion

    def setEdad (self, edad):
        self.edad = edad
    def setBonificacion(self,bonificacion):
        self.bonificacion = bonificacion

    def esTitularValido(self):
        if self.edad >=18 and self.edad <=25:            
            return True
        else:    
            return False
    
    def mostrar(self):
        super().mostrar()
        if self.esTitularValido() == False:
            print("Su edad no lo habilita para tener una Cuenta Joven")
            print("Su cuenta no tiene bonificaciones")
            print("No esta habilitado para retirar dinero de una Cuenta Joven")
        else:
            print("Bienvenido a su Cuenta Joven")
            print(f"Su Cuenta Joven tiene una bonificacion de {self.bonificacion} %")
    
    
    def acreditacion(self):
        if self.esTitularValido() == True:
            acreditacion = round(((cantidad) * self.bonificacion/100),2) 
            print(f"Su bonificacion representa un total de $ {acreditacion}")
   
    def retirar (self):
        if self.esTitularValido() == True: 
            while True:
                try:
                    retiro = float(input("Ingrese la cantidad de dinero a retirar: "))     
                except ValueError:
                    print("Dato erroneo, por favor escribe un numero.")
                    continue
                else:
                    break
            print(f"Ud ha retirado de su cuenta la suma de $ {retiro}")
            self.cantidad = self.cantidad - retiro
            print (f"En su cuenta ahora tiene $ {self.cantidad}")
        
finTit = False
while (finTit != True):
    titular =input("Ingrese su nombre completo: ")
    if titular == "":
        pass    
    list(titular)
    if (titular.isnumeric()):
        print("Dato erróneo, Ud ingresó un número")
        finTit = False
    elif(len(titular)<2):
        print("Ingrese una opcion válida")
        finTit = False
    else:
        finTit = True
while True:
    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Debe escribir un número y que no sea decimal")
        continue
    if edad < 0:
        print("Debe escribir un número positivo.")
        continue
    if edad >=100:
        print ("Debe ingresar una edad menor")
        continue
    else:    
        break
while True:
    try:
        cantidad = float(input("Ingrese fondos disponibles: "))
    except ValueError:
        print("Debe escribir un número")
        continue
    if cantidad < 0:
        pass
    else:    
        break
while True:
    try:
        bonificacion = float(input("Ingrese el porcentaje de bonificacion que recibe: "))
    except ValueError:
        print("Debe escribir un número")
        continue
    if bonificacion < 0:
        print("Debe ingresar un porcentaje positivo")
    else:    
        break

joven = CuentaJoven(titular,cantidad,edad,bonificacion)
joven.esTitularValido()
joven.mostrar()
joven.acreditacion()
joven.retirar()



        