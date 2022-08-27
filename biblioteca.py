# Crea una clase llamada Libro que guarde la información de cada uno de los libros de una biblioteca.
# La clase debe guardar el título del libro, autor, número de ejemplares del libro y número de
# ejemplares prestados. La clase contendrá los siguientes métodos:
# 1. Método préstamo que incremente el atributo correspondiente cada vez que se realice un
# préstamo del libro. No se podrán prestar libros de los que no queden ejemplares
# disponibles para prestar. Devuelve true si ha podido realizar la operación y false en caso
# contrario.
# 2. Método devolución que incremente el atributo correspondiente cuando se produzca la
# devolución de un libro. No se podrán devolver libros que no se hayan prestado.
# Cree un programa modular que permita probar el funcionamiento de la clase Libro:
# a) Cree un menú que permita:
# a. Cargar un libro
# I. Prestarlo
# II. Devolverlo
# b. Mostrar los libros
import os
os.system("cls")
libros=[]#creamos una lista vacia para guardar los libros que se crean
class Libro:
    def __init__(self) :#creamos la clase con sus atributos
        self.titulo= ""
        self.autor= ""
        self.cantidad= 0
        self.libroPrestado= 0

    def cargar(self): #creamos el metodo
        print("Ingresar un nuevo libro")
        libro=Libro()#se instancia (crea) un objeto de la clase Libro
        libro.titulo=input("Ingrese el titulo  del libro: ")
        libro.titulo=libro.titulo.lower()#lo pasamos a minusculas para no generar conflictos cuando lo buscamos, para que pueda comparar sin problemas
        libro.titulo=libro.titulo.strip() #quita los espacios en blanco donde esten    
        libro.autor=input("Ingrese el autor: ")
        libro.cantidad=int(input("Ingrese la cantidad de ejemplares que hay:"))
        libros.append(libro)#lo guardamos en la lista

    def mostrar(self):
        print("Listado de libros")
        for libro in libros:#se recorre la lista para mostrar uno a uno los libros
            print (f"Titulo: {libro.titulo} \n Autor: {libro.autor} \n Cantidad de ejemplares disponibles: {libro.cantidad} \n Cantidad de ejemplares prestados: {libro.libroPrestado} \n ...................")
    
    def prestar(self):
        libroBuscado=""
        print("Buscar un libro")
        nombreLibro= input("Ingrese el titulo del libro: ")
        nombreLibro= nombreLibro.lower()
        nombreLibro=nombreLibro.strip()
        for libro in self:
            if (libro.titulo == nombreLibro):
                libroEncontrado= libro
                print (f"Titulo: {libro.titulo} \nAutor: {libro.autor} \nCantidad de ejemplares disponibles: {libro.cantidad} \nCantidad de ejemplares prestados: {libro.libroPrestado}")   
                if(libroEncontrado.cantidad!=0):
                    libroEncontrado.libroPrestado+=1
                    libroEncontrado.cantidad -=  1
                    print(f"Se han prestado {libroEncontrado.libroPrestado} libro/s")
            else:
                print("No hay libros disponibles de ese titulo")

    def devolver(self):
        print("Buscar un libro")
        nombreLibro= input("Ingrese el titulo del libro: ")
        nombreLibro= nombreLibro.lower()
        nombreLibro = nombreLibro.strip() 
        for libro in self:
            if (libro.titulo == nombreLibro):
                libroEncontrado= libro
                if(libroEncontrado.libroPrestado !=0):
                    libroEncontrado.cantidad+=1
                    libroEncontrado.libroPrestado-=1
            print(f"Hay disponibles {libroEncontrado.cantidad} libro/s de ese titulo")
Opcion= ""
while(Opcion!="5"):  
    print("Elija la opcion deseada:")
    Opcion=input("Opcion 1: Cargar nuevo Libro \nOpcion 2: Prestar libro\nOpcion 3: Devolver libro \nOpcion 4: Mostrar Libros \nOpcion 5: Salir \n ")
    if(Opcion=="1"):
        os.system("cls") 
        Libro.cargar(libros)                        
    elif (Opcion == "2"):
        os.system("cls")
        Libro.prestar(libros)        
    elif (Opcion == "3"):
        os.system("cls")
        Libro.devolver(libros)
    elif (Opcion == "4"):
        os.system("cls")
        Libro.mostrar(libros)        
    elif (Opcion == "5"):
        print("Esta saliendo del sistema")            