# Escribir un programa que pregunte al usuario su nombre, edad, dirección y
# teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el
# mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de
# teléfono es <teléfono>.

usuario = {
    "Nombre": "nombre",
    "Edad":"edad",
    "Direccion":"direccion",
    "Telefono":"telefono"}
nombre = str(input("Ingrese su Nombre y Apellido: "))
edad = str(input("Ingrese su edad: "))
direccion = str(input("Ingrese su direccion: "))
telefono = str(input("Ingrese su telefono: "))
usuario["Nombre"]= nombre
usuario["Edad"]= edad
usuario["Direccion"]= direccion
usuario["Telefono"]= telefono

print(nombre +" tiene "+ edad+" años, vive en "+ direccion+ " y su numero de telefono es "+ telefono)