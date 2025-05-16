# #matrices

matrix=[["ana",23],
        ["juan",45],
        ["sol",65],
        ["luis",22]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ") #El end=" " evita el salto de línea después de cada número.
        #print("fila:", i,"columna",j,"dato:", matrix[i][j] )
    print(" ") #Después de imprimir todos los elementos de una fila, esta línea hace el salto de línea para pasar a la siguiente fila.    

matriz = [[1,2,3,4,5],
          [6,7,8,9,0]]

matriz[1][0] = 15 #cambia el 6 de la matriz por el 15 

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ") 
    print(" ")



def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any)-> list:
    matriz2 = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz2 += [fila]
    return matriz2
#mi_matriz = inicializar_matriz(2,4,0)


# for i in range(len(mi_matriz)):
#     for j in range(len(mi_matriz[i])):
#         print(mi_matriz[i][j], end=" ")
#     print(" ")


def cargar_matriz_secuencialmente(matriz:list):
    # agregar las validasiones/retornos que sean necesarias
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"fila{i} columns {j}: "))
#cargar_matriz_secuencialmente(mi_matriz)

# seguir =  "s"
# while seguir == "s":
#     fila= int(input("indice de fila: "))
#     columna = int(input("indice de columna: "))
#     dato = int(input("ingrese el numero de carga: "))
#     mi_matriz[fila][columna] = dato
#     seguir = input("desea seguir cargando? s/n: ")

# for i in range(len(mi_matriz)):
#     for j in range(len(mi_matriz[i])):
#         print(mi_matriz[i][j], end=" ")
#     print(" ")
# #cargar_matriz_secuencialmente(mi_matriz)


mi_matriz2 = [[1,2,3,4,5], 
              [6,7,8,9,0]]

def buscar_valor_entero(matriz:list, valor:int):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"se encontro el numero: {valor} en la fila {i} columna {j}")
buscar_valor_entero(mi_matriz2, 5)