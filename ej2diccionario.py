# Sobre el ejercicio 1, consultar al usuario las notas y cambiarlas en el
# diccionario.
continuar = True
asignaturas = {
"Matematica": 5, 
"Fisica": 7, 
"Quimica": 9
}
while continuar: 
    materia = input(" Ingrese el nombre de la materia :")
    
    if materia in asignaturas:
        notas = input("Ingrese la nueva nota de " + materia + ":" ) 
        asignaturas [materia]=notas
        respuesta = input("Desea continuar cambiando notas? N/S ")
        if respuesta == "N" or respuesta =="n":
            continuar = False
    else:
        print("La materia no existe")
print (asignaturas)