lista = ["Ana", "Juan", "Sol"] #lista de cadena de caracteres
lista = [23,45,65] #lista de enteros
lista = [ ["Ana", 23], [ "Juan", 45], ["Sol", 65] ] #lista de listas/listas anidadas

contactos = [["ana",23],["juan",45],["sol",65]]
print(contactos[1]) #juan 45 
print(contactos[1][1]) #45 

contactos[1][1] = 66 # modifica los elementos
print(contactos[1])# juan 66

contactos.append(["luis"]) # lo agrega en la ultima posicion 
print(contactos)#agrega a luis pero sin edad

contactos[3].append(22)
print(contactos) #[['ana', 23], ['juan', 66], ['sol', 65], ['luis', 22]]


for e_contacto in contactos: #Recorrer la lista y mostrar los datos con For
    print(e_contacto[0], e_contacto[1])  #para printear recorrer listas  

contactos.pop() #eliminael ultimo en este caso luis 
contactos.pop(2) #elimina a sol
contactos[1].pop() #elimina la edad 22 de luis

for e_contacto in contactos:
    if len(e_contacto) == 2:
        print(e_contacto[0], e_contacto[1])
    else:
        print(e_contacto[0], "(edad no disponible)")
