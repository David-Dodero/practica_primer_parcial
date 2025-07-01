temperaturas = [18, 22, 20, 25, 21] #parametro actuale
umbral = 20   #parametro actual

def temperatura_media_alta(lista, umbral):#parametros formales 
    """
    calcula el promedio de las temperaturas y devuelve true si el promedio es mayor a el umbral

    parametros: 
        lista(list): lista de numeros a promediar 
        umbral(int): numero con el que se compara el promedio

    retorna:
        bool: true si el promedio es mayor al umbral o false si es menor al umbral 

    """
    suma = 0 
    for i in range(len(lista)):
        suma += lista[i]        
    promedio = suma / len(lista) 

    if promedio > umbral:
        resultado = True
    else:
        resultado = False
    
    return resultado 
#Invocacion a la funcion 
print(temperatura_media_alta(temperaturas, umbral))#parametros actuales 