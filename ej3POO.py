# Confeccionar una clase que represente a un empleado.
# Definir como atributos su nombre y su sueldo.
# En el método __init__  cargar los atributos por teclado Y
# luego en otro método imprimir sus datos
# y por último uno que imprima un mensaje si debe pagar impuestos
# (si el sueldo supera 100000, debe pagar sino no)
# VARIANTE:
# Imprimir el sueldo bruto, el impuesto (15% sobre el sueldo bruto) y el
# sueldo a cobrar (sueldo menos el impuesto).

class Empleados():
    def __init__(self):
        self.nombre=input("Ingrese el nombre y apellido del empleado: ")
        self.sueldo=float(input("Ingrese su sueldo: "))
    def imprimir (self):
        print("El empleado ", self.nombre, " tiene un sueldo de $ ",self.sueldo)
    def impuesto (self):
        if self.sueldo < 100000:
            print("Excento de impuestos")
        else:
            self.impuesto =self.sueldo*0.15
            self.sueldobolsillo=self.sueldo-self.impuesto
            print(" Debe pagar impuestos por $", self.impuesto)
            print("El sueldo neto a cobrar es de $ ", self.sueldobolsillo)
empleado1=Empleados()
empleado1.imprimir()
empleado1.impuesto()

        
    