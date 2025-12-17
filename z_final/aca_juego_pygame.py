# Este archivo contiene la logica principal del juego
# Aca se manejan las preguntas, el tiempo, el movimiento del jugador, los sonidos, las imágenes y las condiciones de ganar o perder
#Aca está la lógica del juego, mientras que el main solo controla el flujo
import pygame
import random
from preguntas import*
from funciones_pygame import guardar_puntaje, pedir_nombre_pygame
from dibujo import dibujar_tablero, ANCHO_CASILLA, ALTO_CASILLA, COLUMNAS
from menu import menu_despues_de_juego
BLANCO = (255, 255, 255)
VIOLETA_VACIO = (50, 17, 86)
ROJO = (255, 50, 50)
VERDE = (50, 255, 50)

def jugar(pantalla, tablero, posicion_jugador, fuente, imagenes, sonidos, personaje_elegido):
    """
    Lógica principal del juego
    Muestra preguntas, mueve al jugador, y guarda los puntajes.
    Pide el nombre del jugador
    Muestra preguntas con tiempo límite
    Mueve al jugador en el tablero según las respuestas
    Reproduce sonidos e imágenes
    Guarda el puntaje
    Devuelve el resultado final de la partida
    """
    #1. PEDIR NOMBRE
    nombre = pedir_nombre_pygame(pantalla, fuente)

    preguntas_disponibles = preguntas.copy()  # Copiamos para no modificar la original
    seguir_jugando = True

    # Bucle principal de la partida
    # continúa mientras haya preguntas y el jugador decida seguir
    while preguntas_disponibles != [] and seguir_jugando == True:

        # LIMPIAR PANTALLA Y MOSTRAR TABLERO
        pantalla.fill((VIOLETA_VACIO)) 
        dibujar_tablero(pantalla, fuente, tablero, posicion_jugador, ANCHO_CASILLA, ALTO_CASILLA, COLUMNAS, imagenes, personaje_elegido)

        # Selecciona una pregunta aleatoria y la elimina
        # para evitar que se repita
        pregunta = random.choice(preguntas_disponibles)
        preguntas_disponibles.remove(pregunta) #sacamos la pregunta para que no lo vuelva a preguntar 

        
        pantalla.blit(fuente.render(pregunta["pregunta"], True, (BLANCO)), (50, 100))
        pantalla.blit(fuente.render(f"A: {pregunta['respuesta_a']}", True, (BLANCO)), (70, 160))
        pantalla.blit(fuente.render(f"B: {pregunta['respuesta_b']}", True, (BLANCO)), (70, 210))
        pantalla.blit(fuente.render(f"C: {pregunta['respuesta_c']}", True, (BLANCO)), (70, 260))
        pygame.display.update()

        # ESPERAR RESPUESTA A/B/C CON TIEMPO LIMITE 
        respuesta = ""
        # Se inicia el temporizador para limitar el tiempo de respuesta
        inicio_tiempo = pygame.time.get_ticks()  #guarda el tiempo en milisegundos desde que arrancó pygame
        tiempo_agotado = False

        while respuesta != "a" and respuesta != "b" and respuesta != "c" and tiempo_agotado == False:
            tiempo_actual = pygame.time.get_ticks() 
            segundos_transcurridos = (tiempo_actual - inicio_tiempo) / 1000 #cuantos segundos pasaron desde que aparecio la pregunta
            tiempo_restante = int(10 - segundos_transcurridos)
            if tiempo_restante < 0:
                tiempo_restante = 0
            
            # Paso 1: Borrar el número anterior (repintar fondo violeta solo en esa parte)
            pygame.draw.rect(pantalla, VIOLETA_VACIO, (550, 50, 100, 40))  # ← ajustá la posición si querés
            # Paso 2: Dibujar el número nuevo (el tiempo restante)
            texto_tiempo = fuente.render(str(tiempo_restante), True, BLANCO)
            pantalla.blit(texto_tiempo, (550, 50))  # ← misma posición que el rectángulo
            # Paso 3: Actualizar la pantalla
            pygame.display.update()

            if segundos_transcurridos >= 10:
                pantalla.fill(VIOLETA_VACIO)
                pantalla.blit(imagenes["reloj"],(250, 150))
                pygame.display.update()
                pygame.time.wait(2000)                  
                resultado = 0
                tiempo_agotado = True
                seguir_jugando = False
                
            
            #Captura eventos del teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        respuesta = "a"
                    elif event.key == pygame.K_b:
                        respuesta = "b"
                    elif event.key == pygame.K_c:
                        respuesta = "c"

        # CORREGIR RESPUESTA (solo si no se agotó el tiempo)
        if tiempo_agotado == False: 
            if respuesta == pregunta["respuesta_correcta"]:
                resultado = 1                
            else:
                resultado = 0 

        # MOVER AL JUGADOR
        # Calcula el movimiento según la respuesta
        # y el valor del tablero en la posición actual
        movimiento = 1 + tablero[posicion_jugador]
        if resultado == 1:
            posicion_anterior = posicion_jugador
            posicion_jugador += movimiento
            if tablero[posicion_anterior] > 0:
                pantalla.fill(VIOLETA_VACIO)
                pygame.display.update()
                pantalla.blit(imagenes["escalera"], (30, 30)) 
                sonidos["escalera"].play()
                
        else:
            posicion_anterior = posicion_jugador
            posicion_jugador -= movimiento
            if tablero[posicion_anterior] > 0:
                pantalla.fill(VIOLETA_VACIO)
                pygame.display.update()
                sonidos["serpiente"].play()
                pantalla.blit(imagenes["serpiente"], (200, 100))                
        pygame.display.update()
        pygame.time.wait(2000)  # pequeña pausa para que se vea

        # CONTROLAR QUE NO SALGA DEL TABLERO
        if posicion_jugador < 0:
            posicion_jugador = 0
        elif posicion_jugador >= len(tablero):
            posicion_jugador = len(tablero) - 1

        # REVISAR SI GANÓ O PERDIÓ
        if posicion_jugador == 0:
            #parar el sonido de fondo
            pygame.mixer.music.stop()  # Detener música de fondo
            pantalla.fill(VIOLETA_VACIO)
            pantalla.blit(imagenes["game_over"], (250, 100))  # Ajustá según resolución
            mensaje = fuente.render("Perdiste", True, ROJO)
            pantalla.blit(mensaje, (300, 400))
            pygame.display.update()
            sonidos["perdiste"].play()  # Reproduce sonido derrota
            pygame.time.wait(2000)  
            guardar_puntaje(nombre, posicion_jugador)
            seguir_jugando = False  
              
            otra_partida = menu_despues_de_juego(pantalla, fuente) == "1"
    
            if otra_partida:
                pygame.mixer.music.play(-1)  # Reanudar música en loop
            return "perdiste"
        elif posicion_jugador == len(tablero) - 1:
            #parar el sonido de fondo
            pygame.mixer.music.stop()  # Detener música de fondo            
            pantalla.fill(VIOLETA_VACIO)
            pantalla.blit(imagenes["ganaste"],(250, 100))
            mensaje = fuente.render("Ganaste", True, VERDE)
            pantalla.blit(mensaje,(300, 400))
            pygame.display.update()
            sonidos["ganaste"].play() # Reproduce sonido derrota
            pygame.time.wait(2000)  
            guardar_puntaje(nombre, posicion_jugador)
            seguir_jugando = False  
            
            otra_partida = menu_despues_de_juego(pantalla, fuente) == "1"
    
            if otra_partida:
                pygame.mixer.music.play(-1)  # Reanudar música en loop
            return "ganaste"
        #PREGUNTAR SI QUIERE SEGUIR JUGANDO
        pantalla.fill((VIOLETA_VACIO))
        dibujar_tablero(pantalla, fuente, tablero, posicion_jugador, ANCHO_CASILLA, ALTO_CASILLA, COLUMNAS, imagenes, personaje_elegido)
        pantalla.blit(fuente.render(f"{nombre}, estás en el casillero {posicion_jugador + 1}", True, (BLANCO)), (150, 200))
        pantalla.blit(fuente.render("¿Querés seguir jugando? (s/n)", True, (BLANCO)), (150, 250))
        pygame.display.update()

        esperando = True
        while esperando == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        seguir_jugando = True
                        esperando = False
                    elif event.key == pygame.K_n:
                        seguir_jugando = False
                        guardar_puntaje(nombre, posicion_jugador)
                        pantalla.fill(VIOLETA_VACIO)
                        pantalla.blit(imagenes["fin_del_juego"],(250, 100)) 
                        pygame.display.update()
                        pygame.time.wait(2000)
                        esperando = False
                        return "abandono"
        #La posición actual en el tablero
        pantalla.fill((VIOLETA_VACIO))
        pantalla.blit(fuente.render(f"{nombre} estas en la casilla {posicion_jugador + 1}", True, (BLANCO)), (100, 200))
        pygame.display.update()
        pygame.time.wait(2000)
      

    return posicion_jugador