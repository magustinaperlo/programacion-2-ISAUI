import os
class Lavado:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio
        self.contador=0

    def incrementarContador(self):
        self.contador+=1
    
    def total(self):
        return self.contador * self.precio

lavadoBasico = Lavado('basico',300)
lavadoFull = Lavado('full',500)

class Empleado:
    def __init__(self,id,nombre,apellido):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.ventas=0

    def venta(self,monto):
        self.ventas+=monto
    
    def total(self):
        return self.ventas

Em1=Empleado(1,'Juan','Romero') #colocamos primero el id porque en ese orden estan los parametros
Em2=Empleado(2,'Maria','Ortiz') #colocamos primero el id porque en ese orden estan los parametros
Em3=Empleado(3,'Ricardo','Escobar') #colocamos primero el id porque en ese orden estan los parametros
Em4=Empleado(4,'Matias','Cueto') #colocamos primero el id porque en ese orden estan los parametros

class Auto:
    def __init__(self,precio,tipo):
        self.precio=precio
        self.tipo=tipo
        self.contador=0
    
    def incrementarContador(self):
        self.contador+=1
    
    def total(self):
        return self.contador * self.precio

AutoChico=Auto(100,'chico') #colocamos al reves los parametros porque van en ese orden
AutoGrande=Auto(300,'grande') #colocamos al reves los parametros porque van en ese orden

Op=""
lavado=""
auto=""
contador=0

while (Op!="9"):
    
    lavadoPrecio=0
    print("-----------------------Menú Principal----------------------------------")
    print("1.- Nuevo Servicio")
    print("9.- Salir y ver Estadisticas finales")
    Op=input() #eliminamos el formato "int" porque si se ingresa una letra salta error de programa
    os.system("cls") #agregamos limpiar la pantalla luego de elegir nuevo servicio o salir.
    if (Op=="1" or Op == "9"): #Como ahora los numeros son strings, los colocamos entre ""
        if (Op=="1"):
            finempleado=False
            while(finempleado!=True):
                print('Ingresar Id de empleado')
                print('1 -->', Em1.nombre, Em1.apellido,'\n2 -->', Em2.nombre, Em2.apellido,'\n3 -->', Em3.nombre, Em3.apellido,'\n4 -->', Em4.nombre, Em4.apellido)
                Op=input() #eliminamos el formato "int" porque si se ingresa una letra salta error de programa
                if (Op== "1" or Op== "2" or Op == "3" or Op == "4"): #incluimos esta condicion porque si se ingresa otro valor, el programa corre igual y es erroneo que lo haga
                    finempleado=True
                    finlavado = False
                    finauto = False
                    while (finlavado!= True): #creamos un ciclo while para cuando se ingresa una palabra distinta de basico o full que el programa no ingrese de nuevo a pedir servicio o estadistica, sino que pida solo la instruccion de lo que se ingreso erroneamente. 
                        print('Ingrese tipo de lavado (basico / full)') 
                        lavado=input()
                        lavado = lavado.lower()
                        if (lavado == "basico" or lavado == "full"):#si se escribe la opcion de manera correcta, el programa continua
                            finlavado = True
                            if (lavado==lavadoBasico.tipo):
                                lavadoBasico.incrementarContador()
                                lavadoPrecio+=lavadoBasico.precio
                            elif (lavado==lavadoFull.tipo):
                                lavadoFull.incrementarContador()
                                lavadoPrecio+=lavadoFull.precio
                        else:
                            print('¡Ingresó un tipo de lavado incorrecto!')
                        
                    while (finauto!= True):#creamos un ciclo while para cuando se ingresa una palabra distinta de chico o grande que el programa no ingrese de nuevo a pedir servicio o estadistica, sino que pida solo la instruccion de lo que se ingreso erroneamente. 
                        print('Ingrese tipo de auto(chico / grande)')
                        auto=input()
                        auto = auto.lower()                        
                        if (auto == "chico" or auto == "grande"):
                            finauto = True
                            if (auto==AutoChico.tipo):
                                AutoChico.incrementarContador()
                                lavadoPrecio+=AutoChico.precio
                            elif (auto==AutoGrande.tipo):
                                AutoGrande.incrementarContador()
                                lavadoPrecio+=AutoGrande.precio
                        else:    
                            print('¡Ingresó un tipo de auto incorrecto!')                          
                else:
                    print ("Id del empleado equivocado")
            contador+=1
            if (Op=="1"):
                Em1.venta(lavadoPrecio)
            elif (Op=="2"):
                Em2.venta(lavadoPrecio)
            elif (Op=="3"):
                Em3.venta(lavadoPrecio)
            elif (Op=="4"):
                Em4.venta(lavadoPrecio)
        os.system("cls") #colocamos aca para limpiar lap antalla luegode elegir la opcion 9 de estadisticas  
        if (Op=="9"):            
            print('Total por empleado:')
            print('Empleado 1: $', Em1.total())
            print('Empleado 2: $', Em2.total())
            print('Empleado 3: $', Em3.total())
            print('Empleado 4: $', Em4.total())
            print("...........................")
            print('Total por tipo de lavado:')
            print('Básico: $', lavadoBasico.total())
            print('Full: $', lavadoFull.total())
            print("...........................")
            print('Total por tipo de auto:')    #agregamos total de lavados por tipo de auto
            print('Chico: $', AutoChico.total())
            print('Grande: $', AutoGrande.total())
            print("...........................")
            print('Total general: $', (Em1.total() + Em2.total() + Em3.total() + Em4.total()))
            print("...........................")
            print('Porcentaje por tipo de lavado:')
            if (contador!=0):#agregamos esta condicion porque si se ingresa a las estadisticas sin que haya habido lavados, el contador es 0 y se rompre el programa porque para calcular el porcentaje, no puede dividir por 0.
                print('Básico: ', round(lavadoBasico.contador/contador*100,2), " % ")
                print('Full: ', round(lavadoFull.contador/contador*100,2), " % ")
            else:
                print("No se han realizado lavados de este tipo")
            print("...........................")
            print('Porcentaje por tipo de auto:')
            if (contador!=0):#agregamos esta condicion porque si se ingresa a las estadisticas sin que haya habido lavados, el contador es 0 y se rompre el programa porque para calcular el porcentaje, no puede dividir por 0.
                print('Chico: ', round(AutoChico.contador/contador*100,2), " % ")
                print('Grande: ', round(AutoGrande.contador/contador*100,2), " % ")
            else:
                print("No se han realizado lavados de este tipo de auto")
    else:
        print("Codigo incorrecto")