entrada = [10,20,30,40]
valor = 24 

def calcular_promedio(lista, valor):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
    promedio = suma / len(lista)

    if promedio > valor:
        print(True)
    else:
        print(False)
calcular_promedio(entrada,valor)