# Escribir un programa que cree un diccionario simulando una cesta de la
# compra. El programa debe preguntar el artículo y su precio y añadir el par al
# diccionario, hasta que el usuario decida terminar. Después se debe mostrar por
# pantalla la lista de la compra y el coste total, con el siguiente formato
# Lista de la compra
# Artículo 1    Precio
# Artículo 2    Precio
# Artículo 3    Precio
# ... ...
# Total         Costo
continuar = True
total = 0
compra={}
while continuar==True:
    articulo=str(input(" Ingrese nombre del articulo :"))
    precio = float(input(" Ingrese el precio de dicho articulo :"))
    compra[articulo]=precio
    total = total + precio #compra[articulo]
    respuesta=input("Desea continuar comprando? S/N ")
    if respuesta=="N" or respuesta=="n":
       continuar=False       
       for clave,valor in compra.items():  
        print(f" {clave} : {valor}")
print("El total de su compra es de :",total)   
       