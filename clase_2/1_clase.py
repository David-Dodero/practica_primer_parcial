#contador
i = 0
#acumulador
total= 0
promedio = 0
for i in range(3):
    numero = int(input("ingrese un numero : "))
    print (numero)
    total = total + numero


print("la suma total",total)
promedio = total / 3 
print("el promedio es de ", promedio)
print("fin del programa")