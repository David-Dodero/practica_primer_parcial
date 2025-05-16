def sumar (num1: int, num2: int):
    """
    funcion que recibe dos enteros 
    parametro 1 = recibe un numero entero
    parametro 2 = recibe un numero entero
    retorna el resultado de la suma 
    """
    resultado = num1 + num2
    return resultado

numero1 = 10
numero2 = 20 

##print(sumar (numero1, numero2))

#si yo no quiero que lo muestre a sumar (numero1, numero2) lo hago variable respuesta = sumar (numero1, numero2)
#si quiero mostrarlo printeo respuesta: print(respuesta)

#hardcoriar agregar lo numeros en los parametros 

respuesta = sumar (200, 300)
#print(respuesta)

#buscar mayor o menor 

# min = 0 
# for i in range(5):
#     numero = int(input("ingresar un numero:" ))
#     if i == 0: 
#         min = numero 
#     elif numero < min:
#         min = numero 
    #print("minor por ahora", min)
#print("el menor numero es:", min)

#Buscar mayor o menor con Flag
min = 0 
bandera_min = True

for i in range(5):
    numero = int(input("ingresar un numero:" ))
    
    if numero % 2 == 0: 
        if bandera_min == True:  #sube la bandera en la primera vuelta 
            min = numero
            bandera_min = False # baja la bandera, por aca no pasa mas, sirve para pasar por un lugar una sola ves
        elif numero < min:
            min = numero 
        print("minor por ahora", min)
print("el menor numero es:", min)