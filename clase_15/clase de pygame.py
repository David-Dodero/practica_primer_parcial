import pygame 

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
AZUL_CLARO = (0, 150, 255)
VERDE_CLARO = (0, 255, 155)
VIOLETA_VACIO = (50, 17, 86)
verde = (0, 100, 0) #verde en realidad es 0,255,0

pygame.init() #prende pygame
pantalla = pygame.display.set_mode(((800, 600)), pygame.RESIZABLE) #RESIZABLE Crea una ventana que podés agrandar o achicar con el mouse.
pygame.display.set_caption("juego de preguntas")
rectangulo = pygame.Rect((30, 30), (270,60))

while True:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT:
            pygame.quit() #aca se cierra pygame
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("Se presiono la tecla a")

        font = pygame.font.SysFont("Arial Narrow", 50) #"Arial Narrow" Es el nombre de una fuente (tipografía)
        text = font.render("HOLA MUNDO", True, (NEGRO))
        #pantalla.blit(text,(50,50))
        #rectangulo = pygame.Rect((30, 30), (60,60))
        #pygame.draw.rect(pantalla, (255, 255, 0), rectangulo)

    pantalla.fill ((VIOLETA_VACIO))
        
    pygame.draw.rect(pantalla, (255, 255, 0), rectangulo)
    pantalla.blit(text,(50,50))
    pygame.display.update()