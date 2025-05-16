lista = [6, 3, 8, 5]

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if(lista[i] > lista[j]):
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
print(lista) #3,5,6,8

for i in range(len(lista)):
    print(lista[i]) #3,5,6,8 lo mismo pero uno arriba del orto  