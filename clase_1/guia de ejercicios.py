#David Dodero
#Div : 213  
# edad = int(input("ingrese su edad: "))
# if edad <= 18:
#     print("ustes es menor de edad ")
# elif  edad <= 24:
#     print("usted es joven ")
# elif edad <= 45:
#     print("usted es mayor ")
# else:
#     print("usted es viejo")

#David Dodero
#Div : 213 

# CLASE 1
# Ejercicio 1:
# Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
# sueldo para esa persona.

# nombre = input("Ingrese su nombre: ")
# sueldo = int(input("Ingrese su sueldo: "))

# incremento = sueldo * 0.10 
# nuevo_sueldo = sueldo + incremento

# print("El incremento del sueldo es de", incremento, "el nuevo sueldo es de ", nuevo_sueldo )

# Ejercicio 2:
# Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
# adolescente (entre 13 y 17 años) o niño (menor a 13 años).

# edad= int(input("Ingrese su edad: "))

# if edad < 13 :
#     print("Usted es un niño. ")
# elif edad < 18:
#     print("Usted es un adolecente. ") 
# else:
#     print("Usted es mayor de edad. ")


# Ejercicio 3:
# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

# pares = 0
# impar = 0
# par_mayor = 0
# num_positivos = 0
# num_negativos = 0
# producto_num = 1
# for i in range(5):
#     numero = int(input("Ingrese un numero distinto de 0: "))
#     while numero == 0:
#         numero = int(input("Error, ingrese un numero distinto de 0: "))
#     print(numero)

#     #a)
#     if numero % 2 == 0:
#         pares += 1
#         #c)
#         if numero > par_mayor:
#             par_mayor = numero
#     else:
#         impar += 1
#     #b)
#     if i == 1:
#         menor_numero = numero

#     if numero < menor_numero:
#         menor_numero = numero

#     #d)
#     if numero > 0:
#         num_positivos = num_positivos + numero
        
        
#     #e) 
#     if numero < 0:
#         producto_num = producto_num * numero
#         num_negativos += 1

    

# #a)
# print(f"cantidad de pares es de {pares} y cantidad de impares es de {impar}")
# #b)
# print("el menor numero es", menor_numero)
# #c)
# print("El mayor numero par es de ", par_mayor)
# #d)
# print("la suma de los positivos es de ",num_positivos )
# #e)
# if num_negativos > 0:
#     print(" el producto de los negativos es de ",producto_num)
# else:
#     print("no hay numeros negativos para sacar el producto ")   

# Ejercicio 4:
# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
# distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
# ser soltero.'

# edad = int(input("ingrese su edad: "))
# estado_civil = input("ingrese su estado civil: ")

# if edad < 18 and estado_civil != "Soltero" :
#     print("Es muy pequeño para NO ser soltero.")
    


# Ejercicio 5:
# Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
# por cada estadía como base, se pide el ingreso de una estación del
# año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
# Plata/Córdoba) para vacacionar para poder calcular el precio final:
# -en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
# descuento del 10% Mar del Plata tiene un descuento del 20%
# -en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
# un aumento del 10% Mar del Plata tiene un aumento del 20%
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
# aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
# precio sin descuento.
# Validar el ingreso de datos

tarifa_base = 15000
estacion_del_año = input('ingrese una estacion del año(Invierno/Verano/Otoño/Primavera): ')
localidad = input("ingrese una localidad(Bariloche/Cataratas/Mar del Plata/Córdoba): ")
porciento_20 = tarifa_base * 0.20
porciento_10 = tarifa_base * 0.10
match estacion_del_año:
    case "Invierno" :
        if localidad == "Bariloche":
            tarifa_final = tarifa_base + porciento_20 
            #print(tarifa_final)
        elif localidad == "Cataratas" or localidad == "Córdoba":
            tarifa_final = tarifa_base - porciento_10
            #print(tarifa_final)
        elif localidad == "Mar del Plata":
            tarifa_final = tarifa_base - porciento_20
            #print(tarifa_final)
        else:
            print("no se elijio ninguna localidad correcta ")
    case "Verano" :
        if localidad == "Bariloche":
            tarifa_final = tarifa_base - porciento_20
        elif localidad == "Cataratas" or localidad == "Córdoba":
            tarifa_final = tarifa_base + porciento_10
        elif localidad == "Mar del Plata":
            tarifa_final = tarifa_base + porciento_20
        else:        
            print("no se elijio ninguna localidad correcta ")
    case "Otoño" | "Primavera":
        if localidad == "Bariloche" or localidad == "Cataratas" or localidad == "Mar del Plata":
            tarifa_final = tarifa_base + porciento_10
        elif localidad == "Córdoba":
            tarifa_final = tarifa_base
        else:
            print("no se elijio ninguna localidad correcta ")

print("el precio final es de: ", tarifa_final)






