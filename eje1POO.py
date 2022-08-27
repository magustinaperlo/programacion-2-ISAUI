class Perros():
    def __init__(self,nombre,edad,raza,vacunas,collar): #def(sigue con un espacio y dos guiones altos)init es el iniciador
        self.nombre=nombre
        self.edad=edad
        self.raza=raza
        self.vacunas=True
        self.collar=True

#a)crear el metodo imprimir
    def imprimir(self): #para crear  el metodo imprimir no lleva los dos guiones// para que funcione tiene que ir identado dentro de la clase
       print("El perro se llama", self.nombre, " tiene ",self.edad, " es de la raza ",self.raza, " vacunas: ", self.vacunas, "collar: ", self.collar)

perro1= Perros("Carola","15","Ovejero",True,True) #va entre comillas porque es string
perro1.imprimir() 


#b)Crear 4 instancias (objetos) de la clase Perros e imprimir sus
#características.
perro1= Perros("Carola","15","Ovejero",True,True)
perro2=Perros("Candy","12","Ovejero",True,True)
perro3=Perros("Pupa","10","Labrador",True,True)
perro4=Perros("Bugs","17","Ovejero",True,True)
perro1.imprimir() 
perro2.imprimir() 
perro3.imprimir() 
perro4.imprimir()


#c)cambiar el ejercicio de la siguiente manera, que se ingrese por teclado
#los atributos.
class Perros():
    def __init__(self):#si los ingresas por teclado, no se llaman arriba, va solo el self
        self.nombre=input("Ingrese el nombre del perro: ")
        self.edad=input(" Ingrese su edad: ")
        self.raza=input("De que raza es?: ")
        self.vacunas=input("Tiene vacunas? Si/No ")
        self.collar=input("Tiene collar? Si/No ")
    def imprimir (self):
        print("El perro se llama", self.nombre, " tiene ",self.edad, " es de la raza ",self.raza, " vacunas: ", self.vacunas, "collar: ", self.collar)
perro1=Perros()
perro1.imprimir()

