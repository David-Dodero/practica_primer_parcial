# LISTAS ANIDADAS
# Ejercicio 1: El almacén de barrio nos pide un programa para almacenar, ordenar y
# controlar stock de su mercadería por día.
# Comienza el día con la siguiente disposición en su góndola:
# Cada celda (fila/columna) muestra la ubicación de cada producto, ejemplo: en (1,2)
# se guardan las botellas, etc.
# Armar la lista de Productos con nombre, cantidad y ubicación (fila, columna)

matriz = [
        [[" ",0],["botellas",3],[" ",0],["frascos",4],[" ",0]],
        [[" ",0],[" ",0],["fideos",4],[" ",0],[" ",0],],
        [[" ",0],[" ",0],[" ",0],["leches",6],[" ",0]]
        ]


# Ejercicio 2-Armar el siguiente menú de opciones:
# 1-Alta de productos (producto nuevo)
# 2-Baja de productos (producto existente)
# 3-Modificar productos (cantidad, ubicación)
# 4-Listar productos
# 5-Lista de productos ordenado por nombre
# 6-Salir


def menu_opciones():
    seleccionar = 0
    while seleccionar != 6:
        print("MENU DE OPCIONES")
        print("1-Alta de productos (producto nuevo)")
        print("2-Baja de productos (producto existente)")
        print("3-Modificar productos (cantidad, ubicación)")
        print("4-Listar productos")
        print("5-Lista de productos ordenado por nombre")
        print("6-Salir")

        seleccionar = int(input("ingrese un numero del 1 a 6: "))
        while seleccionar < 1 or seleccionar > 6:
            seleccionar = int(input("ingrese un numero del 1 a 6: "))
    
        match seleccionar:
            case 1:
                agregar_producto()
            case 2:
                sacar_producto()
            case 3:
                modificar_producto()
            case 4:
                lista_productos()
            case 5:
                lista_ordenada_por_nombre()
            case 6:
                salir()






def agregar_producto():
    seguir = "s"

    while seguir == "s":
        producto = input("ingrese el nombre del producto: ")
        cantidad =  int(input("ingrese cantidad de productos que desea agregar: "))
        fila = int(input("ingrese la fila donde desea agregar el productos : "))
        columna = int(input("ingrese la columna donde desea agregar el productos : "))
   
        if matriz[fila][columna] == [" ", 0]:
            matriz[fila][columna] = [producto, cantidad]
            print(f"se agrego el producto {producto} con la cantidad {cantidad},  en la fila y columna {fila} {columna} ")
        else:
            print("ya hay un producto en esa celda: ")

        seguir = input("desea seguir agregando productos? s/n ")







def sacar_producto():
    
    seguir = "s"
    while seguir == "s":
        producto_eliminar = input("ingrese el nombre del producto que desea quitar: ")

        encontre = False
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j][0] == producto_eliminar: 
                    matriz[i][j] = [" ", 0]
                    print(f"se quito el producto:  {producto_eliminar}")
                    encontre = True
        if encontre == False:
            print("no esta ese producto", producto_eliminar )

        seguir = input("desea seguir quitando productos? s/n ")








def modificar_producto():
    seguir = 's'
    while seguir == 's':
        producto_modificar =  input("producto que decea modificar: ")

        mod_encontrado = False
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j][0] == producto_modificar:
                    nueva_ubicacion_fila = int(input("ingrese la nueva ubicacion fila: ")) 
                    nueva_ubicacion_columna = int(input("ingrese la nueva ubicacion columna: "))
                    if matriz[nueva_ubicacion_fila][nueva_ubicacion_columna] == [" ",0]:                        
                        nuevo_cantidad =  int(input("ingrese la cantidad: "))
                        matriz[nueva_ubicacion_fila][nueva_ubicacion_columna] = [producto_modificar, nuevo_cantidad] 
                        matriz[i][j] = [" ", 0]
                        print(f"el producto {producto_modificar} fue modificado correctamente")
                        mod_encontrado = True
                    else:
                        print("el lugar esta ocupado")    
        if mod_encontrado == False:
            print("no se encontro el producto") 

        seguir = input("desea seguir modificando? s/n")




def lista_productos():
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= " ")
        print("")

def lista_ordenada_por_nombre():
    lista_nueva = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != [" ",0]:
                lista_nueva += [matriz[i][j]]

    for i in range(len(lista_nueva)-1):
        for j in range(1+i, len(lista_nueva)):
            if lista_nueva [i][0] > lista_nueva[j][0]:
                aux = lista_nueva[i]
                lista_nueva[i] = lista_nueva[j]
                lista_nueva[j] = aux
    
    for producto in lista_nueva:
        print(f"producto: {producto[0]}, cantidad: {producto[1]}")




            
def salir():
    print("Saliste del menu de opciones")


menu_opciones()