#diccionario = son mutables 
#key = clave (el key es como el indice)
#vlue = valor 
#clave + valor = item
# for alumno in estudiantes: #te muestra que keys o claves tiene 
#     print("Claves que tiene el alumno:", alumno.keys())

dic = { #key
        "Nombre": "Ana", #value
        "Edad": 27,
        "Documento": 45454545
    }
print(dic)
#{'Nombre': ‘Ana', 'Edad': 27, 'Documento': 45454545}
print(dic.keys()) #dict_keys(['Nombre', 'Edad', 'Documento'])
print(dic.values()) #dict_values(['Ana', 27, 45454545])
print(dic.items()) #dict_items([('Nombre', 'Ana'), ('Edad', 27), ('Documento', 45454545)])

#Acceder y modificar elementos
dic["Edad"]=33
print(dic) #{'Nombre': 'Ana', 'Edad': 33, 'Documento': 45454545}

#Si el key al que accedemos no existe, se añadeautomáticamente.
dic["Telefono"]= "123"
print(dic) #{'Nombre': 'Ana', 'Edad': 33, 'Documento': 45454545, 'Telefono': '123'}

#castear un diccionario a una lista 
lista = list(dic.values()) 
print(lista) #['Ana', 27, 45454545]
lista = list(dic.keys()) 
print(lista) #['Nombre', 'Edad', 'Documento']
lista = list(dic.items()) 
print(lista) #[('Nombre', 'Ana'), ('Edad', 27),('Documento', 45454545)]

#Iterar diccionario
for e_dic in dic: #e_dic == elemento del diccionario 
    print(e_dic) #Nombre #Edad #Documento # telefono
#Imprime los keys del diccionario 

#Se puede imprimir también solo el value.
for e_dic in dic:
    print(dic[e_dic]) #Ana #27 #45454545

#Diccionarios anidados
#Los diccionarios en Python pueden contener uno dentro de otro. Para acceder se debe especificar cada key entre corchetes []
dic = { "Nombre": "Ana",
        "Edad": 27,
        "Documento": 45454545,
        "Domicilio":{ "calle": "Solis",
        "numero": 345,
        "localidad": "Avellaneda"
        }
    }
print(dic["Nombre"]) #Ana
print(dic["Domicilio"]["calle"]) #Solis

#Los diccionarios también pueden contener listas[] donde a cada elemento se debe acceder por su índice/posición.
dic = {
        "Nombre": "Ana",
        "Edad": 27,
        "Documento": 45454545,
        "telefonos": [123,456]
    }
print(dic["telefonos"][1]) #456


jugadores = [
       {"nombre": "Ana", "edad": 43, "puntos":[10,12,14]},  
       {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},  
       {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
       {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
]

#buscar el de menor edad y mostrar su nombre 
#Jugadores es una lista de diccionarios, donde cada diccionario representa un jugador con la clave "edad", "nombre" y "puntos".
#Guardamos la edad del primer jugador como la menor edad encontrada hasta el momento
menor_edad = jugadores[0]["edad"]
# Guardamos el primer jugador como el jugador más joven por ahora
jugador_menor = jugadores[0]
# Recorremos la lista de jugadores uno por uno
for e_jugador in jugadores:
    # Si encontramos un jugador con una edad menor a la que teníamos guardada
    if e_jugador["edad"] < menor_edad:
        # Actualizamos la menor edad con la nueva edad más baja encontrada
        menor_edad = e_jugador["edad"]
        # También actualizamos el jugador más joven con este nuevo jugador
        jugador_menor = e_jugador
# Mostramos en pantalla el diccionario completo del jugador más joven
print(jugador_menor)






