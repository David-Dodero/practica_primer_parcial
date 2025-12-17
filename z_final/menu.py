import pygame

# Colores y fuente
BLANCO = (255, 255, 255)
VIOLETA_VACIO = (50, 17, 86)

def menu_principal(pantalla, fuente):
    """
    Muestra un menú principal con tres opciones: Jugar, Ver puntajes o Salir.

    Parámetros:
        pantalla (pygame.Surface): Pantalla donde se dibuja el menú.
        fuente (pygame.font.Font): Fuente usada para renderizar el texto. # Fuente = tipo de letra para mostrar texto en pantalla

    Retorna:
        str: La opción seleccionada por el usuario ("1", "2" o "3").        
    """
    # Cargar y reproducir música de intro
    pygame.mixer.music.pause()  # Pausa la música de fondo
    sonido_intro = pygame.mixer.Sound("z_final/sonidos/cinematic-intro.mp3")
    sonido_intro.play(-1)  # (-1) = loop infinito mientras estes en el menu

    seleccion = ""  #Guarda la opción elegida por el jugador  

    while seleccion == "":
        for event in pygame.event.get():  # Revisa todos los eventos (teclado, cerrar ventana, etc.)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit() # Sale del juego si se cierra la ventana
            if event.type == pygame.KEYDOWN:  # Si el jugador presiona una tecla válida
                if event.key == pygame.K_1:
                    seleccion = "1"
                elif event.key == pygame.K_2:
                    seleccion = "2"
                elif event.key == pygame.K_3:
                    seleccion = "3"

        pantalla.fill(VIOLETA_VACIO)
        titulo = fuente.render("MENU PRINCIPAL", True, BLANCO)   # Crear textos con la fuente
        op1 = fuente.render("1. Jugar", True, BLANCO)
        op2 = fuente.render("2. Ver puntajes", True, BLANCO)
        op3 = fuente.render("3. Salir", True, BLANCO)

        pantalla.blit(titulo, (200, 100))   # Dibujar textos en la pantalla
        pantalla.blit(op1, (250, 200))
        pantalla.blit(op2, (250, 260))
        pantalla.blit(op3, (250, 320))

        pygame.display.update()   # Actualiza la pantalla con los cambios
    sonido_intro.stop()  #para la musica al salir del menú
    pygame.mixer.music.unpause()  # Reanuda música de fondo
    return seleccion

def menu_despues_de_juego(pantalla, fuente):
    """
    Muestra un menu con opciones despues de jugar una partida

    Parametros:
        pantalla (pygame.Surface): Pantalla donde se dibuja el menu
        fuente (pygame.font.Font): Fuente usada para renderizar el texto.

    Retorna:
        str: La opción seleccionada por el usuario ("1", "2" o "3").
    """
    pygame.mixer.music.pause()  # Pausa la música de fondo
    sonido_intro = pygame.mixer.Sound("z_final/sonidos/cinematic-intro.mp3")
    sonido_intro.play()

    seleccion = ""

    while seleccion == "":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    seleccion = "1"  # Jugar con otro jugador
                elif event.key == pygame.K_2:
                    seleccion = "2"  # Ver puntajes
                elif event.key == pygame.K_3:
                    seleccion = "3"  # Salir

        pantalla.fill(VIOLETA_VACIO)
        titulo = fuente.render("Que deseas hacer ahora?", True, BLANCO)
        op1 = fuente.render("1. Jugar con otro jugador", True, BLANCO)
        op2 = fuente.render("2. Ver puntajes", True, BLANCO)
        op3 = fuente.render("3. Salir", True, BLANCO)

        pantalla.blit(titulo, (150, 100))
        pantalla.blit(op1, (200, 200))
        pantalla.blit(op2, (200, 260))
        pantalla.blit(op3, (200, 320))

        pygame.display.update()
    sonido_intro.stop()  #para la musica al salir del menú
    pygame.mixer.music.unpause()  # Reanuda música de fondo
    return seleccion