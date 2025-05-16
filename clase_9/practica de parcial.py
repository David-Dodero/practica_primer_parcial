tablero = [[0,0,1,0,0],
           [0,1,0,1,0],
           [1,0,0,1,0],
           [0,0,1,0,1],
           [0,0,0,0,1]]


def verificar_cordena(tablero:list, x:int, y:int)-> bool:
    hay_barco = False
    if tablero[x][y]==1:
        hay_barco = True
    return hay_barco

seguir = "s"
cont_hundidos = 0
while seguir == "s":
    fila_x= int(input("ingrese un numero para la posicion x "))
    while fila_x < 0 or fila_x > 4:
        fila_x= int(input(" erro, ingrese un numero para la posicion x "))
    fila_y= int(input("ingrese un numero para la posicion y "))
    while fila_y < 0 or fila_y > 4:
        fila_y= int(input("error, ingrese un numero para la posicion y "))

    resultado = verificar_cordena(tablero,fila_x, fila_y)

    if resultado == True:
        print("hundido")
        cont_hundidos += 1
    else:
         print("agua")
    seguir = input("desea seguir 's' para si 'n' para no: ")
print("la cantidad de barcos hundidos", cont_hundidos)
#porque un retur por funcion no entiendo 