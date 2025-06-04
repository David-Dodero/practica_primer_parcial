# (Calificación) Para alcanzar la nota de Aprobación Directa el programa debe estar funcionando correctamente y
# no debe dar error en ningún momento.
# Los principales temas a evaluar son: Array Bidimensionales(matrices) – Listas Paralelas - Ordenamientos
# Objetivos de Aprobación Directa (Calificación de 6 a 10 puntos):
# Título: Gestión de Ventas de Productos con Lista/Array y Matriz en Python
# Descripción: Se dispone de una lista/array de 3 productos: A, B y C, y una matriz que contiene las ventas
# trimestrales de cada producto (en miles de dólares).
# Cada fila de la matriz representa a un producto, y cada columna representa un trimestre (T1, T2, T3).
# Desarrolla un programa en Python que permita al usuario:
# Mostrar la lista de productos y la matriz de ventas.
# Ordenar los productos de mayor a menor según sus ventas totales anuales (suma de los trimestres).
# Buscar un producto por nombre y mostrar sus ventas.
# Buscar un valor de venta dentro de la matriz y mostrar a qué producto y trimestre pertenece.
# El programa debe funcionar de manera paralela, es decir, la lista de productos y la matriz deben mantenerse
# sincronizadas en todo momento.
# Nota: Pueden utilizarse funciones propias.
# Todo debe estar claramente comentado/documentado.

#datos iniciales  
producto = ["A","B","C"] #lista con nombres de productos 
ventas = [               #matriz con las ventas trimestrales por producto
        [50, 60, 70], #A
        [80, 55, 45], #B
        [40, 65, 75]  #C
           ] 
# ventas = [
#         [5, 60, 70], #A
#         [8, 60, 45], #B
#         [4, 65, 60]  #C
#           ] 





def menu_opciones():
    '''muestra el menu de opciones y ejecuta la opción seleccionada por el usuario. '''
    seleccionar = 0
    while seleccionar != 5: 
        print(" MENU DE OPCIONES ") 
        print("1 mostrar productos y ventas")
        print("2 ordenar productos por ventas anuales(desc)")
        print("3 buscar producto por nombre")
        print("4 buscar monto de venta en la matriz")
        print("5 salir")

        seleccionar = int(input("ingrese un numero del 1 a 5: "))
        while seleccionar < 1 or seleccionar > 5:
            seleccionar = int(input("error, ingrese un numero del 1 a 5: "))
    
        match seleccionar:
            case 1:
                mostrar_productos_ventas() #muestra los productos y ventas.
            case 2:
                ordenar_productos_por_ventas_anuales() #ordena los productos de manera desendente por ventas anuales.
            case 3:
                buscar_producto_por_nombre() #busca los productos por nombre 
            case 4:
                buscar_monto_de_venta_en_matriz() #busca un monto en la matriz 
            case 5:
                salir() #salis del programa


def mostrar_productos_ventas():
    '''''muestra los productos y sus ventas trimestrales.'''
    for i in range(len(producto)):
        print(f"producto: {producto[i]}, ", end= " " )
        for j in range(len(ventas[i])):
            print(ventas[i][j], end= " ")
        print(" ")


def ordenar_productos_por_ventas_anuales():
    '''ordena según el total anual de ventas (de mayor a menor).'''
    totales = [0] * len(ventas)
    
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            totales[i] += ventas[i][j]


    for i in range(len(totales)-1):
        for j in range(i+1, len(totales)):
            if totales[i] < totales[j]:
                aux = totales[i]
                totales[i] = totales[j]
                totales[j] = aux

                aux = producto[i]
                producto[i] = producto[j]
                producto[j] = aux

                aux = ventas[i]
                ventas[i] = ventas[j]
                ventas[j] = aux

def buscar_producto_por_nombre():
    '''busca un producto por su nombre y ve sus ventas.'''
    buscar_producto = input("ingrese el nombre del producto que desea buscar ")

    encontrado = False
    for i in range(len(producto)):
        if producto[i] == buscar_producto:
            encontrado = True
            posicion = i

    if encontrado == True:
        print(f"el producto buscado es: {producto[posicion]}, sus ventas son {ventas[posicion]} ")
            
    else:
        print(f"el producto: {buscar_producto}, no fue encontrado")


def buscar_monto_de_venta_en_matriz():
    '''busca un monto dentro de la matriz de ventas y muestra a qué producto y trimestre pertenece.'''
    monto_buscado =  int(input("ingrese el monto que desea buscar: "))
    encontrado = False
    for i in range(len(ventas)):
        for j in range(len(ventas[i])):
            if ventas[i][j] == monto_buscado:
                print(f"el producto es: {producto[i]} y el trimestre es {j + 1}")
                encontrado = True
               
    if encontrado == False:       
        print(f"el monto: {monto_buscado}, no se encontro")


def salir():
    '''sale del programa.''' 
    print("Saliste del menu de opciones")

#invocacion del menu principal
menu_opciones()