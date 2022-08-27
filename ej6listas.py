# Escribir un programa que almacene las asignaturas de un curso (por
# ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte
# al usuario la nota que ha sacado en cada asignatura y elimine de la lista
# las asignaturas aprobadas. Al final el programa debe mostrar por pantalla
# las asignaturas que el usuario tiene que repetir.
import os
os.system("cls")
from os import remove
asignaturas=["Matematicas","Fisica","Quimica","Historia", "Lengua" ]
nota=0
aprobados=[]
for i in range (0,len (asignaturas)):
    nota = int(input(" Ingrese su nota de " + asignaturas[i]+ " : "))
    if nota >= 6:
        aprobados.append(asignaturas[i])
for i in range (0,len(aprobados)):    
    asignaturas.remove(aprobados[i])
print (asignaturas)


# otra forma:

# materias=["Matematica","Fisica","Quimica","Historia","Lengua"]
# aprobadas=[]
# nota = 0
# for materia in materias:
#     nota=float(input("Ingrese su nota en "+ materia+ " : "))
#     if nota>=6:
#         aprobadas.append(materia)
# for materia in aprobadas:
#     materias.remove(materia) 
# print(materias)

