import os
os.system("cls")
class Cuenta: #creo la clase llamada Cuenta
    #constructor
    def __init__ (self, titular, cantidad):  #titular es atributo obligatorio y cantidad es opcional, entonces lo inicializo con un valor por defecto
        self.__titular = titular or "" #El valor de los datos pueden estar vacios
        self.__cantidad = cantidad or ""
       
    #getters
    @property
    def getTitular(self):
        return self.__titular
    def getCantidad(self):
        return self.__cantidad

    #setters
    def titular(self,titular):
        self.__titular = titular
    
    def cantidad(self,cantidad):
        self.__cantidad = cantidad
    
    def __str__(self): # el metodo mostrar muestra los datos de la cuenta
        return f"Datos ingresados: \nNombre del titular: {self.__titular} \nCantidad: ${self.__cantidad} \n"
    
    def ingresar(self):
        while True:
            try:
                deposito=float(input("Ingrese la cantidad de dinero a depositar: "))     
            except ValueError:
                print("Dato erroneo, por favor escribe un número.")
                continue
            else:
                break
        print(f"Ud va a depositar en su cuenta la suma de $ {deposito}")
        self.__cantidad = self.__cantidad + deposito
        print (f"En su cuenta ahora tiene $ {self.__cantidad}")
    def retirar (self):
        while True:
            try:
                #permite el ingreso de un valor superior al que tenemos en la cuenta, y deja el saldo negativo (que seria mostrarlo en rojo)
                retiro=float(input("Ingrese la cantidad de dinero a retirar: "))     
            except ValueError:
                print("Dato erroneo, por favor escribe un numero.")
                continue
            else:
                break
        print(f"Ud ha retirado de su cuenta la suma de $ {retiro}")
        self.__cantidad = self.__cantidad - retiro
        print (f"En su cuenta ahora tiene $ {self.__cantidad}")
finTit = False
while (finTit != True):
    #permite ingresar "m3", "mm", caracteres sin limite
    titular = input("Ingrese nombre y apellido del titular de la cuenta: ")   
    list(titular)
    if (titular.isnumeric()):
        print("Dato erroneo, Ud ingreso un numero")
        finTit = False
    elif(len(titular)<2):
        print("Ingrese una opcion valida")
        finTit = False
    else:
        finTit = True
while True:
    try:
        cantidad = float(input("Ingrese fondos disponibles: "))
        #debería mostrar cartel de error por ingreso negativo para orientar al usuario porqué no continúa la ejecución
    except ValueError:
        print("Debe escribir un número")
        continue
    if cantidad < 0:
        pass
    else:    
        break

persona = Cuenta(titular, cantidad)
print(persona)
persona.ingresar()
persona.retirar()
