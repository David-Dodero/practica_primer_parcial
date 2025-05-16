#FUNCIONES y LISTAS
#David Dodero
# Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los
# guarde en una lista y la retorne. El programa principal debe invocar a la función y
# mostrar por pantalla el retorno.

def nombres ():
    lista_nombres = [""] * 10
    for i in range(10):
        nombre= input("ingrese un nombre: ")
        lista_nombres[i] = nombre
    return lista_nombres
#print(nombres())

# Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida
# posición y número a guardar al usuario, lo guarde en una lista en la posición
# solicitada aleatoriamente y la retorne. El programa principal debe invocar a la
# función y mostrar por pantalla el retorno.

def numeros():
    lista_numeros = [0] * 10
    respuesta = input("desea agregar numeros en la lista? s/n ")
    while respuesta == "s":
        posicion = int(input("ingrese la posicion: "))
        numero = int(input("ingrese numero: "))
        lista_numeros[posicion] = numero
        respuesta = input("desea agregar numeros en la lista? s/n ")
    return lista_numeros

#print(numeros())

# Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango
# especificado, validar los números solicitados dentro de ese rango, guardar en una
# lista y retornarla. El programa principal debe invocar a la función y mostrar por
# pantalla el retorno.

def pedir_numeros():
    lista_numeros = [0] * 10
    for i in range(10):
        numero = int(input("ingrese un numero del 0 al 100: "))
        while numero < 0 or numero > 100:
            numero = int(input("fuera del rango, ingrese un numero del 0 al 100: "))
        lista_numeros [i] = numero
    return lista_numeros
#print(pedir_numeros())

# Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números
# y un número especificado. La misma debe buscar el número especificado en la lista
# y retornar “True” si existe.

numeros_random = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

numero_buscar = int(input("ingrese el numero que desea buscar: "))
def recibe_numeros(lista:list, num:int):
    #numero_encontrado = -1 
    for i in range(len(lista)):
        if lista[i] == num:
            return True
    return False
            #numero_encontrado = i 
            #break
    # if numero_encontrado != -1:
    #     return True
    # else:
    #     return False 
#print(recibe_numeros(numeros_random,numero_buscar ))

# #Ejercicio 5: Dadas las siguientes listas:
# Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
# ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]
# Desarrollar una función que reciba por parámetro la lista de edades, busque a las
# personas de menor edad (puede ser más de una) y las retorne. El programa
# principal deberá mostrar nombre y edad de los menores.


Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


def persona_menor (lista_edades:list):
    menor_edad = lista_edades[0]
    
    for i in range(len(lista_edades)):
        if menor_edad > lista_edades[i]:
            menor_edad = lista_edades[i]
            
    return menor_edad

edad_minima = persona_menor(edades)

for i in range(len(edades)):
    if edad_minima == edades[i] :
        print(f"el nombre de la persona menor es {Nombres[i]} y la edad es {edades[i]}")
    

# Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
# listas_personas.py. Importar los nombres a una lista. Realizar una función que
# muestre los mismos

from listas_personas import nombres

def mostrar_nombres(nombres:list):
    for i in range(len(nombres)):
        print(nombres[i])

#mostrar_nombres(nombres)


# Ejercicio 7: Una startup desea analizar las estadísticas de los usuarios de su sitio de
# compras on-line recientemente lanzado al mercado para ello necesita un programa
# que le permita acceder a los datos relevados.
# Realizar una función con el siguiente Menú de Opciones:
# 1-Importar listas
# 2-Listar los datos de los usuarios de México
# 3-Listar los nombre, mail y teléfono de los usuarios de Brasil
# 4-Listar los datos del/los usuario/s más joven/es
# 5-Obtener un promedio de edad de los usuarios
# 6-De los usuarios de Brasil, listar los datos del usuario de mayor edad
# 7-Listar los datos de los usuarios de México y Brasil cuyo código postal
# sea mayor a 8000
#8-Listar nombre, mail y teléfono de los usuarios italianos mayores a 40
#años.


from listas_personas import *
def importar_listas():
    print("listas importadas ")
    return True
def usuarios_mexico():
    for i in range(len(country)):
        if country[i] == 'Mexico':
            print(f"nombre:{nombres[i]},telefono: {telefonos[i]}, mails: {mails[i]}, address: {address[i]}, postalzip: {postalZip[i]}, region: {region[i]}, country: {country[i]}, edades: {edades[i]}")


    
def datos_brasil(): 
     for i in range(len(country)):
        if country[i] == 'Brazil':
           print(f"nombre:{nombres[i]},telefono: {telefonos[i]}, mails: {mails[i]}")
    
def datos_jovenes():
    edad_min = edades[0]
    for i in range(1,len(edades)):
        if edades[i] < edad_min:
            edad_min = edades[i]

    for i in range(len(edades)):
        if edades[i] == edad_min: 
            print(f"Los datos del usuario más joven: nombre: {nombres[i]}, teléfono: {telefonos[i]}, mails: {mails[i]}, address: {address[i]}, postalZip: {postalZip[i]}, region: {region[i]}, country: {country[i]}, edad: {edades[i]}")
    
def promedio_edad():
    suma_edades = 0 
    for i in range(len(edades)):
        suma_edades += edades[i]
    promedio = suma_edades / len(edades) 
    print("el promedio de las edades es de", promedio)
    
def brasil_mayor():
    brasilero_mayor = -1
    for i in range(len(country)):
        if country[i] == 'Brazil':
            if edades[i] > brasilero_mayor:
                brasilero_mayor = edades[i]
    for i in range(len(edades)):
        if country[i] == 'Brazil' and edades[i] == brasilero_mayor:
            print(f"el usuario brasilero mayor es: nombre: {nombres[i]}, teléfono: {telefonos[i]}, mails: {mails[i]}, address: {address[i]}, postalZip: {postalZip[i]}, region: {region[i]}, country: {country[i]}, edad: {edades[i]}")
    
def mex_bra_pos_mayor():
    for i in range(len(country)):
        if (country[i] == 'Brazil' or country [i] == 'Mexico') and postalZip[i] > 8000 :
             print(f"los usuarios brasileros y mexicanos con codigo postal mayor a 8000: nombre: {nombres[i]}, teléfono: {telefonos[i]}, mails: {mails[i]}, address: {address[i]}, postalZip: {postalZip[i]}, region: {region[i]}, country: {country[i]}, edad: {edades[i]}")
    
def italianos_mayores_40():
    for i in range(len(country)):
        if country[i] == 'Italy' and edades[i] > 40 :
             print(f"los usuarios italianos mayores a 40: nombre: {nombres[i]}, teléfono: {telefonos[i]}, mails: {mails[i]}, country: {country[i]}, edad: {edades[i]}")
    


def menu_opciones():
    listas_importadas = False
    while listas_importadas == False:
        seleccion = int(input("ingrese el numero 1 para importar las listas: "))
        if seleccion == 1:
            listas_importadas = importar_listas()


    seleccion = int(input("seleccione una opcion del 2 al 8: "))
    while seleccion < 2 or seleccion > 8:
        seleccion = int(input("error, seleccione una opcion del 2 al 8: "))
        
    if seleccion == 2:
        usuarios_mexico()
            
    elif seleccion == 3:
        datos_brasil() 
            
    elif seleccion == 4:
        datos_jovenes()        
    elif seleccion == 5:
        promedio_edad()        
    elif seleccion == 6:
        brasil_mayor()            
    elif seleccion == 7:
        mex_bra_pos_mayor()            
    else:
        italianos_mayores_40()
            


menu_opciones()