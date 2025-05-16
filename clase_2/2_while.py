#while quiere decir mientras, es un condicional(pone condiciones para que funciones) 
#se repite hasta que se cumpla una condicion, es parecido al if 
#nunca olvidarse de incrementar la variable, para que no entre en bucle infinito 

i = 0 

while (i < 3):
    print("itero con while", i)
    i += 1
print("fin del programa")

#esto no es buena practica de programacion, no esta bueno que termine con breack
i = 0
while True: 
    print (i)
    i += 1
    if i == 3:
        break 
#que termine por algo logico que yo pense, no por un break violento 
#el programador debe pensar/saber para que quiere usar el while 

respuesta = 's'

while respuesta == 's':
    nota = int(input("ingrese una nota: "))
    print("nota ingresada: ",nota)

    respuesta = input("desa seguir agregando nota? (s/n)")

print("fin del programa")
#cualquier respuesta diferente a s corta el programa

#validar el ingreso de datos

nota= int(input("ingrese una nota menor a 10: "))
while nota > 10:
    nota = int(input("error, ingrese una nota menotr a 10: "))

print("nota correcta", nota)

#validar el ingreso de datos en un rango como de (1 - 10) necesito lo que no quiero  

nota= int(input("ingrese una nota entre 1 y 10: "))
while nota < 1 or nota > 10:
    nota = int(input("error, ingrese una nota entre 1 y 10: "))

print("nota correcta", nota)