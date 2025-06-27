# def nombre_jugador():
#     nombre = input("ingrese su nombre: ")
#     return nombre

def hacer_pregunta(pregunta_dict : dict):
    """
    muestra una pregunta con tres opciones de respuesta, solicita al usuario una respuesta
    y evalua si es correcta o no

    Parametro:
    pregunta_dict : dict

    retorna:    
    int
        1 si la respuesta del usuario es correcta, 0 si es incorrecta.
    """
    print(pregunta_dict["pregunta"])
    print(f"a) {pregunta_dict['respuesta_a']}")
    print(f"b) {pregunta_dict['respuesta_b']}")
    print(f"c) {pregunta_dict['respuesta_c']}")

    respuesta = input("Tu respuesta (a/b/c): ").lower()

    if respuesta == pregunta_dict["respuesta_correcta"]:
        print("correcto")
        resultado = 1
    else:
        print("incorrecto.")
        resultado = 0
    
    return resultado


def mover_jugador(posicion: int, resultado: int):
    """
    mueve al jugador en el tablero segun el resultado de una pregunta

    parametros:
    posicion : int
        La posición actual del jugador en el tablero (índice del casillero)

    resultado : int
        El resultado de la pregunta:
        1 si la respuesta fue correcta (avanza)
        0 si la respuesta fue incorrecta (retrocede)

    retorna:
    int
        La nueva posición del jugador después del movimiento
    """
    if resultado == 1:
        posicion += 1  # Respuesta correcta: avanza
        print(f"avanzas al casillero {posicion + 1}")
    else:
        posicion -= 1  # Respuesta incorrecta: retrocede
        print(f"retrocedes al casillero {posicion + 1}")
    return posicion

def serpiente_escalera(posicion: int, resultado: int, tablero: list):
    """
    Ajusta la posición del jugador según casillas especiales (escaleras o serpientes)

    Parametros:
    posicion : int
        La posición actual del jugador en el tablero

    resultado : int
        Resultado de la pregunta:
        1 si la respuesta fue correcta
        0 si la respuesta fue incorrecta

    tablero : list[int]
        Lista que representa el tablero
        Cada posición puede tener:
        0 si no hay nada especial
        Un número positivo que indica cuánto avanzar o retroceder adicionalmente

    Retorna:
    int
        La nueva posición del jugador luego de aplicar serpientes o escaleras
    """
    if posicion >= 0 and posicion < len(tablero): #me asegura de que la posición del jugador este dentro de los limites validos del tablero
        movimiento_extra = tablero[posicion]
        if movimiento_extra > 0:
            if resultado == 1:
                posicion += movimiento_extra  # si respondió bien, sube por la escalera
            else:
                posicion -= movimiento_extra  # si respondió mal, baja por la serpiente
    
    return posicion

def verificar_estado(posicion: int, tablero: list, nombre: str) -> bool:
    """
    Verifica si el jugador gano, perdio o desea abandonar el juego

    Parámetros:
    posicion : int
        Posición actual del jugador en el tablero (índice)

    tablero : list
        Lista que representa el tablero. Su longitud determina el último casillero

    nombre : str
        Nombre del jugador, usado para personalizar los mensajes 

    Retorna:
    -------
    bool
        True si el juego debe continuar, False si el jugador perdió, ganó o decidió salir.
    """
    respuesta = True

    if posicion <= 0:
        print(f"perdiste, {nombre} llegaste al casillero perdedor")
        respuesta = False
    elif posicion >= len(tablero) - 1: #si posición llega al índice 29 (último), equivale al casillero 30 ganaste
        print(f"felicidades, {nombre} llegaste al casillero ganador")
        respuesta = False
    else:
        seguir = input("Queres seguir jugando? s/n: ").lower()
        while seguir != "s" and seguir != "n":
            seguir = input("Error. Querés seguir jugando? (s/n): ").lower()

        if seguir == "n":
            print(f"{nombre} estás en el casillero {posicion + 1}")
            print("Fin del juego.")
            
            respuesta = False

    return respuesta


def mostrar_puntajes():
    """
    Lee y muestra en pantalla los puntajes almacenados en el archivo 'Score.csv'.

    Esta función abre el archivo en modo lectura ('r') y muestra cada línea,
    que representa un puntaje registrado previamente. Luego cierra el archivo

    Retorna:
        No retorna ningun valor
    """
    archivo = open("Score.csv", "r")
    for puntajes in archivo:
        print(puntajes)
    archivo.close()