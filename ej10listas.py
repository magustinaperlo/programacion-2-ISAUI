# Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y
# muestre por pantalla su producto escalar.
vec1=[1,2,3]
vec2=[-1,0,2]
producto=[]
for i in range (0,len(vec1)):
    prod = vec1[i]*vec2[i]
    producto.append(prod)
print(producto)


