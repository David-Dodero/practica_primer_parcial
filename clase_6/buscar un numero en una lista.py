#buscar un numero en una posicion de la lista 
lista = [10,20,30,40,50,60,70,80,90]
posicion = 0 

numero_a_buscar= int(input("ingresar un numero: "))

for i in range(len(lista)):
    if lista[i] == numero_a_buscar:
        posicion = i 
        break
    
if posicion > -1 :
    print("se encontro el elemento", posicion)
else :
    print("no se encontro elemento")