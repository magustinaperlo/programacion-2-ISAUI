# Escribir un programa que guarde en un diccionario los precios de las frutas de
# la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por
# pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el
# diccionario debe mostrar un mensaje informando de ello.
# Fruta      Precio
# Plátano     1.35
# Manzana     0.80
# Pera        0.85
# Naranja     0.70

continuar = True
precio = 0
frutas = {
"Platano": 1.35, 
"Manzana": 0.80, 
"Pera": 0.85,
"Naranja":0.70
}
for clave,valor in frutas.items():    
   print(f" {clave} : {valor}")
while continuar: 
    fruta = input(" Ingrese la fruta elegida :")
    if fruta in frutas:
        cantidad = float(input("Ingrese la cantidad en kg de la  fruta elegida: " )) 
        precio = cantidad * frutas[fruta]
        print(cantidad , " kg de " , fruta , " cuestan $", precio )
        respuesta = input("Desea continuar comprando? N/S ")
        if respuesta == "N" or respuesta =="n":
            continuar = False
    else:
        print("La fruta no existe")


# otra
# frutas={"Platano":1.35,
# "Manzana":0.80,
# "Pera":0.85,
# "Naranja":0.70}
# for clave,valor in frutas.items():  #asi lo imprime en lista, cada clave con su valor  
#     print(f" {clave} : {valor}") 

# fruta=input("Ingrese nombre fruta elegida: ")
# cantidad=float(input("Cuantos kg de esa fruta? :"))
# if fruta in frutas:    
#     precio=frutas[fruta] * cantidad       
#     print(cantidad , " kg de ", fruta , " cuesta ", precio, "$")
# else:
#     print("Esa fruta no existe ")



