# Escribir un programa que almacene el abecedario en una lista, elimine de 
# la lista las letras que ocupen posiciones múltiplos de 3, y muestre por 
# pantalla la lista resultante.
# abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
# for i in range(len(abecedario),1,-1):
#     if i%3==0: #multiplo de 3
#         abecedario.pop(i-1)
# print(abecedario)

#otra forma mia!
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
eliminar=[]
for i in range(0,len(abc)):
    if (i+1)%3==0:
        eliminar.append(abc[i])
for i in range(0, len(eliminar)):
    abc.remove(eliminar[i])
print(abc)
