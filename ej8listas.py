# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es
# un palíndromo.
# palabra= (input("Ingrese una palabra: "))
# palabrainvertida=palabra
# palabra=list(palabra)
# print(palabra)
# palabrainvertida = list(palabrainvertida)
# palabrainvertida.reverse()
# if palabra == palabrainvertida:
#     print("La palabra ingresada es un palindromo")
# else:
#     print("La palabra ingresada no es un palindromo")

#otra forma mia 
palabra=input("Ingrese una palabra ")
invertida = palabra
letras=list(palabra) #crea una lista con las letras de la palabra
print(letras)
invertida=list(palabra)
invertida.reverse()
print(invertida)
if letras == invertida:
    print("La palabra es un palindromo")
else:
    print("La palabra no es un palindromo")

# otra:
# palabra=[]
# palabra= input(" Ingrese una palabra ")
# invertida = palabra
# palabra=list(palabra)
# invertida = list(invertida)
# invertida.reverse()
# if palabra==invertida:
#     print(" La palabrea es un palindromo ")
# else:
#     print(" La palabrea no es un palindromo ")
