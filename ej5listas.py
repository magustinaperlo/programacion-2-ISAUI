# Escribir un programa que almacene en una lista los números del 1 al 10 y
# los muestre por pantalla en orden inverso separados por comas.
lista=[]
con = 0
num = 0
i = 0
for i in range (0,10):
    num=(i+1)
    lista.append(num)   
#for i in range(0,len(lista)):
    #print(lista[-1-i])
#no los muestra separados por comas

#lista.sort(reverse=True)
#print(lista)

lista.reverse() #ordena los valores del vector en orden inverso
print (lista)

# otra forma
# con = 1
# numeros=[]
# while con < 11:
#     numeros.append(con)
#     con = con + 1
# numeros.reverse()
# print(numeros)

