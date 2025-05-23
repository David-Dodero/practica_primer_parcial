# Crear un programa en Python que:
# Construya una matriz de 4 filas x 4 columnas con números fijos (predefinida).
# Utilice una función que recorra las columnas de la matriz y verifique si existe un número repetido 3 veces de manera vertical 
# (una debajo de otra).
# Si lo encuentra, la función debe retornar ese número.
# Si no existe, debe retornar None.
# MATRIZ FIJA
matriz = [
    [5, 2, 3, 4],
    [5, 2, 7, 8],
    [2, 2, 3, 1],
    [1, 6, 7, 4]
]

def recorrer_vertical(matriz):
    for col in range(4):  # recorro columnas una por una
        print(f"Columna {col}:")
        for fila in range(4):  # recorro cada fila dentro de esa columna
            print(matriz[fila][col])
        print(" ")
recorrer_vertical(matriz)




