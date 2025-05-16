#carga aleatoria con listas
mi_lista2 = [0] * 5
respuesta = "s"

#muestra mi lista inisial en 0 
for i in range(len(mi_lista2)):
    print(mi_lista2[i])

while respuesta == "s":
    posicion = int(input("ingrese una posicion de la lista: "))
    numero = int(input("ingrese una numero: "))
    mi_lista2[posicion] = numero
    respuesta = input("ingrese otro numero s/n? ")

for i in range(len(mi_lista2)):
    print(mi_lista2[i])


#siempre que estoy hablando del elemento dentro de la posicion van corchetes [i] y si solo hablo del indice hablo de i 
# osea Estás accediendo al valor que está dentro de la lista en la posición i 
#ejemplo:
# mi_lista2 = [5, 7, 3]
# print(mi_lista2[1])  # Imprime 7 (porque es el valor en la posición 1)

# Cuando usás solo i (sin corchetes):
#Estás hablando del índice o posición, no del contenido.
#ejemplo
# for i in range(len(mi_lista2)):
#     print(f"Posición: {i}")           # Solo muestra el índice
#     print(f"Valor: {mi_lista2[i]}")   # Muestra el valor en esa posición


lista = []
lista.append (40)
lista.append("David") # siempre lo agrega al final de la lista
print(lista)