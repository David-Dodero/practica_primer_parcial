frutas = ["manzana", "banana"]
#El método APPEND agrega un elemento al final de la lista
frutas.append("naranja")
print(frutas) #['manzanada', 'banana', 'naranja']

#El método INSERT inserta un elemento en la posición especificada
frutas.insert(1, "kiwi")
print(frutas) #['manzanada', 'kiwi', 'banana', 'naranja']

#El método EXTEND permite añadir una lista a la lista inicial

otras_frutas = ["pomelo","uva"]
frutas.extend(otras_frutas)
print(frutas) #['manzana', 'kiwi', 'banana', 'naranja', 'pomelo', 'uva']

#El método SORT ordena la lista en orden ascendente
frutas.sort()
print(frutas) #['banana', 'kiwi', 'manzana', 'naranja', 'pomelo', 'uva']

#El método REMOVE elimina la primer ocurrencia del elemento especificado
frutas.remove("manzana")
print(frutas) #['kiwi', 'banana', 'naranja', 'pomelo', 'uva']

#El método POP elimina y devuelve el elemento en la posición dada. Si no se especifica un índice, se elimina y devuelve el último elemento
fruta = frutas.pop(1)
print(fruta) # se elimino banana
print(frutas) #['kiwi', 'naranja', 'pomelo', 'uva']

#El método INDEX devuelve el índice de la primera ocurrencia del elemento especificado
posicion = frutas.index("naranja")
print(f"la naranja esta en la posicion: {posicion}") #la naranja esta en la posicion: 1

#El método CLEAR elimina todos los elementos de la lista, dejándola vacía
frutas.clear()
print(frutas) #[]

#El método SORT ordena la lista en orden ascendente
numeros = [616,42,23,54]
numeros.sort()
print(numeros) #[23, 42, 54, 616]

#El método REVERSE invierte el orden de los elementos de la lista
numeros.reverse()
print(numeros) #[616, 54, 42, 23] 

#para ordenar una lista de forma descendente uso primero el SORT y despues el REVERSE
numeros = [616,42,23,54]
numeros.sort()
print(numeros) #[23, 42, 54, 616]
numeros.reverse()
print(numeros) #[616, 54, 42, 23] 

# Otra forma de Eliminación
# del lista[índice] (no es un metodo)
lista2 = [10,20,30,40]
del lista2[1]
print(lista2) #[10, 30, 40]

#SHALLOW COPY (Copia superficial)
#Shallow copy copia la lista en otra variables para poder usarla sin modificar a la original

# Lista original con una lista interna
original = [[1, 2], [3, 4]]

# Hacemos una copia superficial
copia_original = original.copy()

# Modificamos un valor dentro de una sublista
copia_original[0][0] = 99

print("Original:", original) #Original: [[99, 2], [3, 4]]
print("copia original:", copia_original) #copia original: [[99, 2], [3, 4]]

#DEEP COPY (Copia profunda)
import copy

# Lista original con una lista interna
original = [[1, 2], [3, 4]]

# Hacemos una copia profunda usando deepcopy
copia_original = copy.deepcopy(original)

# Modificamos un valor dentro de una sublista
copia_original[0][0] = 99

print("Original:", original)          # Original: [[1, 2], [3, 4]]
print("copia original:", copia_original)  # copia original: [[99, 2], [3, 4]]

lista = [10,20,30,40]
copia_lista = lista.copy() #este es el mejor

# La función enumerate() agrega un contador (índice) a un iterable, como una lista,
# devolviendo un objeto enumerado. Esto es especialmente útil cuando necesitas
# acceder a los índices de los elementos mientras iteras sobre ellos

frutas2 =['banana', 'kiwi', 'manzana', 'naranja', 'pomelo', 'uva']

for indice, fruta in enumerate(frutas2):
    print(f"indice: {indice}, frruta: {fruta}") 
#indice: 0, frruta: banana
# indice: 1, frruta: kiwi
# indice: 2, frruta: manzana
# indice: 3, frruta: naranja
# indice: 4, frruta: pomelo
# indice: 5, frruta: uva

# Función zip
# Permite iterar múltiples listas a la vez
nombres= ["ana", "luis", "jusn"]
edades = [25, 30, 35]

for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tine {edad} anos")
# ana tine 25 anos
# luis tine 30 anos
# jusn tine 35 anos 


#  ¿Para qué sirve un set?
# Para eliminar duplicados de una lista:

lista = [1, 2, 2, 3]
sin_repetidos = set(lista)
print(sin_repetidos)  # {1, 2, 3}