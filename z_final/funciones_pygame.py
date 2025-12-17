# Contiene funciones auxiliares del juego (puntajes, ingreso de nombre, selección de personaje)
import pygame
BLANCO = (255, 255, 255)
VIOLETA_VACIO = (50, 17, 86)
ROJO = (255, 50, 50)

def guardar_puntaje(nombre, posicion_jugador):
    """
    Guarda el puntaje del jugador en el archivo Score.csv.

    parametros:
        nombre (str): Nombre del jugador.
        posicion_jugador (int): Posición final del jugador en el tablero.    """   
    #Uso with para abrir el archivo porque se cierra automáticamente cuando termina el bloque.
    with open("Score.csv", "a") as archivo:
        #La función guarda el puntaje en un archivo, por eso los datos persisten aunque se cierre el juego
        archivo.write(f"{nombre}, {posicion_jugador + 1}\n")  #Guarda el nombre y la posición (le suma 1 porque el tablero empieza en indice 0)

def nombre_ya_existe(nombre: str) -> bool:
    """
    Verifica si un nombre ya está en Score.csv

    Parámetro:
        nombre (str): Nombre que se quiere verificar.

    Retorna:
        bool: True si el nombre ya está guardado, False si no.
    """
    with open("Score.csv", "r") as archivo:
        for linea in archivo:   # recorre línea por línea el archivo Score.csv
            nombre_guardado = "" 
            posicion = 0  # Índice para recorrer la línea
            
            # Leer carácter por carácter hasta encontrar una coma
            while posicion < len(linea) and linea[posicion] != ",": # se fija cada letra del nombre y lo agrega en nombre_guardado hata encontrar una ","
                nombre_guardado += linea[posicion]  # agrega cada letra en nombre_guardado hasta encontrar una ","
                posicion += 1 #cuando suma una posicion es la siguiente letra 

            # Comparar ignorando mayúsculas y minúsculas
            if nombre_guardado.lower() == nombre.lower():
                return True  # Ya existe

    return False  # Si recorrió todo y no lo encontró

def pedir_nombre_pygame(pantalla, fuente) -> str:
    """
    Pide un nombre de jugador. Verifica que no esté vacío ni repetido.

    Retorna:
        str: nombre válido
    """
    nombre = ""
    escribiendo = True
    mensaje_error = ""  # Acá guardamos un posible mensaje de error (nombre vacío o repetido)

    while escribiendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:     # Si se presiona una tecla
                if event.key == pygame.K_RETURN:    ## Si se presiona enter
                    if nombre == "":     # Si no escribió nada: mensaje de error
                        mensaje_error = "El nombre no puede estar vacío"
                    elif nombre_ya_existe(nombre):  # Si el nombre ya está en Score.csv: mensaje de error
                        mensaje_error = "Ese nombre ya esta en uso"
                        nombre = ""
                    else:
                        escribiendo = False # salimos del bucle
                elif event.key == pygame.K_BACKSPACE: # Si presiona borrar
                    nombre = nombre[:-1]
                else:
                    nombre += event.unicode  # Agrega la letra que escribió

        pantalla.fill(VIOLETA_VACIO) # Limpia la pantalla con color de fondo

        # Título Mostrar instrucciones
        texto_titulo = fuente.render("Ingresa tu nombre:", True, BLANCO)
        pantalla.blit(texto_titulo, (100, 150))

        # Rectángulo blanco para escribir
        pygame.draw.rect(pantalla, BLANCO, (100, 200, 600, 50), 2)

        # Nombre escrito # Mostrar lo que el jugador va escribiendo
        texto_nombre = fuente.render(nombre, True, BLANCO)
        pantalla.blit(texto_nombre, (110, 210))

        # Mostrar mensaje de error si hay
        if mensaje_error != "":
            texto_error = fuente.render(mensaje_error, True, ROJO)
            pantalla.blit(texto_error, (100, 280))

        pygame.display.update() # Refresca la pantalla para mostrar los cambios

    return nombre


def seleccionar_personaje(pantalla, fuente, imagenes):
    """
    Permite al jugador seleccionar un personaje usando el teclado.

    Retorna:
        str: clave del personaje seleccionado
    """
    seleccion = " "
    while seleccion == " ":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    seleccion = "personaje_mas"
                elif event.key == pygame.K_2:
                    seleccion = "personaje_fem"

        pantalla.fill((50, 50, 100))  # Fondo

        titulo = fuente.render("Elige tu personaje", True, (BLANCO))
        pantalla.blit(titulo, (150, 50))

        # Mostrar personaje 1
        pantalla.blit(imagenes["personaje_mas_grande"], (150, 150))
        pantalla.blit(fuente.render("1. Personaje 1", True, (BLANCO)), (130, 250))

        # Mostrar personaje 2
        pantalla.blit(imagenes["personaje_fem_grande"], (400, 150))
        pantalla.blit(fuente.render("2. Personaje 2", True, (BLANCO)), (380, 250))

        pygame.display.update()

    return seleccion
  