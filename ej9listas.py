# Escribir un programa que almacene en una lista los siguientes precios, 50,
# 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los 
# precios.
precios=[50,75,46,22,80,65,8]
print(precios)
ordenados=sorted(precios)#escribe la lista ordenada de menor a mayor
print(ordenados)
print ("El menor precio es " + str(ordenados[0])+ " y el mayor " + str(ordenados[6]))

#FUNCIONA!!!

# otra forma 
# precios=[50,75,46,22,80,65,8]
# precios.sort()  los ordena de menor a mayor pero no los imprime
# print(precios)
#print("El menor precio es :",precios[0], "y el mayor es :", precios[-1])