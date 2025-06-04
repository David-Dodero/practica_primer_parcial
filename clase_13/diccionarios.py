#diccionario = son mutables 
#key = clave (el key es como el indice)
#vlue = valor 
#clave + valor = item

jugadores = [
       {"nombre": "Ana", "edad": 43, "puntos":[10,12,14]},  
       {"nombre": "Juan", "edad": 32, "puntos":[12,10,11]},  
       {"nombre": "Pedro", "edad": 28, "puntos":[9,15,11]},
       {"nombre": "Sol", "edad": 31, "puntos":[11,8,15]}
]

#buscar el de menor edad y mostrar su nombre 
menor_edad = jugadores[0]["edad"]
jugador_menor = jugadores[0]
for e_jugador in jugadores:
    if e_jugador["edad"] < menor_edad:
        menor_edad = e_jugador ["edad"]
        jugador_menor = e_jugador

print(jugador_menor)

# for i in range(len(jugadores)):
#     if jugadores[i]  