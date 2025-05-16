# Ejercicio 2: Dadas las siguientes listas:
# Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias
# Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos",
# "Base de Datos", "Ergonomia", "Naturaleza"]
# Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]
# Desarrollar una función que realice el ordenamiento de las listas por nombre de
# manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera
# descendente.

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias" , "Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"]
Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98]

for i in range(len(Nombres)-1):
    for j in range(i+1, len(Nombres)):
        if Nombres[i] > Nombres[j]:
            aux = Nombres[i]
            Nombres[i] = Nombres[j]
            Nombres[j] = aux

            
            aux_puntos = Puntos[i]
            Puntos[i] = Puntos[j]
            Puntos[j] = aux_puntos
        elif Nombres[i] == Nombres[j]:
            if Puntos[i] < Puntos[j]:
                aux_puntos = Puntos[i]
                Puntos[i] = Puntos[j]
                Puntos[j] = aux_puntos

                aux = Nombres[i]
                Nombres[i] = Nombres[j]
                Nombres[j] = aux

#print(len(Nombres), len(Puntos))

# for i in range(len(Nombres)):
#     print(Nombres[i], Puntos[i])

# Ejercicio 3: Dadas las siguientes listas:
# Estudiantes =
# ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Anto
# nio", "Eugenia", "Soledad", "Mario", "María"]
# Apellidos =
# [“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”
# ,”Mitre”,”Andrade”,”Loza”,”Antares”,”Roca”,”Perez”]
# Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]
# Desarrollar una función que realice el ordenamiento de las listas por apellido de
# manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera
# ascendente, si el nombre también es el mismo, debe ordenar por nota de manera
# descendente.

Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"]
Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"]
Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8]

def ordenar_apellido_nombre_edad():
    for i in range(len(Apellidos)-1):
        for j in range(i+1, len(Apellidos)):
            if Apellidos[i] > Apellidos[j]:
                aux = Apellidos[i]
                Apellidos[i] = Apellidos[j]
                Apellidos[j] = aux

                aux_estudiante = Estudiantes[i]
                Estudiantes[i] = Estudiantes[j]
                Estudiantes[j] = aux_estudiante

                aux_nota = Nota[i]
                Nota[i] = Nota[j]
                Nota[j] = aux_nota



            elif Apellidos[i] == Apellidos[j]:
                if Estudiantes[i] > Estudiantes[j]: 
                    aux = Apellidos[i]
                    Apellidos[i] = Apellidos[j]
                    Apellidos[j] = aux

                    aux_estudiante = Estudiantes[i]
                    Estudiantes[i] = Estudiantes[j]
                    Estudiantes[j] = aux_estudiante

                    aux_nota = Nota[i]
                    Nota[i] = Nota[j]
                    Nota[j] = aux_nota           
            
                elif Estudiantes[i] == Estudiantes[j]: 
                    if Nota[i] < Nota [j]:
                        aux = Apellidos[i]
                        Apellidos[i] = Apellidos[j]
                        Apellidos[j] = aux

                        aux_estudiante = Estudiantes[i]
                        Estudiantes[i] = Estudiantes[j]
                        Estudiantes[j] = aux_estudiante

                        aux_nota = Nota[i]
                        Nota[i] = Nota[j]
                        Nota[j] = aux_nota

ordenar_apellido_nombre_edad()

for i in range(len(Estudiantes)):
    print("Apellido del estudiante:", Apellidos[i])
    print("Nombre del estudiante:",Estudiantes[i])
    print("Nota del estudiante:", Nota[i])

    