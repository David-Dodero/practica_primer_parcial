# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.


cuando_viaja = input("ingrese cuando viaja (invierno / verano / otoño / primavera): ")
donde_viaja = input("ingrese a donde viaja (bariloche / mar del plata / catamarca): ")

match cuando_viaja:
    case "invierno":
        if donde_viaja == "bariloche":
            print("elejiste",donde_viaja, "se viaja")
        else:
            print("elejiste",donde_viaja, "No se viaja")
    case "verano":
        if donde_viaja == "mar del plata" or donde_viaja == "cataratas" :
            print("elejiste",donde_viaja, "se viaja")
        else:
            print("elejiste",donde_viaja, "No se viaja")
    case "otoño":
        print("elejiste",donde_viaja, "se viaja")
    case "primavera": 
        if donde_viaja == "bariloche":
            print("elejiste",donde_viaja, "No se viaja")
        else:
            print("elejiste",donde_viaja, "se viaja")