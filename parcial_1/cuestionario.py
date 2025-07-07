# 1. que imprime el siguiente codigo?
def func(lista):               # Define una función llamada 'func' que recibe una lista como parámetro
    suma = 0                   # Inicializa una variable 'suma' en 0 para acumular los números pares
    for num in lista:         # Recorre cada elemento (num) dentro de la lista
        if num % 2 == 0:      # Verifica si el número es par (el resto de dividirlo por 2 es 0)
            suma += num       # Si es par, lo suma a la variable 'suma'
    return suma               # Al finalizar el bucle, devuelve el total acumulado de los pares

print(func([1, 2, 3, 4, 5]))   # Llama a la función con la lista [1, 2, 3, 4, 5]
# Los pares son 2 y 4 → 2 + 4 = 6 → imprime 6

# NOTA:
# En Python se puede recorrer una lista directamente sin usar 'range'.
# Ejemplo más simple y recomendado:

# lista = [10, 20, 30]
# for num in lista:         # Recorre directamente cada elemento
#     print(num)

# Esto es equivalente a usar 'range', pero más claro y corto:

# for i in range(len(lista)):
#     print(lista[i])       # Accede a cada elemento usando el índice

# Usá 'for elemento in lista' cuando NO necesitás el índice.
# Usá 'for i in range(len(lista))' cuando SÍ necesitás saber la posición (índice).

# 2. cual es el resultado de ejecutar este fragmento?

def verifica(lista):                    # Define una función llamada 'verifica' que recibe una lista como parámetro
    for x in lista:                     # Recorre cada elemento 'x' en la lista
        if x < 0:                       # Verifica si el número es negativo
            return "negativo encontrado"  # Si encuentra un número negativo, devuelve este mensaje y sale de la función
    return "todos positivos"           # Si termina el bucle sin encontrar negativos, devuelve este mensaje

print(verifica([5, 3, -2, 8]))          # Llama a la función con la lista [5, 3, -2, 8]
# Como -2 es negativo, se imprime: "negativo encontrado"

# 3. cuantas veces se imprime "hola" en el codigo?
i = 0                         # Se inicializa la variable 'i' en 0
while i < 5:                  # Mientras 'i' sea menor que 5, se repite el bucle
    print("hola")             # Se imprime "hola"
    i += 2                    # Se incrementa 'i' en 2 en cada vuelta

# Paso a paso:
# 1ª vuelta → i = 0 → imprime "hola" → i pasa a 2
# 2ª vuelta → i = 2 → imprime "hola" → i pasa a 4
# 3ª vuelta → i = 4 → imprime "hola" → i pasa a 6
# 4ª vuelta → i = 6 → ya no cumple la condición (6 < 5 es falso), termina el bucle

# Resultado: Se imprime "hola" 3 veces

# 4. que devuelve esta funcion?
def misterio(lista) -> list:             # Define una función llamada 'misterio' que recibe una lista y devuelve otra lista
    lista_misterio = []                  # Crea una lista vacía para guardar los resultados
    for x in lista:                      # Recorre cada elemento 'x' de la lista original
        if x > 3:                        # Verifica si 'x' es mayor que 3
            lista_misterio.append(x*2)  # Si cumple, multiplica 'x' por 2 y lo agrega a la nueva lista
    return lista_misterio                # Devuelve la nueva lista con los valores modificados

print(misterio([1, 2, 3, 4, 5]))         # Llama a la función con la lista [1, 2, 3, 4, 5]
# Solo 4 y 5 son mayores que 3 → se agregan 8 y 10 → imprime [8, 10]

# 5. que imprime el siguiente codigo?

def analizar(lista):                    # Define una función llamada 'analizar' que recibe una lista como parámetro
    primero = lista[0]                  # Guarda el primer elemento de la lista en la variable 'primero'
    for num in lista:                   # Recorre cada número 'num' en la lista
        if num > primero:               # Si el número actual es mayor que 'primero'...
            primero = num               # ...actualiza 'primero' con ese número
    return primero                      # Devuelve el mayor número encontrado en la lista

print(analizar([3, 9, 2, 5, 6]))        # Llama a la función con la lista [3, 9, 2, 5, 6]
                                        # Compara cada valor con el primero (3):
                                        # 9 > 3 → primero = 9
                                        # 2 < 9 → nada cambia
                                        # 5 < 9 → nada cambia
                                        # 6 < 9 → nada cambia
                                        # Resultado final: devuelve 9

# 6. ¿Qué valor toma el resultado?

def suma_indices(lista):                    # Define una función que recibe una lista
    suma = 0                                # Inicializa la variable 'suma' en 0
    for i in range(len(lista)):             # Recorre los índices de la lista (i = 0, 1, 2, 3, 4)
        if i % 2 == 0:                      # Si el índice es par (resto de dividir por 2 es 0)...
            suma += lista[i]                # ...suma el elemento en esa posición
    return suma                             # Devuelve la suma total de los elementos en índices pares

# Llamada a la función con la lista [10, 20, 30, 40, 50]
# Índices pares: 0, 2, 4 → valores: 10, 30, 50 → suma: 10 + 30 + 50 = 90

resultado = suma_indices([10, 20, 30, 40, 50])
print(resultado)                            # Imprime 90

# 7. ¿Qué hace el siguiente código?

def transforma(lista):                    # Define una función llamada 'transforma' que recibe una lista
    nueva = []                            # Crea una lista vacía llamada 'nueva'
    for num in lista:                     # Recorre cada número de la lista original
        if num % 2 != 0:                  # Si el número es impar (resto de dividir por 2 es distinto de 0)...
            nueva.append(num + 1)         # ...le suma 1 y lo agrega a la lista 'nueva'
    return nueva                          # Devuelve la lista 'nueva' con los números transformados

print(transforma([1, 2, 3, 4, 5]))         # Llama a la función con la lista [1, 2, 3, 4, 5]
                                          # Números impares: 1, 3, 5 → se transforman en 2, 4, 6
                                          # Resultado: [2, 4, 6]
                                        
# 8. ¿Qué salida produce este fragmento?

def contar(lista):                   # Define una función llamada 'contar' que recibe una lista
    contador = 0                     # Inicializa un contador en 0
    for num in lista:               # Recorre cada número de la lista
        if num == 0:                # Si el número es igual a 0...
            contador += 1          # ...aumenta el contador en 1
    return contador                 # Devuelve la cantidad de ceros encontrados

print(contar([0, 1, 0, 2, 0, 3]))   # Llama a la función con la lista [0, 1, 0, 2, 0, 3]
                                   # Hay tres ceros en la lista → contador = 3

# 9. ¿Qué tarea realiza el siguiente código?

a = 6                           # Se asigna el valor 6 a la variable 'a'
b = 1                           # Se asigna el valor 1 a la variable 'b'
c = 9                           # Se asigna el valor 9 a la variable 'c'

if a > b and a > c:             # Si 'a' es mayor que 'b' Y también mayor que 'c'...
    print("el mayor es a ")     # ...imprime que el mayor es 'a'
elif b > c:                     # Si no se cumplió lo anterior, verifica si 'b' es mayor que 'c'...
    print("el mayor es b ")     # ...si es así, imprime que el mayor es 'b'
else:                           # Si ninguna de las condiciones anteriores se cumplió...
    print("el mayor es c")      # ...entonces imprime que el mayor es 'c'

# En este caso:
# a = 6, b = 1, c = 9
# ¿a > b? → sí (6 > 1)
# ¿a > c? → no (6 < 9)
# Entonces no entra al primer if

# ¿b > c? → no (1 < 9)
# Entonces tampoco entra al elif

# Va al else → imprime "el mayor es c"


# 10. ¿Qué realiza el siguiente código?

def procesar(sublista: list):                     # Define una función que recibe una lista
    for i in range(len(sublista) - 1):            # Bucle externo: recorre cada índice menos el último
        for j in range(i + 1, len(sublista)):     # Bucle interno: compara con los elementos siguientes
            if sublista[i] < sublista[j]:         # Si el elemento en la posición i es menor al de la j...
                valor = sublista[i]               # Guarda temporalmente el valor en la posición i
                sublista[i] = sublista[j]         # Coloca el valor más grande en la posición i
                sublista[j] = valor               # Coloca el valor más chico en la posición j

# Es un algoritmo de ordenamiento por comparación (parecido a bubble sort)
# Ordena la lista de mayor a menor

lista = [5, 2, 9, 3, 7, 1, 8, 4, 6]               # Lista original
procesar(lista)                                   # Llama a la función para ordenar la lista

# Después de ejecutarse, la lista queda modificada y ordenada de mayor a menor:
# [9, 8, 7, 6, 5, 4, 3, 2, 1]

# 11. crear una funcion llamada calcular_promedio(lista,valor) que reciba una lista de numero
# y un numero valor
#la funcion debe calcular el promedio de la lista y decir si el promedio es mayor que valor.
#debe retornar true si es mayor y false si no lo es.
#datos a usar de ejemplo:

entrada = [10,20,30,40]
valor = 24
#salida esperada true

def calcular_promedio(lista,valor): #parametro reales 
    """
    calcula el promedio de una lista y si retorna un true si el promedio es mayor a un valor o false si es menor 

    parametros: 
        lista (list): lista de numeros a promediar 
        valor (int): numero a comparar con el promedio de la lista 

    retorna: 
        bool: true si el valor es mayor, false si el valor es menor
    """
    suma = 0 
    for i in range(len(lista)):
        suma += lista[i] 
    promedio =suma / len(lista)

    if promedio > valor:
        resultado = True
    else:
        resultado = False
    
    return resultado

#invocacion de la funcion 
print(calcular_promedio(entrada, valor))



        