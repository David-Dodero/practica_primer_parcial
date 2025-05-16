#David Dodero
#1. Realizar una función recursiva que calcule la suma de los primeros números naturales:
def sumar_naturales(numero: int)->int:
    if numero != 0:
        return numero + sumar_naturales(numero - 1)
    else:
        return 0 
    
#print(sumar_naturales(3))

#2. Realizar una función recursiva que calcule la potencia de un número:
def calcular_potencia(base: int, exponente: int)-> int:
    if exponente != 0:
        return base * calcular_potencia(base, exponente - 1 )
    else:
        return 1
    
#print(calcular_potencia(2, 4))

#3. Realizar una función recursiva que permita realizar la suma de los dígitos de un número
def sumar_digitos(numero: int)-> int:
    if numero != 0:
        return numero % 10 + sumar_digitos(numero // 10 )
    else:
        return 0
#print(sumar_digitos(543))

# Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La
# función deberá seguir el siguiente prototipo:
# Definición:
# La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de
# los dos anteriores:

def calcular_fibonacci(numero: int)->int:
    if numero == 0 or numero == 1:
        return numero
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)
numero = int(input("ingrese un numero: "))
#print(calcular_fibonacci(9))

for i in range(numero + 1):
    resultado = calcular_fibonacci(i)
    if i > 1:
        print(f"F({i}) = F({i - 1}) + F({i - 2}) = {resultado}")
    else:
        print(f"F({i}) = {resultado}")