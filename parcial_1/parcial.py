entrada = [10,20,30,40]
valor = 24 

def calcular_promedio(lista, valor):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    promedio = suma / len(lista)

    if promedio > valor:
        #print(True)
        return True
    else:
        #print(False)
        return False
    

resultado = calcular_promedio(entrada,valor)
print(resultado)

#Código corregido y comentado:

# Parámetros reales: lista de números y un valor de comparación
entrada = [10, 20, 30, 40]  # lista de números (parametro real)
valor = 24                  # valor contra el que se compara el promedio (parametro real)

def calcular_promedio(lista, valor):
    """
    Calcula el promedio de los elementos de una lista y lo compara con un valor dado.

    Parámetros:
    lista (list): Lista de números (parámetro formal).
    valor (int o float): Valor con el que se compara el promedio (parámetro formal).

    Retorna:
    bool: True si el promedio es mayor al valor, False en caso contrario.
    """
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    promedio = suma / len(lista)

    if promedio > valor:
        return True
    else:
        return False

# Invocación de la función con los parámetros reales
resultado = calcular_promedio(entrada, valor)
print(resultado)  # Muestra el resultado en pantalla


# 🔹 ¿Qué significa "no comenta parámetros reales"?
# Cuando llamás a la función, usás valores como [10, 20, 30, 40] y 24. Esos son los parámetros reales. El comentario debe explicar qué representan.

# Ejemplo:
# Parámetros reales: lista de números y un valor de comparación
# entrada = [10, 20, 30, 40]  # Parámetro real: lista de números
# valor = 24                  # Parámetro real: valor con el que se compara el promedio

# 🔹 ¿Qué significa "no comenta parámetros formales"?
# Cuando definís la función, escribís cosas como def calcular_promedio(lista, valor):. Ahí lista y valor son los parámetros formales. Se recomienda poner un comentario (o usar docstring) para explicar qué recibe la función.

# Ejemplo 

# def calcular_promedio(lista, valor):
#     """
#     Parámetros formales:
#     lista: una lista de números.
#     valor: un número para comparar con el promedio.
#     """

# 🔹 ¿Qué significa "no comenta invocación"?
# Cuando hacés esto:

# calcular_promedio(entrada, valor)
# Estás invocando la función. El comentario tiene que explicar qué hace esa llamada.

# Ejemplo:

# # Invocación: se calcula si el promedio de 'entrada' es mayor que 'valor'
# calcular_promedio(entrada, valor)

# 🔹 ¿Qué significa "no documenta función"?
# Quiere decir que no explicaste qué hace la función. Para eso usamos un docstring, que es un texto entre triple comillas justo debajo de def.

# Ejemplo:

# def calcular_promedio(lista, valor):
#     """
#     Calcula el promedio de una lista y lo compara con un valor.

#     Retorna True si el promedio es mayor que el valor, False si no.
#     """

#ejercicio terminado corecto con un solo return
# def calcular_promedio(lista, valor):
#     suma = 0
#     for i in range(len(lista)):
#         suma += lista[i]
    
#     promedio = suma / len(lista)

#     if promedio > valor:
#         resultado = True
#     else:
#         resultado = False

#     return resultado

# Llamada a la función con parámetros reales
entrada = [10, 20, 30, 40]  # Lista de números (parámetro real)
valor = 24                  # Valor con el que se compara el promedio (parámetro real)

def calcular_promedio(lista, valor):
    """
    Calcula el promedio de los valores en una lista y devuelve True
    si el promedio es mayor que el valor dado, o False en caso contrario.

    Parámetros:
    lista (list): Lista de números a promediar.
    valor (float): Valor con el que se compara el promedio.

    Retorna:
    bool: True si el promedio es mayor que 'valor', False si no lo es.
    """
    suma = 0  # Inicializa la suma
    for i in range(len(lista)):  # Recorre la lista (parámetro formal: 'lista')
        suma += lista[i]
    
    promedio = suma / len(lista)  # Calcula el promedio

    if promedio > valor:
        resultado = True
    else:
        resultado = False

    return resultado  # Retorna True o False según el resultado

# Invocación de la función
resultado_final = calcular_promedio(entrada, valor)
print("¿El promedio es mayor que", valor, "?:", resultado_final)