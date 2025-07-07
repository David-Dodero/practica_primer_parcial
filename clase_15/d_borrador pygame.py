import pygame

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (0, 150, 255)
VERDE_CLARO = (0, 255, 155)
VIOLETA_VACIO = (50, 17, 86)
pygame.init() #prende pygame

pantalla = pygame.display.set_mode(((800, 600)),pygame.RESIZABLE)
pygame.display.set_caption("probando que onda")
fuente = pygame.font.SysFont("Arial Narrow", 50)
nombre = ""
escribiendo_nombre = True
while escribiendo_nombre:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and nombre != "":
                escribiendo_nombre = False  # Listo, terminamos de escribir
            elif event.key == pygame.K_BACKSPACE:
                nombre = nombre[:-1]  # Borra una letra
            else:
                nombre += event.unicode  # Agrega letra nueva

    pantalla.fill(VIOLETA_VACIO)

    # Mostrar instrucciones
    titulo = fuente.render("Ingresá tu nombre y presioná:", True, BLANCO)
    pantalla.blit(titulo, (100, 150))

    # Cuadro de texto
    pygame.draw.rect(pantalla, BLANCO, (100, 200, 600, 50),5)

    # Mostrar lo que el jugador va escribiendo
    entrada = fuente.render(nombre, True, BLANCO)
    pantalla.blit(entrada, (110, 210))

    pygame.display.update()

bandera = True
while bandera:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False

    texto = fuente.render("Dodero David", True, (NEGRO))

    pantalla.fill(AZUL_CLARO)
    pantalla.blit(texto, (50, 50))

    pygame.display.update()


pygame.quit()



#nombre = ""
#escribiendo_nombre = True

# Bucle para ingresar el nombre
# while escribiendo_nombre:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN and nombre != "":
#                 escribiendo_nombre = False  # Listo, terminamos de escribir
#             elif event.key == pygame.K_BACKSPACE:
#                 nombre = nombre[:-1]  # Borra una letra
#             else:
#                 nombre += event.unicode  # Agrega letra nueva

#     pantalla.fill(VIOLETA_VACIO)

#     # Mostrar instrucciones
#     titulo = fuente.render("Ingresá tu nombre y presioná ENTER:", True, BLANCO)
#     pantalla.blit(titulo, (100, 150))

#     # Cuadro de texto
#     pygame.draw.rect(pantalla, BLANCO, (100, 200, 600, 50), 2)

#     # Mostrar lo que el jugador va escribiendo
#     entrada = fuente.render(nombre, True, BLANCO)
#     pantalla.blit(entrada, (110, 210))

#     pygame.display.update()