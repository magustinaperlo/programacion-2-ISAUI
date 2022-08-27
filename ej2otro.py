asignaturas = {
"Matematica": "5", 
"Fisica": "7", 
"Quimica": "9"
}
for i in asignaturas:
    nota=int(input("Ingrese nota de " + i + ":"))
    asignaturas[i]=nota
print(asignaturas)