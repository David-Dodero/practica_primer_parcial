# def dibujar_tablero(posicion_jugador):
#     for i in range(len(tablero)): # Recorre cada casilla del tablero Para saber en qué fila y columna está la casilla número i
#         fila = i // COLUMNAS      #Esta cuenta me da su posicion en la fila  # Divide el índice por la cantidad de columnas para saber en qué fila está
#         columna = i % COLUMNAS    #Esta cuenta me da la posicion en la columna  # Saca el resto de la división para saber en qué columna está
       
#         # Calculamos la coordenada horizontal (x) de la casilla en la pantalla (+ 50 y + 100 → agregan un margen para que el tablero no quede pegado al borde)
#         x = columna * ANCHO_CASILLA + 50  # 50 es el margen desde el borde izquierdo  # posición horizontal con margen ( columna * ANCHO_CASILLA → te da cuántos pixeles hay que avanzar hacia la derecha)
#         # Calculamos la coordenada vertical (y) de la casilla en la pantalla
#         y = fila * ALTO_CASILLA + 100     # 100 es el margen desde arriba de la pantalla  # posición vertical con margen (# fila * ALTO_CASILLA     → te da cuántos pixeles hay que bajar)

#         valor = tablero[i]
#         if i == 0:
#             color = (ROJO)  # rojo
#         elif i == 29:
#             color = (VERDE)    # verde 
#         elif valor > 0:
#             color = (AZUL_VACIO)  # azul
#         else:
#             color = GRIS
#         # color = VERDE if valor > 0 else GRIS

#         # Dibujar casilla
#         pygame.draw.rect(pantalla, color, (x, y, ANCHO_CASILLA, ALTO_CASILLA))
#         #              ↑        ↑       ↑  ↑  ↑              ↑
#         #Dibuja en pantalla  con color   en (x, y) y tamaño de la casilla
#         # Dibujar el borde de la casilla en color negro (línea de grosor 2)
#         pygame.draw.rect(pantalla, NEGRO, (x, y, ANCHO_CASILLA, ALTO_CASILLA), 2)
#         #                             ↑                  ↑                     ↑ grosor del borde
#         # Dibujar número en la casilla
#         # Preparar el número de la casilla como texto a renderizar
#         texto = fuente.render(str(valor), True, NEGRO) #el método .render() convierte el texto (acá, el valor del tablero) en una imagen para poder dibujarla en la pantalla.
#         #        ↑          ↑           ↑
# #            fuente      texto      antialias (suavizado)     color
#         # Dibujar el número dentro de la casilla, más o menos centrado
#         pantalla.blit(texto, (x + 22, y + 18))
# #                             ↑       ↑
# #                   coordenadas donde se "pega" el texto (ajustadas para que quede centrado)


# #Obtener la fila donde está el jugador (cada 10 casillas cambia de fila)
#     # Dibujar la ficha del jugador
#     fila = posicion_jugador // COLUMNAS     #la división entera da el número de fila
#     columna = posicion_jugador % COLUMNAS   #el Modulo da el resto, o sea la columna
# #Calcular la posición X y Y de la casilla en la pantalla
#     x = columna * ANCHO_CASILLA + 50    #50 es el margen desde la izquierda
#     y = fila * ALTO_CASILLA + 100       #100 es el margen desde arriba

# #Calcular el centro de esa casilla (para dibujar la ficha bien en el medio)
#     # Coordenadas del centro de la casilla
#     centro_x = x + ANCHO_CASILLA // 2   #centro horizontal
#     centro_y = y + ALTO_CASILLA // 2    #centro vertical

# # Dibujar un círculo (la ficha del jugador) en el centro de la casilla
#     pygame.draw.circle(pantalla, AMARILLO, (centro_x, centro_y), 10)
# # - pantalla: dónde dibujar - AMARILLO: color de la ficha - (centro_x, centro_y): posición en pantalla (centro de la casilla) - 10: radio del círculo

from preguntas2 import*
import pygame

pygame.init()

# Configuración básica
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Test Pregunta Pygame")



def hacer_pregunta_pygame(pantalla, pregunta_dict):
    """
    Muestra la pregunta en pantalla y espera que el jugador responda con A, B o C.
    Devuelve 1 si es correcta, 0 si es incorrecta.
    """
    fuente = pygame.font.SysFont("Arial Narrow", 28)
    esperando_respuesta = True
    respuesta = ""

    while esperando_respuesta:
        pantalla.fill((50, 17, 86))  # VIOLETA_VACIO

        # Mostrar pregunta y opciones
        texto_preg = fuente.render(pregunta_dict["pregunta"], True, (255, 255, 255))
        pantalla.blit(texto_preg, (50, 100))

        texto_a = fuente.render(f"A: {pregunta_dict['respuesta_a']}", True, (255, 255, 255))
        pantalla.blit(texto_a, (70, 160))

        texto_b = fuente.render(f"B: {pregunta_dict['respuesta_b']}", True, (255, 255, 255))
        pantalla.blit(texto_b, (70, 210))

        texto_c = fuente.render(f"C: {pregunta_dict['respuesta_c']}", True, (255, 255, 255))
        pantalla.blit(texto_c, (70, 260))

        pygame.display.update()

        # Esperar respuesta del jugador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    respuesta = "a"
                    esperando_respuesta = False
                elif event.key == pygame.K_b:
                    respuesta = "b"
                    esperando_respuesta = False
                elif event.key == pygame.K_c:
                    respuesta = "c"
                    esperando_respuesta = False

      # Mostrar resultado unos segundos antes de salir
    pantalla.fill((50, 17, 86))
    if respuesta == pregunta_dict["respuesta_correcta"]:
        texto_res = fuente.render("¡Correcto!", True, (0, 255, 0))
        resultado = 1
    else:
        texto_res = fuente.render("Incorrecto", True, (255, 0, 0))
        resultado = 0
    pantalla.blit(texto_res, (50, 200))
    pygame.display.update()
    pygame.time.delay(1500)  # Espera 1.5 segundos para que el jugador vea el mensaje

    return resultado


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

