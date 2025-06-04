# frutas = ["manzanada", "banana"]

lista = [10,20,30,40]

for elementos in lista:
    print(elementos)

for i in range(len(lista)):
    print(lista[i])

for puesto, elemento in enumerate(lista):
    print(puesto, elemento)




# otras_frutas = []
# frutas.extend()

#referencias es copia de memoria
#shallow copy 

lista = [10,20,30,40]

print("1-original",lista)

#copia_lista = lista 
#copia_lista[3] = "Roberto"
#esto no va, se usa shallow copy para una copia real 
#Shallow copy copia la lista en otra variables para poder usarla sin modificar a la original 
copia_lista = lista.copy() #este es el mejor

#otra forma de hacer shallow copy 
copia_lista = lista[:]

copia_lista = list(lista) #ojo con esta castea la lista 
copia_lista[3] = "Roberto" 

print("3-copia", copia_lista)
print("2- original", lista)
# cada vez que copio una lista copia la direccion de memoria 