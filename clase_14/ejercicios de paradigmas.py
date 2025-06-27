# PARADIGMA FUNCIONAL
# Ejercicio 1: Se tiene una lista de diccionarios, donde cada diccionario representa un
# producto con nombre, precio y categoría. Escribe una función procesar_productos
# que reciba esta lista y una función de operación. Luego, crear distintas funciones
# para:
#  Filtrar productos de una categoría dada.
#  Calcular el precio promedio de todos los productos.
productos = [
 {"nombre": "Laptop", "precio": 1200, "categoria": "tecnología"},
 {"nombre": "Silla", "precio": 150, "categoria": "hogar"},
 {"nombre": "Smartphone", "precio": 800, "categoria": "tecnología"},
 {"nombre": "Mesa", "precio": 300, "categoria": "hogar"},
 {"nombre": "Auriculares", "precio": 200, "categoria": "tecnología"}
]


def procesar_productos(lista: list, funcion: callable):
    return funcion(lista)

def filtrar_por_categoria(lista, categoria):
    filtrados = []
    for producto in lista:
        if producto["categoria"] == categoria:
            filtrados.append(producto)
    return filtrados

# producto_tecnologia = filtrar_por_categoria(productos,"tecnología")
# print(f"los productos de tecnologia son {producto_tecnologia}")

# producto_hogar = filtrar_por_categoria(productos,"hogar")
# print(f"los productos del hogar son {producto_hogar}")

resultado_tec = procesar_productos(productos, lambda lista: filtrar_por_categoria(lista, "tecnología"))
print(f"los productos de tecnologia son: {resultado_tec} ")

def solo_hogar(lista):
    return filtrar_por_categoria(lista, "hogar")

resultado_hogar = procesar_productos(productos, solo_hogar)
print("productos del hogar:", resultado_hogar)