#Asignar funciones a variables
def sumar(a, b):
    return a + b 

operacion = sumar

print(operacion(4, 2)) #6

#Almacenarlas en estructuras de datos (listas)
def sumar(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

operaciones = [sumar, resta, multiplicacion]

for operacion in operaciones:
    print(operacion(10, 5)) #15 , 5 , 50

#si quiero solo la suma con tupla
operaciones = (sumar, resta, multiplicacion)

resultado_suma = operaciones[0](10, 5)
print(f"el resultado de la suma es {resultado_suma}") #el resultado de la suma es 15

#si quiero solo la multiplicacion con diccionario 
operaciones = {
    "suma": sumar,
    "restar": resta,
    "multiplicar": multiplicacion
}

resultado = operaciones["multiplicar"](10,5)
print(f"resultado de la multiplicacion:{resultado}") #resultado de la multiplicacion:50

#Función que toma otra función como parámetro
def operar(x, y, funcion):
    return funcion(x, y)

resultado_suma = operar(10, 5, sumar)
resultado_resta = operar(10, 5, resta)

print(f"resultado de la suma: {resultado_suma}")   #resultado de la suma: 15
print(f"resultado de la resta: {resultado_resta}") #resultado de la resta: 5

def aplicar_operacion(numero, funcion):
    resultado = funcion(numero)
    return resultado

def duplica(x):
    return x * 2


def triplicar(x):
    return x * 3

resultado1 = aplicar_operacion(5, duplica)
resultado2 = aplicar_operacion(5, triplicar)

print(resultado1) #10
print(resultado2) #15

#Función que toma otra función como parámetro
def ordenar_lista(funcion, lista):
    '''ordena una lista segun una funcion de comparacion'''
    lista.sort(key=funcion)
    return lista 

def ordenar_por_longitud(cadena):
    return len(cadena)

palabra = ["manzana", "banana", "pera"]
resultado = ordenar_lista(ordenar_por_longitud,palabra)
print(resultado) #['pera', 'banana', 'manzana']

# Función que toma otra función como parámetro
def filtrar_lista(funcion, lista):
    '''filtra una lista segun una funcion de predicado'''
    resultado = []
    for elemento in lista:
        if funcion(elemento):
            resultado.append(elemento)
    return resultado

def es_par(numero):
    return numero % 2 == 0

numero = [1, 2, 3, 4, 5]
resultado = filtrar_lista(es_par, numero)
print(resultado) #[2, 4]
#///////////////////////////////////////////////////////////////

#Función que devuelve otra función
def funcion_externa(x):
    return x + 5

def retornar_funcion():
    return funcion_externa

#obtener la funcion externa
mi_funcion = retornar_funcion()

#usar la funcion externa
resultado = mi_funcion(10)
print(resultado) #salida 15
#///////////////////////////////////////////////////////////////////

def crear_multiplicador_con_base(base):
    def multiplicador_con_base(x):
        return base * x
    return multiplicador_con_base

#crear una funcion que multiplica por 10 
multiplicar_por_10 = crear_multiplicador_con_base(10)

#usar la funcion generada 
resultado = multiplicar_por_10(7)
print(resultado) #70

#///////////////////////////////////////////////////////

def formatear_mayusculas(texto):
    return texto.upper()

def formatear_minusculas(texto):
    return texto.lower()

def formatear_titulo(texto):
    return texto.title()

#funcion que retorna la funcion de manera deseada 
def obtener_formateo(tipo):
    if tipo == "mayuscula":
        return formatear_mayusculas
    elif tipo == "minuscula":
        return formatear_minusculas
    elif tipo == "titulo":
        return formatear_titulo
    else:
        raise ValueError("tipo de formateo no valido")

texto = "hola mundo"

formateador = obtener_formateo('mayuscula')
resultado = formateador(texto)
print(f"texto en mayuscula: {resultado}") #texto en mayuscula: HOLA MUNDO

formateador = obtener_formateo('minuscula')
resultado = formateador(texto)
print(f"texto en minuscula: {resultado}") #texto en minuscula: hola mundo

formateador = obtener_formateo('titulo')
resultado = formateador(texto)
print(f"texto en titulo: {resultado}") #texto en titulo: Hola Mundo



#funciones lambada 
suma = lambda a, b: a + b 
print(suma(2,4)) #6

#Comparando una función normal con una función lambda
def suma(a, b, c):
    return a + b + c
resultado = suma(2, 3, 4)
print(f"el resultado de la suma es  {resultado}") #el resultado de la suma es  9

suma_lambda = lambda a, b , c : a + b + c
resultado_lambda = suma_lambda(2, 3, 4) 
print(resultado_lambda) #9

#lambda como parámetro de una función
def validar(valor, condicion):
    return condicion(valor)

es_positivo = lambda x: x > 0 
print(validar(10, es_positivo)) #true
print(validar(-5, es_positivo)) #false

