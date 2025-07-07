# Título: Gestión de Calificaciones de Estudiantes con Lista/Array y Matriz en Python
# Descripción: Se dispone de una lista/array con 4 estudiantes: ["Ana", "Bruno", "Carla", "Diego"] y una matriz
# que contiene sus calificaciones en 3 materias: Matemática, Historia y Biología.
# Cada fila representa a un estudiante y cada columna a una materia.
# Desarrolla un programa en Python que permita al usuario:
#  Mostrar la lista de estudiantes y la matriz de calificaciones (con etiquetas legibles).
#  Ordenar a los estudiantes de mayor a menor según su promedio general (promedio de sus 3 materias).
#  Buscar un estudiante por nombre y mostrar sus calificaciones.
#  Buscar una calificación en la matriz y mostrar a qué estudiante y materia pertenece.
# 2
# Nota:
#  La lista de estudiantes y la matriz deben estar sincronizadas en todo momento (es decir, si se reordenan,
# deben coincidir).
#  Pueden utilizarse funciones propias para separar las tareas.
#  El código debe estar comentado adecuadamente.

#lista de estudiantes (indice i)
estudiantes = ["Ana", "Bruno", "Carla", "Diego"]

#matriz de calificacions por estudiante [matematica, historia, biologia]
calificaciones = [
    [9, 8 , 10], #Ana   
    [6, 7, 8],   #Bruno
    [10, 10, 9], #Carla
    [7, 6, 5]    #Diego
] 


def menu_gestion_estudiantes():
    """
    Muestra un menú con opciones para gestionar estudiantes y sus calificaciones.
    """
    seleccionar = 0
    while seleccionar != 5: 
        print(" MENU DE OPCIONES DE GESTION DE ESTUDIANTES")
        print("1 Mostrar estudiantes y calificacions")
        print("2 Ordenar estudiantes segun su promedio ")
        print("3 Buscar estudiante por nombre y mostrar calificacion")
        print("4 Buscar calificacion y mostrar a qué estudiante y materia pertenece")
        print("5 Salir")

        seleccionar = int(input("Ingrese un número del 1 al 5: "))
        while seleccionar < 1 or seleccionar > 5:
            seleccionar = int(input("Error, ingrese un número del 1 al 5: "))
    
        match seleccionar:
            case 1:
                mostrar_estudiante_calificaciones() 
            case 2:
                ordenar_estudiantes_segun_promedio()
            case 3:
                buscar_estudiante_por_nombre()
            case 4:
                buscar_calificacion_de_estudiante()
            case 5:
                salir()


def mostrar_estudiante_calificaciones():
    """
    Muestra todos los estudiantes con sus respectivas calificaciones.
    """
    for i in range(len(estudiantes)):
        print(f"Estudinte: {estudiantes[i]}, ", end=" " )
        for j in range(len(calificaciones[i])):
            print(f"Calificacion: {calificaciones[i][j]},", end=" ")
        print(" ")


def ordenar_estudiantes_segun_promedio():
    """
    Ordena a los estudiantes según su promedio de calificaciones (de mayor a menor)
    y muestra el resultado por pantalla.
    """
    promedio = [0] * len(calificaciones)
    
    for i in range(len(calificaciones)):
        for j in range(len(calificaciones[i])):
            promedio[i] += calificaciones[i][j]  # Suma de notas
        promedio[i] /= len(calificaciones[i])    # División para sacar promedio

    for i in range(len(promedio)-1):
        for j in range(i+1, len(promedio)):
            if promedio[i] < promedio[j]:
                aux = promedio[i]
                promedio[i] = promedio[j]
                promedio[j] = aux

                aux = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux

                aux = calificaciones[i]
                calificaciones[i] = calificaciones[j]
                calificaciones[j] = aux

    for i in range(len(estudiantes)):
        print(f"{estudiantes[i]} - Promedio: {promedio[i]}")

def buscar_estudiante_por_nombre():
    """
    Solicita al usuario el nombre de un estudiante, y si lo encuentra, muestra sus calificaciones.
    """
    buscar_estudiante = input("Ingrese el nombre del estudiante que desea buscar: ")

    encontrado = False
    for i in range(len(estudiantes)):
        if estudiantes[i] == buscar_estudiante:
            encontrado = True
            posicion = i

    if encontrado == True:
        print(f"El nombre buscado es: {estudiantes[posicion]}, sus calificaciones son: {calificaciones[posicion]} ")
            
    else:
        print(f"El estudiante: {buscar_estudiante}, no fue encontrado")


def buscar_calificacion_de_estudiante():
    """
    Solicita una calificacion y muestra a qué estudiante y materia pertenece.
    """
    calificacion_buscada = int(input("Ingrese la calificación que desea buscar: "))
    
    encontrado = False
    materias = ["Matematica", "Historia", "Biologia"]  

    for i in range(len(calificaciones)):        #i recorre las filas, o sea, los estudiantes
        for j in range(len(calificaciones[i])): #j recorre las columnas, o sea, las materias
            if calificaciones[i][j] == calificacion_buscada:
                print(f"La calificación {calificacion_buscada} pertenece a {estudiantes[i]} en {materias[j]}")
                encontrado = True
    
    if encontrado == False:
        print(f"no se encontro la calificacion: {calificacion_buscada}")

def salir():
    """
    Muestra un mensaje de salida del programa.
    """
    print("Saliste del menú de opciones.")

#invocacion de la funcion 
menu_gestion_estudiantes()