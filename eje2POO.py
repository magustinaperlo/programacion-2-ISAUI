# Implementar la clase Operaciones. Se deben cargar dos valores enteros
# por teclado en el método __init__, calcular su suma, resta,
#multiplicación y división
# cada una en un método, imprimir dichos resultados.
class Operaciones():
    def __init__(self):
        self.num1=float(input("Ingrese el primer numero: "))
        self.num2=float(input("Ingrese el segundo numero: "))
    def sumar(self):
        suma=self.num1 + self.num2
        print(" El resultado de la suma es: ", suma)
    def restar(self):
        resta=self.num1 - self.num2
        print(" El resultado de la resta es: ", resta)
    def multiplicar(self):
        producto=self.num1 * self.num2
        print(" El resultado del producto es: ", producto)
    def dividir(self):
        if self.num2 == 0:#siempre se pone le self adelante para llmar la variable
            print("No se puede dividir por 0")
        else:
            division=self.num1/self.num2
            division=round(division,2) #El round es para que el resultado se redondee a 2 decimales
            print(" El resultado del cociente es: ", division)

operacion1=Operaciones()#llama un objeto de la clase operaciones
operacion1.sumar() #llamo la instancia (suma)para que haga el metodo suma dentro de la clase operaciones
operacion1.restar()
operacion1.multiplicar()    
operacion1.dividir()