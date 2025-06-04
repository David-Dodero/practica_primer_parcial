# # Crear una función llamada "es_promedio_par_mayor" que reciba una lista de números
# # La función debe calcular el promedio de la lista y:
# # → Retornar True si el promedio es un número **par** y es **mayor a 50**
# # → Si no se cumple alguna de esas condiciones, debe retornar False

# # Datos de ejemplo para probar:
# datos = [60, 70, 50, 40]   # promedio = 55 → es mayor a 50 y es impar → False
# #datos = [60, 70, 50, 40] parametros actuales 
# def es_promedio_par_mayor(lista): #parametros formales 

#     suma = 0 
#     for i in range(len(lista)):
#         suma += lista[i]   #suma los valores de la lista 
    
#     promedio = suma / len(lista) #saca el promedio de la suma de los valores de la lista con la cantidad de valores de la lista 
    
#     if promedio % 2 == 0 and promedio > 50: # si es par y mayor a 50 retorna true 
#         resultado = True
#     else:
#         resultado = False # sino retorna false 
    
#     return resultado # el retorno 

# print(es_promedio_par_mayor(datos)) # invocacion de la funcion con parametros actuales 

# Crear una función llamada "promedio_supera_mitad" que reciba una lista de números
# La función debe calcular el promedio y verificar si es mayor que la mitad del valor más alto de la lista.
# Si el promedio es mayor que la mitad del número más grande, retornar True, sino False.

# Ejemplo de datos:
# numeros = [10, 20, 30, 40, 50] #parametros actuales
# # el mayor es 50 → su mitad es 25
# # el promedio es (10+20+30+40+50)/5 = 30
# # → como 30 > 25 → devuelve True

# def promedio_supera_mitad(lista): #parametros formales 
#     mayor_numero = lista[0]             # mayor numero inicia con el primer valor de la lista 
#     suma = 0                            # suma inicia en 0     
#     for i in range(len(lista)):         # recore la lista 
#         if mayor_numero < lista[i]:     # si el numero mayor es mas chico que el valor de lalista toma ese valor 
#             mayor_numero = lista[i]
        
#         suma += lista[i]                #suma los valores de la lista 
#     promedio = suma / len(lista)        #saca el promedio de la lista con la cantidad de valores de la lista 

#     la_mitad_del_mayor = mayor_numero / 2 #divide el numero mas grande 

#     if promedio > la_mitad_del_mayor:   #pregunta si el promedio es mas grande que la mitad del numero mas grande, si es asi retorna true, sino false 
#         resultado = True                
#     else:
#         resultado = False

#     return resultado

# print(promedio_supera_mitad(numeros)) #invocacion a la funcion con parametros actuales 

# Crear una función llamada "promedio_pares_es_mayor" que reciba una lista de números.
# La función debe calcular el promedio de **solo los números pares**.
# Si ese promedio es mayor a 25, retornar True. Si no lo es, retornar False.

# Ejemplo de datos:
valores = [10, 15, 20, 30, 35] #parametros actuales
# Pares: 10, 20, 30 → promedio = (10+20+30)/3 = 20 → retorna False
numero_mayor = 25 # parametros actuales que agrege yo 

def promedio_pares_es_mayor(lista, numero)-> bool: #parametros formales 
    """la funcion resive una lista de numeros por parametro formal.
    la funcion calcula el promedio solo de los numeros pares y si 
    el promedio es mayor a 25 retorna true, sino retorna false"""
    
    suma = 0  
    contador_numeros_pares = 0
    for i in range(len(valores)):
        if valores[i] % 2 == 0 :
            suma += valores[i]
            contador_numeros_pares += 1 
    promedio = suma / contador_numeros_pares

    if promedio > numero_mayor:
        respuesta = True
    else:
        respuesta = False
    
    return respuesta

print(promedio_pares_es_mayor(valores, numero_mayor)) #invocacion a la funcion con un print y parametros actuales 

    
