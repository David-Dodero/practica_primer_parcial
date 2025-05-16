#David Dodero

# Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos):
# Realizar el juego "Radar del Tesoro"
# Dado el siguiente mapa de 5x5 donde se encuentra oculto un único tesoro, marcado con un 1:
# mapa = [
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0] ]
# Pedir al usuario una coordenada fila (x) entre 0 y 4 (inclusive).
# Pedir al usuario una coordenada columna (y) entre 0 y 4 (inclusive).
# Desarrollar una función con el siguiente prototipo:
#  verificar_tesoro(mapa: list, x: int, y: int) -> int
# La función debe retornar:
#  - 0 si el usuario encontró el tesoro.
#  - En caso contrario, retornar la distancia Manhattan entre la coordenada ingresada y la ubicación real del
# tesoro.
# **Distancia Manhattan**:
# distancia = |x_usuario - x_tesoro| + |y_usuario - y_tesoro|
# Según el valor retornado, mostrar al usuario:
#  - "¡Encontraste el tesoro!" si retorna 0.
#  - "Fallaste. El tesoro está a X casilleros de distancia." si retorna otro número.
# El juego continúa hasta que el usuario encuentre el tesoro o hasta que el usuario lo desee.



mapa = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0] ]

def verificar_tesoro(mapa: list, x: int, y: int) -> int:
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] == 1:
                x_tesoro = i
                y_tesoro = j
    
    if fila > x_tesoro :
        distancia_x = fila - x_tesoro
    else:
        distancia_x = x_tesoro - fila
    
    if columna > y_tesoro:
        distancia_y = columna - y_tesoro
    else:
        distancia_y = y_tesoro - columna

    distancia = distancia_x + distancia_y

    if distancia == 0: 
        print("encontraste el tesoro")
    else:
        print(f"fallaste el tesoro esta a {distancia} de distacia ")


seguir = "s"
while seguir == "s":
    fila = int(input("ingrese una cordenada para la fila entre el 0 y el 4: "))
    while fila < -1 or fila > 5:
        fila = int(input("error, ingrese una cordenada para la fila entre el 0 y el 4: "))

    columna = int(input("ingrese una cordenada para la columna: "))
    while columna < -1 or columna >5:
        columna = int(input("error, ingrese una cordenada para la columna entre el 0 y el 4: "))
    
    verificar_tesoro(mapa,fila,columna)

    seguir = input("quiere seguir buscando el tesoro? s/n ")

    
    


