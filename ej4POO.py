#Herencia: a partir de la clase Vehículo, crear 2 subclases, 
#aparte de la clase moto.
import os
os.system("cls")
class Vehiculo():
    def __init__(self, marca, modelo, anio, color, cantidadDeRuedas):
        self.marca = marca
        self.modelo = modelo
        self.anio= anio
        self.color = color
        self.cantidadDeRuedas= cantidadDeRuedas 
        self.en_marcha = False
        self.acelerando=False
        self.frenando=False
    def arrancar(self):
        self.en_marcha = True
    def frenar(self):
        self.frenando = True
    def acelerar(self):
        self.acelerando = True    
    def estado (self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo,"\nAño: ", self.anio,"\nColor: ", self.color,"\nCantidad de ruedas: ", self.cantidadDeRuedas,"\nEncendido?: ", self.en_marcha,"\nAcelerando?: ", self.acelerando,"\nFrenando?: ", self.frenando)
        
print ("..........MOTOS............")
class Moto(Vehiculo):
    def __init__(self, tipo,cilindrada, marca_moto, modelo_moto, anio_moto, color_moto, cantidadDeRuedas_moto):
        super().__init__(marca_moto, modelo_moto, anio_moto, color_moto, cantidadDeRuedas_moto)      
        self.tipo = tipo
        self.cilindrada = cilindrada        
        
    def estado (self):
        super().estado()
        print("Tipo: ", self.tipo,"\nCilindrada del motor: ", self.cilindrada)

moto1 = Moto("Enduro","125cc","Honda","Biz","2020","Blanca",2 )
moto1.arrancar()
moto1.acelerar()

moto1.estado()

print("-----------------------")
moto2 = Moto("Motocross","250cc","Yamaha","CMX","2018","Negra",2 )
moto2.frenar()
moto2.estado()

print ("..........AUTOS............")
class Auto(Vehiculo):
    def __init__(self, tipoDeCaja,cantidadDePuertas, marca_auto, modelo_auto, anio_auto, color_auto, cantidadDeRuedas_auto):
        super().__init__ (marca_auto, modelo_auto, anio_auto, color_auto, cantidadDeRuedas_auto)  #asi se llama al constrtuctor de la clase padre
        self.tipoDeCaja= tipoDeCaja
        self.cantidadDePuertas= cantidadDePuertas       
    def estado (self):
        super().estado()
        print("Tipo de transmision de la caja: ", self.tipoDeCaja, "\nCantidad de puertas: ", self.cantidadDePuertas)
auto1 = Auto("Automatica", "5","Ford","Ecosport","2016","Blanco",4)
auto1.arrancar()
auto1.frenar()
auto1.estado()
print("-----------------------")
auto2 = Auto("Manual","5","Volkswagen","Gol Country","2005","Gris",4)
auto2.acelerar()
auto2.estado()

print ("..........LANCHAS............")
class Lancha(Vehiculo):
    def __init__(self, tipo,tipoMotor, potenciaMotor, marca_lancha, modelo_lancha, anio_lancha, color_lancha, cantidadDeRuedas_lancha):
        super().__init__ (marca_lancha, modelo_lancha, anio_lancha, color_lancha, cantidadDeRuedas_lancha)  #asi se llama al constrtuctor de la clase padre
        self.tipo = tipo
        self.tipoMotor = tipoMotor
        self.potenciaMotor= potenciaMotor       
    def estado (self):
        super().estado()
        print("Tipo de lancha: ", self.tipo, "\nTipo de motor:", self.tipoMotor,"\nPotencia del motor: ", self.potenciaMotor)
lancha1 = Lancha("Deportiva", "Turbo diesel","80 HP","Cuddy","Eclipse","2012","Blanco","-")
lancha1.acelerar()
lancha1.frenar()
lancha1.estado()
print("-----------------------")
lancha2 = Lancha("Competicion","4 tiempos","60 HP","Bakota","Canestrari","2018","Negra","-")
lancha2.arrancar()
lancha2.estado()
















