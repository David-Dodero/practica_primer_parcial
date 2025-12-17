"""
Archivo principal del juego Trivia Serpientes y Escaleras.

Se encarga de:
 Inicializar pygame
 Cargar recursos (imágenes y sonidos)
 Controlar el flujo del juego mediante estados
 Llamar a los menus y a la logica principal del juego
"""
# El main importa los menus, la logica del juego, funciones de dibujo y selección de personaje
# El main no contiene logica del juego, solo controla el flujo del juego

import pygame
from menu import menu_principal, menu_despues_de_juego
from aca_juego_pygame import jugar
from dibujo import mostrar_puntajes_pygame ,dibujar_tablero, tablero, ANCHO_CASILLA, ALTO_CASILLA, COLUMNAS
from funciones_pygame import seleccionar_personaje

posicion_jugador = 14

#Inicializo pygame, creo la ventana, defino la fuente y cargo música de fondo en loop.
pygame.init()
pantalla = pygame.display.set_mode(((800, 600)), pygame.RESIZABLE)
pygame.display.set_caption("Trivia Serpientes y Escaleras")
fuente = pygame.font.SysFont("Arial Narrow", 28)
# Inicializar mixer 
pygame.mixer.init()
# Cargar música de fondo
pygame.mixer.music.load("z_final/sonidos/guitarra.mp3")
pygame.mixer.music.set_volume(0.2) #volumen de la guitarra
pygame.mixer.music.play(-1)  # loop infinito

#Uso diccionarios porque es mas practico, tengo todas las imágenes y sonidos
#en un solo lugar y después solo los llamo cuando los necesito
#cargar los sonidos en un diccionario
sonidos = {
   "serpiente": pygame.mixer.Sound("z_final/sonidos/snake.mp3"),
    "escalera": pygame.mixer.Sound("z_final/sonidos/escaleras_corto.mp3"),
    "ganaste": pygame.mixer.Sound("z_final/sonidos/ganaste.mp3"),
    "perdiste": pygame.mixer.Sound("z_final/sonidos/perdedor.mp3")
}

# Cargar y escalar imágenes en un diccionario
imagenes = {
    "escalera":  pygame.transform.scale(pygame.image.load("z_final/imagenes/escalera1.png").convert_alpha(), (300, 350)),
    "serpiente": pygame.transform.scale(pygame.image.load("z_final/imagenes/serpiente.png").convert_alpha(), (300, 300)),
    "ganaste":   pygame.transform.scale(pygame.image.load("z_final/imagenes/ganaste.png").convert_alpha(),(300, 300)),
    "perdiste":  pygame.transform.scale(pygame.image.load("z_final/imagenes/perdiste.png").convert_alpha(), (300, 300)),
    "fin_del_juego": pygame.transform.scale(pygame.image.load("z_final/imagenes/findeljuego1.png").convert_alpha(), (300, 300)),
    "game_over": pygame.transform.scale(pygame.image.load("z_final/imagenes/game_over1.png").convert_alpha(), (300, 300)),
    "personaje_mas": pygame.transform.scale(pygame.image.load("z_final/imagenes/personaje_mas.png").convert_alpha(),(50, 50)),
    "personaje_fem": pygame.transform.scale(pygame.image.load("z_final/imagenes/personaje_fem.png").convert_alpha(),(50, 50)),
    "personaje_mas_grande": pygame.transform.scale(pygame.image.load("z_final/imagenes/personaje_mas.png").convert_alpha(), (100, 100)),
    "personaje_fem_grande": pygame.transform.scale(pygame.image.load("z_final/imagenes/personaje_fem.png").convert_alpha(), (100, 100)),
    "reloj": pygame.transform.scale(pygame.image.load("z_final/imagenes/reloj.jpg").convert_alpha(),(300,350)),
}

#El flujo del juego se controla mediante un bucle principal y una variable de estado
# Variable de control del bucle principal
jugando = True
estado = "menu_principal"

while jugando == True:
    # muestra el menu principal
    #if mostrar_menu_principal:
    if estado == "menu_principal":
        # Mostrar el menú y guardar la opción elegida
        opcion = menu_principal(pantalla, fuente)        
        if opcion == "1":
            estado = "jugando"
        elif opcion == "2":
            mostrar_puntajes_pygame(pantalla, fuente)
            estado = "menu_principal"
        elif opcion == "3":
            jugando = False         
    elif estado == "jugando":
        #Primero selecciono el personaje y luego ejecuto la función jugar, que contiene toda la lógica del juego 
        personaje_elegido = seleccionar_personaje(pantalla, fuente, imagenes)
        resultado = jugar(pantalla, tablero, posicion_jugador, fuente, imagenes, sonidos, personaje_elegido)
        
        if resultado == "ganaste" or resultado == "abandono" or resultado == "perdiste":
            estado = "menu_despues_juego"
    elif estado == "menu_despues_juego":
        siguiente_opcion = menu_despues_de_juego(pantalla, fuente)

        if siguiente_opcion == "1":
            estado = "jugando"
        elif siguiente_opcion == "2":
            mostrar_puntajes_pygame(pantalla, fuente)
            estado = "menu_despues_juego" 
        elif siguiente_opcion == "3":
            jugando = False 
  
pygame.quit()
exit()  