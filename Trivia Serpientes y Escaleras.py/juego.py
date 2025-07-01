import random
from preguntas import *
from funciones import *

tablero = [0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 0, 2, 1, 1, 0, 0, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 0]


def jugar():
    """
    Inicia y controla una partida del juego de preguntas y tablero

    El jugador ingresa su nombre, comienza en una posición fija del tablero y debe responder preguntas
    Según si responde bien o mal, avanza o retrocede. También puede subir escaleras
    o bajar por serpientes, según la posición en el tablero

    El juego termina si:
        El jugador llega al primer o último casillero (pierde o gana)
        Decide no seguir jugando
        Se acaban las preguntas

    Al final de la partida, se guarda el puntaje en un archivo CSV y se muestran los puntajes

    Retorna:
        No retorna ningún valor
    """
    nombre = input("ingrese su nombre: ")
    posicion = 14 
    
    jugar_respuesta = input("¿Querés jugar? (s/n): ").lower()
    while jugar_respuesta != "s" and jugar_respuesta != "n":
        jugar_respuesta = input("Error. ¿Querés jugar? (s/n): ").lower()

    if jugar_respuesta  == "n":
        print("Fin del juego.") 
        return



    preguntas_disponibles = preguntas.copy()
    seguir_jugando = True

    while preguntas_disponibles != [] and seguir_jugando == True: #sigue jugando mientras haya preguntas disponibles y el jugador no haya decidido o perdido/ganado
        pregunta = random.choice(preguntas_disponibles)  # Elegir una pregunta al azar
        preguntas_disponibles.remove(pregunta)           # Sacarla para no repetir

        resultado = hacer_pregunta(pregunta)
        
        posicion = mover_jugador(posicion, resultado)
        
        posicion = serpiente_escalera(posicion, resultado, tablero)
    
        print(f"{nombre} estás en el casillero {posicion + 1}")
        
        seguir_jugando = verificar_estado(posicion, tablero, nombre)
    
    with open("Score.csv", "a") as archivo: #Comma Separated Values (valores separados por coma) #El modo "a" significa "append", es decir: agrega al final del archivo sin borrar lo anterior
        archivo.write(f"{nombre}, {posicion + 1}\n") #.write() escribe texto en el archivo

    print("puntajes guardados: ")    
    mostrar_puntajes()    

jugar_otra_vez = "s"

while jugar_otra_vez == "s":
    jugar()
    jugar_otra_vez = input("¿Querés jugar con otro jugador? (s/n): ").lower()

        
        
        
       
     

