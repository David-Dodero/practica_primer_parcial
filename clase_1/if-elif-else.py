#1) A partir del ingreso de la altura en centímetros de un jugador de baloncesto,
# el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

# altura = int(input("ingrese su altura: "))

# if altura < 160:
#     print("sos base, tu altura es de",altura,"cm")
# elif altura < 179:
#     print("sos escolta, tu altura es de",altura,"cm")
# elif altura < 199:
#     print("sos alero, tu altura es de",altura,"cm")
# else:
#     print("sos ala-pivo / pivot, tu altura es de",altura,"cm")


#2) Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

nota = int(input("ingrese su nota: ")) 

if nota >= 1 and nota <= 3:
    print("Desaprobado, la nota es", nota)
elif nota >= 4 and nota <=5 :
    print("Aprobado, la nota es", nota)
elif nota >= 6 and nota <= 10:
    print("Promoción directa, la nota es")
else:
    print("la nota", nota, "que agregaste no es valida")