def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any)-> list:
    matriz2 = []
    for i in range(cantidad_filas):
        fila = [valor_inicial] * cantidad_columnas

        matriz2 += [fila]
    return matriz2
mi_matriz = inicializar_matriz(2,4,0)

def cargar_matriz_secuencialmente(matriz:list):
    # agregar las validasiones/retornos que sean necesarias
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = int(input(f"fila{i} columns {j}: "))
cargar_matriz_secuencialmente(mi_matriz)