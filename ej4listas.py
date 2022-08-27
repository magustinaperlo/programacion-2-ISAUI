# Escribir un programa que pregunte al usuario los números ganadores de la lotería
# primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
# a mayor.

loteria=[]
con = 0
num = 0
while con <6:
    num =int(input("Ingrese el "+ str(con +1 )+ " numero ganador  "))
    loteria.append(num) 
    con = con + 1
print (sorted (loteria))