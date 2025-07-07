import pygame
import random
from preguntas import *

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 50, 50)
AZUL_VACIO = (100, 150, 255) 
VIOLETA_VACIO = (50, 17, 86)
VERDE = (50, 255, 50)
GRIS = (150,150, 150)
AMARILLO = (250, 250, 100)

# Inicialización
pygame.init()
pantalla = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Juego de preguntas")
fuente = pygame.font.SysFont("Arial Narrow", 28)

# Variables de juego
COLUMNAS = 10
ANCHO_CASILLA = 60
ALTO_CASILLA = 60
posicion_jugador = 14

# Tablero lógico
tablero = [
    0, 1, 0, 0, 0, 3, 0, 0, 0, 0,
    0, 1, 0, 0, 2, 1, 1, 0, 0, 0,
    1, 0, 2, 0, 0, 0, 1, 0, 0, 0
]

# Funciones: jugar, dibujar_tablero, guardar_puntaje, mostrar_puntajes_pygame, mostrar_mensaje
# (Ya las tenés, solo hay que asegurarse que estén ordenadas arriba del bucle principal)

# Preguntar si quiere jugar
esperando_respuesta = True
jugar_confirmado = False
while esperando_respuesta:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                jugar_confirmado = True
                esperando_respuesta = False
            elif event.key == pygame.K_n:
                jugar_confirmado = False
                esperando_respuesta = False

    pantalla.fill(VIOLETA_VACIO)
    texto = fuente.render("¿Querés jugar? (s/n)", True, BLANCO)
    pantalla.blit(texto, (200, 250))
    pygame.display.update()

# Si no quiere jugar, salir
if not jugar_confirmado:
    pantalla.fill(VIOLETA_VACIO)
    mensaje = fuente.render("Fin del juego", True, BLANCO)
    pantalla.blit(mensaje, (250, 250))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    exit()

# Jugar
jugar_otra_vez = True
while jugar_otra_vez:
    jugar(pantalla, tablero, posicion_jugador)

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