# Estructura repetitivas FOR
# Actividades
# 1. Mostrar los números ascendentes desde el 1 al 10

# for i in range (1,11):
#     print(i)

# 2. Mostrar los números descendentes desde el 10 al 1
# ¿Qué significa cada número en range(10, 0, -1)?
# 10 es el valor inicial (empieza en 10)
# 0 es el límite que no se incluye (va hasta 1)
# -1 es el paso (va restando de a uno)

# for i in range (10, 0, -1):
#     print(i)

# 3. Ingresar un número. Mostrar los números desde 0 hasta el número
# ingresado.

# numero = int(input("ingrese un numero: "))
# for i in range(0, numero + 1):
#     print(i)

# 4. Ingresar un número y mostrar la tabla de multiplicar de ese número. Por
# ejemplo si se ingresa el numero 5:
# 5 x 0 = 0
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15 …

# numero = int(input('ingrese un numero: '))

# for i in range(0, 11):
#     resultado = numero * i
#     print(f"{numero} x {i} = {resultado}")

# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el
# número 0. Mostrar la suma y el promedio de todos los números.
# suma = 0
# cant_num = 0
# for i in range(0,10):
#     num= int(input("ingrese un numero: "))
#     if num == 0:
#         break
#     else:
#         cant_num += 1
#         suma= suma + num


# promedio = suma / cant_num
# print(f"el promedio es de {promedio}")

# 6. Imprimir los números múltiplos de 3 entre el 1 y el 10 (*)
#el número que querés evaluar (i) va primero, y el número que querés usar como múltiplo (en este caso 3) va después en el módulo.
# for i in range (1, 11 ): 
#     if i % 3 == 0 :
#         print(i)

#7. Mostrar los números pares que hay desde la unidad hasta el número 50 (*)
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)

# 8. Realizar un programa que permita mostrar una pirámide de números. Por
# ejemplo: si se ingresa el numero 5, la salida del programa será la
#siguiente: 
# 1
# 12
# 123
# 1234
# 12345

# piramide = ""

# for i in range(1,6):
#     piramide += str(i)
#     print(piramide)

# 9. Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta
# el número ingresado. Mostrar la cantidad de divisores encontrados.

# numero =  int(input("ingrese un numero: "))
# contador = 0

# for i in range(1,numero + 1):
#     divisor = numero % i 
#     if divisor == 0:
#         contador+= 1
#         print(i) 
# print(contador)        

# 10.Ingresar un número. Determinar si el número es primo o no.

# num = int(input("ingrese un numero: "))

# if num == 1 :
#     print(f"el numero {num} no es primo")
# else:    
#     cont = 0
#     for i in range(1, num + 1):
#         if num % i == 0: 
#             cont += 1 
#     if cont > 2 :
#         print(f"el numero {num} no es primo")
#     else:
#         print(f"el numero {num} es primo")

# 11.Ingresar un número. Mostrar cada número primo que hay entre el 1 y el
# número ingresado. Informar cuántos números primos se encontraron.


num = int(input("Ingresá un número: "))
contador_primos = 0

for i in range(2, num + 1):
    divisor = 1
    cantidad_divisores = 0

    while divisor <= i:
        if i % divisor == 0:
            cantidad_divisores += 1
        divisor += 1

    if cantidad_divisores == 2:
        print(f"{i} es primo")
        contador_primos += 1

print(f"Se encontraron {contador_primos} números primos")