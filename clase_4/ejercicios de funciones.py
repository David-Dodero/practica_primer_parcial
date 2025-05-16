#David Dodero
#Div: 213 
# Ejercicio 3-1: Crear una función que muestre por pantalla el número que recibe
# # como parámetro.
# def mostrar_numero (numero):
#     print(numero)
# num = int(input("ingrese un numero" ))
# mostrar_numero(num)

# Ejercicio 3-2: Crear una función que pida el ingreso de un número y lo retorne

# def ingrese_un_numero ():
#     numero = int(input("ingrese un numero: "))
#     return numero
# print(ingrese_un_numero())

# Ejercicio 3-3: Crear una función que permita determinar si un número es par o no. La
# función retorna “True” en caso afirmativo y “False en caso contrario. Probar en el
# programa principal realizando la invocación o llamada.

# def verificar_par (num: int)-> bool:
#     if num % 2 == 0:
#         return True
#     else:
#         return False
# numero = int(input("ingrese un numero: "))
# print(verificar_par(numero))

# Ejercicio 3-4: Especializar la función del punto 3.1 y 3.2 para que valide el número en
# un rango determinado pasado por parámetro “desde”-“hasta”.

# def mostrar_numero (numero:int):
#     print(numero)
# #num = int(input("ingrese un numero" ))
# #mostrar_numero(num)
# def ingrese_un_numero ():
#     numero = int(input("ingrese un numero: "))
#     return numero
# #print(ingrese_un_numero())

# def mostrar_numero_desde_hasta (desde:int, hasta:int):
#     """
#     verifica que el numero ingresado en la funcion mostrar_numero() este dentro de un rango 
#     """
#     numero = ingrese_un_numero()
#     if numero > desde and numero < hasta:
#         print(f"el numero {numero} esta dentro del rango desde {desde}, hasta {hasta}")
#         mostrar_numero(numero)
#     else:
#         print(f"el numero {numero} no esta dentro del rango desde {desde}, hasta {hasta}")
#         mostrar_numero(numero)
# mostrar_numero_desde_hasta(1, 10)

# Ejercicio 3-5: Realizar un programa en donde se puedan utilizar los prototipos de la
# función Restar en sus 4 combinaciones.
#  Restar1(int, int)->int:
#  Restar2()->int:
#  Restar3(int, int):
#  Restar4():

# def Restar1(num:int, num2:int)->int:
#     resta= num - num2 
#     return resta
# # print(Restar1(2,10))
# numero = int(input("ingrese un numero: "))
# numero2 = int(input("ingrese otro un numero: "))
# respuesta = Restar1(numero, numero2)
# print(f"la resta de {numero} y {numero2} es de {respuesta}")

# def Restar2()->int:
#     numero = int(input("ingrese un numero: "))
#     numero2 = int(input("ingrese otro un numero: "))
#     resta2 = numero - numero2 
#     return resta2
# respuesta2 = Restar2()
# print(f"la resta es de {respuesta2}")

# def Restar3(num:int, num2:int):
#     resta3 = num - num2
#     print(f"El resultado de la resta es: {resta3}")
# Restar3(3,9)
    
# def Restar4():
#     numero = int(input("ingrese un numero: "))
#     numero2 = int(input("ingrese otro un numero: "))
#     resta4 = numero - numero2
#     print(f"El resultado de la resta es: {resta4}")
# Restar4()

# Ejercicio 3-6: Realizar un programa que: asigne a la variable numero1 un valor
# solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a
# dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado
# por pantalla. Atención: pueden reutilizarse funciones ya creadas.

# def mostrar_numero (numero):
#     print(numero)
# # num = int(input("ingrese un numero" ))
# # mostrar_numero(num)
# def ingrese_un_numero ():
#     numero = int(input("ingrese un numero: "))
#     return numero
# #print(ingrese_un_numero())

# def realizarDescuento():
#     numero1 = ingrese_un_numero()
#     if numero1 >= 10 and numero1 <= 100 :
#         descuento_5 = numero1 - (numero1 * 0.05)   
#         print("numero ingresado:")
#         mostrar_numero(numero1)
#         print(f"precio final con 5% de descuento: {descuento_5}")
#     else:
#         print("numero ingresado:")
#         mostrar_numero(numero1)
#         print("el numero elejido no esta en el rango entre el 10 y el 100")
        
# realizarDescuento()

# Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2
# los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la
# variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice
# la operación de dichos valores a través de una función. Mostrar el resultado por
# pantalla.


def suma_o_resta():
    
    numero1 = int(input("ingrese un numero entre el 10 y el 100: "))
    while numero1 < 10 or numero1 > 100:
        numero1 = int(input("ingrese un numero entre el 10 y el 100: "))

    numero2 = int(input("ingrese un numero entre el 10 y el 100: "))
    while numero2 < 10 or numero2 > 100:
        numero2 = int(input("ingrese un numero entre el 10 y el 100: "))    
    
    operacion = input("ingrese 's' para la suma o 'r' para la resta ")
    while operacion != 's' and operacion != 'r':
        operacion = input("error, ingrese 's' para la suma o 'r' para la resta ")
    
    if operacion == 's':
        suma = numero1 + numero2
        print(f"la suma de el numero {numero1} y el numero {numero2} es de {suma}")
    else:
        resta = numero1 - numero2
        print(f"la resta de el numero {numero1} y el numero {numero2} es de {resta}")
   
    
    
#suma_o_resta()

# 8) Define una función que encuentre el máximo de tres números. La función debe aceptar tres
# # argumentos y devolver el número más grande.
 
def maximo_numero(num: int)->int:
    pass