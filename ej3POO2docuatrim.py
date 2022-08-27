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
class Cuenta():
    def __init__ (self, titular, cantidad ):
        self.titular = titular
        self.__cantidad = cantidad or ""
       
    @property
    def getTitular(self):
        return self.titular
    @property
    def getCantidad(self):
        return self.__cantidad

    def setTitular(self,titular):
        self.titular = titular
    def setCantidad(self,cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print(f"Datos ingresados: \nNombre del titular: {self.getTitular} \nCantidad: {self.getCantidad} \n")
    def ingresar(self):
        while True:
            try:
                deposito=int(input("Ingrese la cantidad de dinero a depositar: "))     
            except ValueError:
                print("Dato erroneo, por favor escribe un número entero.")
                continue
            else:
                break
        print(f"Ud va a depositar en su cuenta la suma de $ {deposito}")
        self.__cantidad = self.__cantidad + deposito
        print (f"En su cuenta ahora tiene $ {self.__cantidad}")
    def retirar (self):
        while True:
            try:
                retiro=int(input("Ingrese la cantidad de dinero a retirar: "))     
            except ValueError:
                print("Dato erroneo, por favor escribe un número entero.")
                continue
            else:
                break
        print(f"Ud ha retirado de su cuenta la suma de $ {retiro}")
        self.__cantidad = self.__cantidad - retiro
        print (f"En su cuenta ahora tiene $ {self.__cantidad}")
finTit = False
while (finTit != True):
    titular = input("Ingrese nombre y apellido del titular de la cuenta: ")   
    list(titular)
    if (titular.isnumeric()):
        print("Dato erroneo, ingreso un numero")
        finTit = False
    elif(len(titular)<2):
        print("Ingrese una opcion valida")
        finTit = False
    else:
        finTit = True
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

persona = Cuenta(titular, cantidad)
persona.ingresar()
persona.retirar()


class CuentaJoven (Cuenta):
    def __init__ (self, titular, cantidad, edad ):
        Cuenta.__init__(titular, cantidad)
        self.edad = edad
        
    @property
    def getBonificacion(self):
        return self.bonificacion

    def setBonificacion(self,bonificacion):
        self.bonificacion = bonificacion

    def Bonificacion(self,porcentaje):
        self.bonificacion= self.cantidad * (porcentaje/100) 

    def esTitularValido():
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
        if (edad >=18 and edad <=25):
            return True
        else:
            return False
    def mostrar(self):
        super().mostrar()
        print(f"Los datos ingresados corresponden a Una Cuenta Joven y tiene una bonificacion de {self.getBonificacion()} en base a la cantidad {self.getCantidad}")
    
    def retirar (self,cantidad):
        if self.esTitularValido() == True:
            while retiro > self.cantidad or retiro < 0:
                print("La cantidad que desea retirar es excesiva o el numero ingresado es negativo.")
                retiro= int(input("Ingrese nuevamente el monto a retirar:"))
            else:
                print(f"Ud ha retirado de su cuenta la suma de $ {retiro}")
                self.__cantidad= self.__cantidad - retiro
                print (f"En su cuenta ahora tiene $ {self.__cantidad}")
        else:
            print("No esta habilitado para retirar dinero")       
        
joven = CuentaJoven()
joven.esTitularValido()
joven.bonificacion()
joven.mostrar()
joven.retirar()



        