# 11. crear una funcion llamada calcular_promedio(lista,valor) que reciba una lista de numero
# y un numero valor
#la funcion debe calcular el promedio de la lista y decir si el promedio es mayor que valor.
#debe retornar true si es mayor y false si no lo es.
#datos a usar de ejemplo:

# entrada = [10,20,30,40] #parametros actuales
# valor = 24              #parametros actuales 
# #salida esperada true
# #nota: indicar como comentario en el programa los parametros formales,
# # los parametros actuales y la invocacion  

# def calcular_promedio(lista,valor): #parametros formales
#     suma = 0 
#     for i in range(len(lista)):
#         suma += lista[i]        #suma los volores de la lista entrada
#     promedio = suma / len(lista) # saca el promedio 

#     if promedio > valor:
#         resultado = True
#     else:
#         resultado = False
    
#     return resultado
# #invocacion de la funcion 
# print(calcular_promedio(entrada, valor)) #parametros actuales


entrada = [10,20,30,40]
valor = 24
#salida esperada true

def calcular_promedio(lista,valor):
    suma = 0 
    for i in range(len(lista)):
        suma += lista[i] 
    promedio =suma / len(lista)

    if promedio > valor:
        resultado = True
    else:
        resultado = False
    
    return resultado


print(calcular_promedio(entrada, valor))

