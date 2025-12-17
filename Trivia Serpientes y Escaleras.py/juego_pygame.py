import pygame 
import random
from preguntas import* 

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 50, 50)
AZUL_VACIO= (100, 150, 255) 
VIOLETA_VACIO = (50, 17, 86)
VERDE = (50, 255, 50)
GRIS = (150,150, 150)
AMARILLO = (250, 250, 100)
pygame.init()
pantalla = pygame.display.set_mode(((800, 600)), pygame.RESIZABLE)
pygame.display.set_caption("juego de preguntas")
fuente = pygame.font.SysFont("Arial Narrow", 50) # Crea una fuente para mostrar texto, con tamaño 50

# Variables de control
esperando_respuesta = True
jugar_confirmado = False
#Preguntar si quiere jugar
while esperando_respuesta: #Este while sólo se detiene cuando esperando_respuesta vale False. (solo cambia a false con S o N) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        #Si se presionó una tecla...
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_s:     #Si la tecla presionada fue "s"
                jugar_confirmado = True     #confirma que el jugador quiere jugar
                esperando_respuesta = False  # Ya no esperamos más la respuesta y salimos del while
            elif event.key == pygame.K_n:    # Si la tecla presionada fue "n"
                jugar_confirmado = False     #confirma que NO quiere jugar
                esperando_respuesta = False  # Ya no esperamos más la respuesta y salimos del while
            # Si no es "s" o "n", no cambia nada y sigue esperando
 # Si presionó otra tecla (por ejemplo: a, t)
    #  no entra en ningún `if`, y la variable `esperando_respuesta` sigue siendo True
    #  entonces el while no termina y volvemos a mostrar la pregunta



    pantalla.fill(VIOLETA_VACIO)
    texto = fuente.render("Queres jugar? (s/n)", True, BLANCO)
    pantalla.blit(texto, (200, 250))
    pygame.display.update()
 
#Si no quiere jugar, termina
if jugar_confirmado == False:
    pantalla.fill(VIOLETA_VACIO)
    mensaje = fuente.render("Fin del juego", True, (BLANCO))  # Texto blanco
    pantalla.blit(mensaje, (250, 250))  # Posición del texto
    pygame.display.update()
    pygame.time.delay(2000)  # Espera 2 segundos antes de cerrar 
    # print("Fin del juego.")
    pygame.quit()
    exit()

def guardar_puntaje(nombre, posicion_jugador):
    with open("Score.csv", "a") as archivo:
        archivo.write(f"{nombre}, {posicion_jugador + 1}\n")


    
def mostrar_puntajes_pygame(pantalla):
    pantalla.fill(VIOLETA_VACIO)

    fuente = pygame.font.SysFont("Arial Narrow", 28)
    y = 50

    archivo = open("Score.csv", "r")
    for linea in archivo:
        
        texto = fuente.render(linea, True, BLANCO)  
        pantalla.blit(texto, (50, y))
        y += 30
    archivo.close()

    pygame.display.update()
    pygame.time.wait(5000)

def jugar(pantalla, tablero, posicion_jugador):
    nombre = "" # Variable para almacenar el nombre del jugador 
    escribiendo_nombre = True # Bandera para controlar el bucle de escritura
    while escribiendo_nombre:
    # Bucle sigue hasta que se termine de escribir el nombre
        for event in pygame.event.get():
        # Captura todos los eventos del teclado, mouse, etc
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Si se cierra la ventana, termina el programa
        
            if event.type == pygame.KEYDOWN:
             # Si se presionó una tecla...
                if event.key == pygame.K_RETURN and nombre != "": # Si se presionó Enter y ya hay texto, termina la escritura
                    escribiendo_nombre = False  # Listo, terminamos de escribir
                elif event.key == pygame.K_BACKSPACE:  # Si se presionó Backspace, borra la última letra
                    nombre = nombre[:-1]  # Borra una letra
                else:
                #Si se presionó otra tecla, agrega el carácter al nombre
                    nombre += event.unicode  # Agrega letra nueva

        pantalla.fill(VIOLETA_VACIO)  #pinta la pantalla con un color de fondo

        # Mostrar instrucciones
        titulo = fuente.render("Ingresa su nombre:", True, BLANCO) #"renderizarlo" (prepararlo como imagen)
        #el texto "Ingresa su nombre" y lo dibuja en pantalla
        pantalla.blit(titulo, (100, 150)) # "bliteás" (dibujás) sobre la pantalla

        # Cuadro de texto  
        pygame.draw.rect(pantalla, BLANCO, (100, 200, 600, 50),2)  #Dibuja un rectángulo que actúa como el campo de entrada de texto

        # Mostrar lo que el jugador va escribiendo dentro del rectangulo
        entrada = fuente.render(nombre, True, BLANCO) #"renderizarlo" (prepararlo como imagen)
        pantalla.blit(entrada, (110, 210)) # "bliteás" (dibujás) sobre la pantalla
        # Renderiza el nombre y lo dibuja dentro del cuadro, con algo de margen

        pygame.display.update()  # Actualiza la pantalla con todos los cambios realizados


    preguntas_disponibles = preguntas.copy()
    seguir_jugando = True

    while preguntas_disponibles != [] and seguir_jugando:
        pantalla.fill(VIOLETA_VACIO)
        pygame.draw.rect(pantalla, VIOLETA_VACIO, (0, 0, 800, 300))  # Zona de preguntas #violeta vacio
        dibujar_tablero(posicion_jugador)  # Mostrar siempre el tablero

    # Elegir y mostrar pregunta
        pregunta = random.choice(preguntas_disponibles)
        preguntas_disponibles.remove(pregunta)

        
        fuente_preg = pygame.font.SysFont("Arial Narrow", 28)
        texto_preg = fuente_preg.render(pregunta["pregunta"], True, BLANCO)
        pantalla.blit(texto_preg, (50, 100))

        texto_a = fuente_preg.render(f"A: {pregunta['respuesta_a']}", True, BLANCO)
        pantalla.blit(texto_a, (70, 160))

        texto_b = fuente_preg.render(f"B: {pregunta['respuesta_b']}", True, BLANCO)
        pantalla.blit(texto_b, (70, 210))

        texto_c = fuente_preg.render(f"C: {pregunta['respuesta_c']}", True, BLANCO)
        pantalla.blit(texto_c, (70, 260))

        pygame.display.update()

         # Esperar respuesta A/B/C
        respuesta = ""
        inicio_tiempo = pygame.time.get_ticks()  # Tiempo actual en milisegundos
        tiempo_agotado = False
        while respuesta != "a" and respuesta != "b" and respuesta != "c" and tiempo_agotado == False:
            tiempo_actual = pygame.time.get_ticks()
            segundos_transcurridos = (tiempo_actual - inicio_tiempo) / 1000
            tiempo_restante = max(0, 10 - int(segundos_transcurridos))  # Redondeo hacia abajo

            # Limpiar sólo la zona donde va el tiempo
            rect_tiempo = pygame.Rect(540, 40, 180, 40)  # ajustá según tu layout
            pygame.draw.rect(pantalla, VIOLETA_VACIO, rect_tiempo)

            # Dibujar el tiempo restante
            texto_tiempo = fuente.render(f"Tiempo restante: {tiempo_restante} s", True, BLANCO)
            pantalla.blit(texto_tiempo, (540, 50))

            pygame.display.update(rect_tiempo)  # Actualiza sólo esa zona


            if segundos_transcurridos >= 10:
                # Tiempo agotado
                resultado = 0
                mostrar_mensaje("¡Tiempo agotado!", ROJO)
                tiempo_agotado = True

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
            
           

            # fuente_tiempo = pygame.font.SysFont("Arial Narrow", 30)
            # texto_tiempo = fuente_tiempo.render(f"Tiempo restante: {tiempo_restante} s", True, BLANCO)
            # pantalla.blit(texto_tiempo, (550, 50))  # Ubicación arriba a la derecha, ajustá como quieras

            # pygame.display.update()


         # Ver si la respuesta fue correcta
        if respuesta == pregunta["respuesta_correcta"]:
            resultado = 1
        else:
            resultado = 0

        # Movimiento base
        movimiento = 1 + tablero[posicion_jugador]

        if resultado == 1:
            posicion_jugador += movimiento
        else:
            posicion_jugador -= movimiento

        # Limitar los bordes del tablero
        if posicion_jugador < 0:
            posicion_jugador = 0
        elif posicion_jugador >= len(tablero):
            posicion_jugador = len(tablero) - 1
      
        # Mostrar nueva posición
        dibujar_tablero(posicion_jugador)
        pygame.display.update()
        pygame.time.wait(1000)

        # Ver si ganó o perdió
        if posicion_jugador == 0:
            mostrar_mensaje("¡Perdiste!", ROJO)
            seguir_jugando = False
            # Guardar en el archivo
            guardar_puntaje(nombre, posicion_jugador)
        elif posicion_jugador == len(tablero) - 1:
            mostrar_mensaje("¡Ganaste!", VERDE)
            seguir_jugando = False
            # Guardar en el archivo
            guardar_puntaje(nombre, posicion_jugador)


        if seguir_jugando:  # Sólo pregunta si no ganó ni perdió aún
            pantalla.fill(VIOLETA_VACIO)
            mensaje_posicion = fuente.render(f"{nombre} estás en el casillero {posicion_jugador + 1}", True, BLANCO)
            pantalla.blit(mensaje_posicion, (150, 200))
            mensaje = fuente.render("¿Querés seguir jugando? (s/n)", True, BLANCO)
            pantalla.blit(mensaje, (150, 250))
            pygame.display.update()

            seguir_respondiendo = True
            seguir_jugando = False  # Por defecto corta si no responde 's'

            while seguir_respondiendo:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            seguir_jugando = True
                            seguir_respondiendo = False
                        elif event.key == pygame.K_n:
                            seguir_jugando = False
                            guardar_puntaje(nombre, posicion_jugador)
                            seguir_respondiendo = False

    #Si dijo que no quiere seguir, mostramos mensaje final y salimos
    if seguir_jugando == False:
        pantalla.fill(VIOLETA_VACIO)
        mensaje = fuente.render(f"{nombre} terminaste en la casilla {posicion_jugador + 1}", True, BLANCO)
        pantalla.blit(mensaje, (100, 200))
        pygame.display.update()
        pygame.time.wait(2000)

        mostrar_puntajes_pygame(pantalla)

    return posicion_jugador

 
# Tablero lógico
tablero = [0, 1, 0, 0, 0, 3, 0, 0, 0, 0,
           0, 1, 0, 0, 2, 1, 1, 0, 0, 0,
           1, 0, 2, 0, 0, 0, 1, 0, 0, 0]

# Tamaño de casillas
ANCHO_CASILLA = 60
ALTO_CASILLA = 60
COLUMNAS = 10
fuente = pygame.font.SysFont("Arial Narrow", 28)
posicion_jugador = 14

def dibujar_tablero(posicion_jugador):
    for i in range(len(tablero)): # Recorre cada casilla del tablero Para saber en qué fila y columna está la casilla número i
        fila = i // COLUMNAS      #Esta cuenta me da su posicion en la fila  # Divide el índice por la cantidad de columnas para saber en qué fila está
        columna = i % COLUMNAS    #Esta cuenta me da la posicion en la columna  # Saca el resto de la división para saber en qué columna está
       
        # Calculamos la coordenada horizontal (x) de la casilla en la pantalla (+ 50 y + 100 → agregan un margen para que el tablero no quede pegado al borde)
        x = columna * ANCHO_CASILLA + 50  # 50 es el margen desde el borde izquierdo  # posición horizontal con margen ( columna * ANCHO_CASILLA → te da cuántos pixeles hay que avanzar hacia la derecha)
        # Calculamos la coordenada vertical (y) de la casilla en la pantalla
        y = fila * ALTO_CASILLA + 320     # 320 es el margen desde arriba de la pantalla  # posición vertical con margen (# fila * ALTO_CASILLA     → te da cuántos pixeles hay que bajar)

        valor = tablero[i]
        if i == 0:
            color = (ROJO)  # rojo
        elif i == 29:
            color = (VERDE)    # verde 
        elif valor > 0:
            color = (AZUL_VACIO)  # azul
        else:
            color = GRIS
        # color = VERDE if valor > 0 else GRIS

        # Dibujar casilla
        pygame.draw.rect(pantalla, color, (x, y, ANCHO_CASILLA, ALTO_CASILLA))
        #Dibuja en pantalla  con color   en (x, y) y tamaño de la casilla
        # Dibujar el borde de la casilla en color negro (línea de grosor 2)
        pygame.draw.rect(pantalla, NEGRO, (x, y, ANCHO_CASILLA, ALTO_CASILLA), 2)
                                                                            # grosor del borde
        # Dibujar número en la casilla
        # Preparar el número de la casilla como texto a renderizar
        texto = fuente.render(str(valor), True, NEGRO) #el método .render() convierte el texto (acá, el valor del tablero) en una imagen para poder dibujarla en la pantalla.
#            fuente      texto      antialias (suavizado)     color
        # Dibujar el número dentro de la casilla, más o menos centrado
        pantalla.blit(texto, (x + 22, y + 18))
#                   coordenadas donde se "pega" el texto (ajustadas para que quede centrado)


#Obtener la fila donde está el jugador (cada 10 casillas cambia de fila)
    # Dibujar la ficha del jugador
    fila = posicion_jugador // COLUMNAS     #la división entera da el número de fila
    columna = posicion_jugador % COLUMNAS   #el Modulo da el resto, o sea la columna
#Calcular la posición X y Y de la casilla en la pantalla
    x = columna * ANCHO_CASILLA + 50    #50 es el margen desde la izquierda
    y = fila * ALTO_CASILLA + 320       #320 es el margen desde arriba

#Calcular el centro de esa casilla (para dibujar la ficha bien en el medio)
    # Coordenadas del centro de la casilla
    centro_x = x + ANCHO_CASILLA // 2   #centro horizontal
    centro_y = y + ALTO_CASILLA // 2    #centro vertical

# Dibujar un círculo (la ficha del jugador) en el centro de la casilla
    pygame.draw.circle(pantalla, AMARILLO, (centro_x, centro_y), 10)
# - pantalla: dónde dibujar - AMARILLO: color de la ficha - (centro_x, centro_y): posición en pantalla (centro de la casilla) - 10: radio del círculo



def mostrar_mensaje(texto, color):
    pantalla.fill(VIOLETA_VACIO)
    fuente = pygame.font.SysFont("Arial Narrow", 40)
    mensaje = fuente.render(texto, True, color)
    pantalla.blit(mensaje, (250, 250))
    pygame.display.update()
    pygame.time.wait(2000)



jugar_otra_vez = True

while jugar_otra_vez:
    # Llamás a la función que inicia el juego
    jugar(pantalla, tablero, posicion_jugador)

    # Mostrás el mensaje
    pantalla.fill(VIOLETA_VACIO)
    texto = fuente.render("¿Querés jugar con otro jugador? (s/n)", True, BLANCO)
    pantalla.blit(texto, (100, 250))
    pygame.display.update()

    esperando_respuesta = True
    while esperando_respuesta:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    esperando_respuesta = False
                    jugar_otra_vez = True
                elif event.key == pygame.K_n:
                    esperando_respuesta = False
                    jugar_otra_vez = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pantalla.fill(VIOLETA_VACIO)
    dibujar_tablero(posicion_jugador)
    pygame.display.update()



