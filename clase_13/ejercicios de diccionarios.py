# DICCIONARIOS
# Ejercicio 1: Se trabajará con el archivo estudiantes.py
# Realizar una función con el siguiente Menú de Opciones:
# 1-Listar los alumnos por orden ascendente de apellido, si se repite,
# ordenar por nombre. Mostrar legajo, nombre, apellido y edad
# 2-Obtener el promedio de notas para cada estudiante
# 3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el
# programa de “Ingenieria en Informatica”
# 4-Obtener un promedio de edad de los estudiantes. Mostrar nombre y
# apellido
# 5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y
# apellido
# 6-Listar nombre y apellido de los alumnos que forman el grupo “Club de
# Informática” con sus respectivos promedios
# 7-Listar legajo, nombre, apellido y programas que cursan los alumnos
# más jóvenes.
# Ejercicio 2: Crear una función para cada opción de menú.

from estudiantes import estudiantes


def menu_opciones():
    print("MENU DE OPCIONES")
    print("1-lista de alumnos de forma ascendete")
    print("2-promedio de nota de cada estudiante)")
    print("3-datos de estudiantes que cursan “Ingenieria en Informatica” ")
    print("4-promedio de edad")
    print("5-alumno de mayor promedio de nota")
    print("6-alumno de club de informatica ")
    print("7-almuno mas jovenes")

    
        
    seleccionar = int(input("ingrese un numero del 1 a 7: "))
    while seleccionar < 1 or seleccionar > 7:
        seleccionar = int(input("ingrese un numero del 1 a 7: "))
    
    match seleccionar:
        case 1:
            alumnos_ordenados()
        case 2:
            promedio_notas()
        case 3:
            inginieria_informatica()
        case 4:
            promedio_edad()
        case 5:
            alumno_mayor_nota()
        case 6:
            club_de_informatica()
        case 7:
            mas_jovenes()







def alumnos_ordenados():
    for i in range(len(estudiantes)-1):
        for j in range(i+1, len(estudiantes)):
            if estudiantes[i]["apellido"] > estudiantes[j]["apellido"]:
                aux = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux
            elif estudiantes[i]["apellido"] == estudiantes[j]["apellido"]:
                if estudiantes[i]["nombre"] > estudiantes[j]["nombre"]:
                    aux = estudiantes[i]
                    estudiantes[i] = estudiantes[j]
                    estudiantes[j] = aux
    
    for alumno in estudiantes:
        print("apellido:", alumno["apellido"],
              "nombre:", alumno["nombre"],
              "legajo:", alumno["legajo"],
                "edad:", alumno["edad"])

def promedio_notas():
    for alumno in estudiantes:
        suma_notas = 0
        for nota in alumno["notas"]:
            suma_notas += nota
        promedio = suma_notas / len(alumno["notas"])
        print("apellido:", alumno["apellido"],
            "nombre:", alumno["nombre"],
            "notas", alumno["notas"],
            "el promedio de las notas es:", promedio)

def inginieria_informatica():
    for alumno in estudiantes:
        if alumno["programa"]["nombre"] == "Ingenieria en Informatica":
            print("legajo:",alumno["legajo"],
                "apellido", alumno["apellido"],
                "nombre:", alumno["nombre"],
                "edad:", alumno["edad"]  
                                      )

def promedio_edad():
    suma_edades = 0
    for alumno in estudiantes:
        suma_edades += alumno["edad"]
    promedio = suma_edades / len(estudiantes)
    print("El promedio de edades de los alumnos: ", promedio)
    print("listado de estudiantes: ")
    for alumno in estudiantes:
        print("nombre:", alumno["nombre"],
              "apellido:", alumno["apellido"])


def alumno_mayor_nota():
    promedio_mayor = 0
    alumnos_promedio_mayor = []
    for alumno in estudiantes:
        suma_notas = 0
        for nota in alumno["notas"]:
            suma_notas += nota
        promedio = suma_notas / len(alumno["notas"])
        if promedio > promedio_mayor:
            promedio_mayor = promedio
            alumnos_promedio_mayor = [alumno]
        elif promedio == promedio_mayor:    
            alumnos_promedio_mayor.append(alumno)
            
    for alumno in alumnos_promedio_mayor:       
        print("el promedio es:", promedio_mayor,
            "nombre:", alumno["nombre"],
            "apellido:", alumno["apellido"])

def club_de_informatica():
  
    for alumno in estudiantes:
        if "grupos" in alumno:
            for grupos in alumno["grupos"]:
                if grupos["nombre"] == "Club de Informatica" :
                    suma_notas = 0
                    for notas in alumno["notas"]:
                        suma_notas += notas
                    promedio = suma_notas / len(alumno["notas"])
        
                    print("nombre:", alumno["nombre"],
                        "apellido:", alumno["apellido"],
                        "el promedio de notas del club de informatica es: ", promedio)

                    
def mas_jovenes():
    alumnos_jovenes = []
    edad_menor = estudiantes[0]["edad"]
    for alumno in estudiantes:
        if alumno["edad"] < edad_menor :
            edad_menor = alumno["edad"]
            alumnos_jovenes = [alumno]
        elif edad_menor == alumno["edad"]:
            alumnos_jovenes.append(alumno)

    for alumno in alumnos_jovenes:
        print("la edad de los alumnos mas jovenes es:", edad_menor,
              "legajo:",alumno["legajo"], 
              "nombre:", alumno["nombre"],
              "apellido:", alumno["apellido"],
              "programa:", alumno["programa"])

menu_opciones()