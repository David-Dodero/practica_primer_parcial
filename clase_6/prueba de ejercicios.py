# Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]
# edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]


# def persona_menor (lista_edades:list):
#     menor_edad = lista_edades[0]
    
#     for i in range(len(lista_edades)):
#         if menor_edad > lista_edades[i]:
#             menor_edad = lista_edades[i]
            
#     return menor_edad

# edad_minima = persona_menor(edades)

# for i in range(len(edades)):
#     if edad_minima == edades[i] :
#         print(f"el nombre de la persona menor es {Nombres[i]} y la edad es {edades[i]}")



# Ejercicio 6: Analizar los datos del archivo listas_personas.py. Utilizando el archivo
# listas_personas.py. Importar los nombres a una lista. Realizar una función que
# muestre los mismos

# from listas_personas import nombres

# def mostrar_nombres(nombres:list):
#     for i in range(len(nombres)):
#         print(nombres[i])


# mostrar_nombres(nombres)

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
# #años.
# 9-Listar los datos de los usuarios de México ordenados por nombre
# 10-Listar los datos del/los usuario/s más joven/es ordenados por edad de
# manera ascendente (Si la edad se repite, ordenar por nombre de manera
# ascendente)
# 11-Listar los datos de los usuarios de México y Brasil cuyo código postal
# sea mayor a 8000 ordenado por nombre y edad de manera descendente


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

def datos_mexico():
    los_usuarios_mexico = [] 
    for i in range(len(country)):
        if country[i] ==  'Mexico':
            los_usuarios_mexico.append(i)
            
    for i in range(len(los_usuarios_mexico)-1):
        for j in range(i+1, len(los_usuarios_mexico)):
            if nombres [los_usuarios_mexico[i]] > nombres [los_usuarios_mexico[j]]:
                        aux = los_usuarios_mexico[i]
                        los_usuarios_mexico[i] = los_usuarios_mexico[j]
                        los_usuarios_mexico[j] = aux
                        
    for i in los_usuarios_mexico:
        print("nombre: ", nombres[i],"telefono:",telefonos[i],"mail:", mails[i],"pais:",country[i],"edad:",edades[i],"direccion:",address[i],"codigo postal:",postalZip[i],"region",region[i])

def mas_jovenes():
    edad_min = edades[0]
    for i in range(1, len(edades)):
        if edades[i] < edad_min:
            edad_min = edades[i]

    indice_jovenes = []
    for i in range(len(edades)):
        if edades[i] == edad_min:
            indice_jovenes.append(i)

    for i in range(len(indice_jovenes)-1):
        for j in range(i+1, len(indice_jovenes)):
            if nombres[indice_jovenes[i]] > nombres[indice_jovenes[j]]:
                aux_nom = indice_jovenes[i]
                indice_jovenes[i] = indice_jovenes[j]
                indice_jovenes[j] = aux_nom

    for i in indice_jovenes:
        print("nombre:",nombres[i],"edad:", edades[i])

def ordena_mex_bra():
    indice_mex_bra = []
    for i in range(len(country)):
        if (country[i] == 'Brazil' or country [i] == 'Mexico') and postalZip[i] > 8000 :
            indice_mex_bra.append(i)
    
    for i in range(len(indice_mex_bra)-1):
        for j in range(i+1, len(indice_mex_bra)):
            if nombres[indice_mex_bra[i]] < nombres[indice_mex_bra[j]]:
                aux_mex_bra = indice_mex_bra[i]
                indice_mex_bra[i] = indice_mex_bra[j]
                indice_mex_bra[j] = aux_mex_bra
            elif nombres[indice_mex_bra[i]] == nombres[indice_mex_bra[j]]:
                if edades[indice_mex_bra[i]] < edades[indice_mex_bra[j]]:
                    aux_mex_bra = indice_mex_bra[i]
                    indice_mex_bra[i] = indice_mex_bra[j]
                    indice_mex_bra[j] = aux_mex_bra





    for i in indice_mex_bra:
        #print("nombre: ", nombres[i],"telefono:",telefonos[i],"mail:", mails[i],"pais:",country[i],"edad:",edades[i],"direccion:",address[i],"codigo postal:",postalZip[i],"region",region[i])
        print("nombre:", nombres[i], "edad", edades[i])



def menu_opciones():
    listas_importadas = False
    while listas_importadas == False:
        seleccion = int(input("ingrese el numero 1 para importar las listas: "))
        if seleccion == 1:
            listas_importadas = importar_listas()


    seleccion = int(input("seleccione una opcion del 2 al 11: "))
    while seleccion < 2 or seleccion > 11:
        seleccion = int(input("error, seleccione una opcion del 2 al 11: "))
        
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
    elif seleccion == 8:
        italianos_mayores_40()
    elif seleccion == 9:
        datos_mexico()
    elif seleccion == 10:
        mas_jovenes()
    elif seleccion == 11:
        ordena_mex_bra()

menu_opciones()




# def mas_jovenes():
#     for i in range(len(edades)-1):
#         for j in range(i+1, len(edades)):
#             if edades[i] > edades[j]:
#                 aux_edades = edades[i]
#                 edades[i] = edades[j]
#                 edades[j] = aux_edades
#             elif edades[i] == edades[j]:
                
#                 aux_edades = edades[i]
#                 edades[i] = edades[j]
#                 edades[j] = aux_edades

#                 aux_nom = nombres[i]
#                 nombres[i] = nombres[j]
#                 nombres[j] = aux_nom
#     for i in range(len(edades)):
#         print("nombre:",nombres[i],"edad:", edades[i])