#mi archivo dibujo.py contiene:
# dibujar_tablero(posicion_jugador)

# mostrar_mensaje(pantalla, texto, color, fuente)

# mostrar_puntajes_pygame(pantalla)

# (y más adelante) funciones como dibujar_boton, mostrar_menu_interactivo, etc.

import pygame



BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 50, 50)
AZUL = (0, 0, 255)
AZUL_VACIO= (100, 150, 255) 
AZUL_CLARO = (0, 150, 255)
VERDE_CLARO = (0, 255, 155)
VIOLETA_VACIO = (50, 17, 86)
VERDE = (50, 255, 50)
GRIS = (150,150, 150)
AMARILLO = (250, 250, 100)



# Tablero lógico
tablero = [0, 1, 0, 0, 0, 3, 0, 0, 0, 0,
           0, 1, 0, 0, 2, 1, 1, 0, 0, 0,
           1, 0, 2, 0, 0, 0, 1, 0, 0, 0]

# Tamaño de casillas
ANCHO_CASILLA = 60
ALTO_CASILLA = 60
COLUMNAS = 10
#fuente = pygame.font.SysFont("Arial Narrow", 28)
# posicion_jugador = 14

def dibujar_tablero(pantalla, fuente, tablero, posicion_jugador, ANCHO_CASILLA, ALTO_CASILLA, COLUMNAS, imagenes, personaje_elegido):
    """
    Dibuja el tablero completo y la ficha del jugador.

    Parametro:        
        pantalla (pygame.Surface): Superficie donde se dibuja.
        fuente (pygame.font.Font): Fuente para mostrar los números.
        tablero (list): Lista de valores del tablero.
        posicion_jugador (int): Índice actual de la posición del jugador en el tablero. #14     
        ANCHO_CASILLA (int): Ancho de cada casilla. #60
        ALTO_CASILLA (int): Alto de cada casilla.   #60
        COLUMNAS (int): Cantidad de columnas del tablero.  #10   
    """
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

    if personaje_elegido != "":
        personaje_img = imagenes[personaje_elegido] 
        # Calcular la posición de la casilla
        #x = columna * ANCHO_CASILLA + 50
        #y = fila * ALTO_CASILLA + 320
        #pantalla.blit(personaje_img, (x, y))
         # Calcular posición centrada
        pos_x = centro_x - personaje_img.get_width() // 2
        pos_y = centro_y - personaje_img.get_height() // 2
        pantalla.blit(personaje_img, (pos_x, pos_y))
        #pantalla.blit(personaje_img, (centro_x, centro_y))
    pygame.display.update()
# Dibujar un círculo (la ficha del jugador) en el centro de la casilla
    #pygame.draw.circle(pantalla, AMARILLO, (centro_x, centro_y), 10)
# - pantalla: dónde dibujar - AMARILLO: color de la ficha - (centro_x, centro_y): posición en pantalla (centro de la casilla) - 10: radio del círculo


def mostrar_mensaje(pantalla, texto, color, fuente):
    """
    Muestra un mensaje centrado en pantalla con fondo violeta y espera 2 segundos.

    Parametro:
        pantalla (pygame.Surface): Pantalla donde se va a mostrar el mensaje.
        texto (str): Mensaje a mostrar.
        color (tuple): Color del texto (por ejemplo, blanco o rojo).
        fuente (pygame.font.Font): Fuente utilizada para renderizar el texto.
    """
    pantalla.fill(VIOLETA_VACIO)  # Limpia la pantalla con el color de fondo
    mensaje = fuente.render(texto, True, color) # Renderiza el texto como una imagen
    pantalla.blit(mensaje, (250, 250)) # Dibuja el texto en una posición fija (centro aproximado)
    pygame.display.update() # Actualiza la pantalla para mostrar los cambios
    pygame.time.wait(2000) # Espera 2 segundos (2000 milisegundos)

# mostrar_mensaje(pantalla, "¡Ganaste!", VERDE, fuente)
# mostrar_mensaje(pantalla, "Fin del juego", BLANCO, fuente)
# mostrar_mensaje(pantalla, "¡Tiempo agotado!", ROJO, fuente)

def mostrar_puntajes_pygame(pantalla,fuente):
    """
    Muestra los 5 mejores puntajes del archivo Score.csv, ordenados de mayor a menor.

    Parámetro:
        pantalla (pygame.Surface): La pantalla donde se dibujan los puntajes.
    """
    pantalla.fill(VIOLETA_VACIO) # Limpia la pantalla con fondo violeta
    #aca ??
    #fuente = pygame.font.SysFont("Arial Narrow", 28)  # Fuente para el texto
    y = 50  # Coordenada vertical para mostrar el primer puntaje

    puntajes = [] # Lista para guardar los puntajes del archivo

    # Abrimos el archivo y leemos los nombres y puntajes
    archivo = open("Score.csv", "r")
    for linea in archivo:  # Recorre cada línea del archivo
        nombre = "" # Variable para guardar el nombre
        puntos_texto = "" # Variable para guardar los puntos como texto
        i = 0  # Usamos un índice para recorrer la línea carácter por carácter


        # Leer el nombre hasta la coma 
        while i < len(linea) and linea[i] != ",":  # Recorrer carácter por carácter hasta la coma (para obtener el nombre)
            nombre += linea[i]
            i += 1

        i += 1  # Saltear la coma

        # Leer los puntos después de la coma
        while i < len(linea) and linea[i] != "\n":
            puntos_texto += linea[i]
            i += 1

        if puntos_texto != "":
            puntos = int(puntos_texto) # Convierte los puntos a entero
        else:
            puntos = 0        
        puntajes.append([nombre, puntos]) # Agrega el nombre y puntos a la lista

    
    archivo.close() # Cierra el archivo

    # Ordenar los puntajes de mayor a menor usando algoritmo de burbujeo
    for i in range(len(puntajes) - 1):
        for j in range(i + 1, len(puntajes)):
            if puntajes[i][1] < puntajes[j][1]:  # Comparo puntos. Si el puntaje en i es menor al de j
                aux = puntajes[i]                # Uso auxiliar para intercambiar
                puntajes[i] = puntajes[j]
                puntajes[j] = aux

    # Mostrar solo los 5 primeros
    # Mostrar solo los primeros 5 sin usar min() ni break
    cantidad_a_mostrar = 5
    if len(puntajes) < 5:
        cantidad_a_mostrar = len(puntajes)

    for i in range(cantidad_a_mostrar):
        nombre = puntajes[i][0]
        puntos = puntajes[i][1]
        texto = fuente.render(f"{nombre}: {puntos}", True, BLANCO)
        pantalla.blit(texto, (50, y)) # Muestra el texto en la pantalla
        y += 30 # Baja 30 píxeles para el siguiente nombre
    
    
    pygame.display.update()
    #pygame.time.wait(5000)  # Espera 5 segundos antes de cerrar si funciona con esc lo borro 

    aviso =  fuente.render("Precione ESC para volver al menu", True, BLANCO)
    pantalla.blit(aviso, (50, 400))
    pygame.display.update()

    esperando = True 
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #esperando = False
                    return "menu"



    