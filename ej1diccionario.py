# Escribir un programa que almacene las asignaturas de un curso y sus notas
from msilib.schema import ODBCTranslator


notas = {
"Matematica": "5",
"Fisica": "7", 
"Quimica": "9"
}   
# for clave,valor in notas.items():  #asi lo imprime en lista, cada clave con su valor  
#    print(f" {clave} : {valor}") #la f hace que se impriman los valores de cada clave y valor, si no esta imprime "clave""valor"

#otra forma
#print(notas) asi lo imprime en formato diccionario {"clave}:{valor}
# #funciona!!!

# otra 
#
for i in notas:
   print("En " + str(i) + " te sacaste: " + str(notas.get(i)))