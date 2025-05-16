#recorido
calificacion = [85, 90, 78, 92, 86]  

suma = 0

for i in range(len(calificacion)):
    suma += calificacion[i]

promedio = suma / len(calificacion)

#print(promedio)

#lista_vacia = []
nombres = ["david , veritas, aprax"]
num = []
mi_lista = [0] * 5
#print(mi_lista)
#print(len(mi_lista))

for i in range(len(mi_lista)):
    mi_lista[i] = i

for i in range(len(mi_lista)):
    mi_lista[3] = 5


calificacion = [85, 90, 78, 92, 86]
#print(len(calificacion)) #len = 5 es la cantidad de elementos en la lista 

#Recorer por indice (esta es la que va)
for i in range(len(calificacion)):
    calificacion [3] = 29 
    #print(calificacion[i])
    

#recorer por lista
#for nota in calificacion:
 #   print(nota)

#mostrar la lista 
#print (calificacion)

mi_lista2 = [0] * 3

for i in range(len(mi_lista2)):
    print(mi_lista2[i])

for i in range(len(mi_lista2)):
    print("en la posicion", i )
    num = int(input("ingrese un numero: "))
    
for i in range(len(mi_lista2)):
    print(len(mi_lista2))