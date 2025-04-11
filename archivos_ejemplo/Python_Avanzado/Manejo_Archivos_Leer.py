# Se pueden utilizar los metodos:
#se debe abrir en modo lectura con "r"
#read()
#readline()
#readlines()

nombre_archivo = "mi_archivo.txt"

with open(nombre_archivo, "r") as archivo:
    #print(archivo.readlines()) #imprime todas las lineas del archivo
    #recupera una lista con todas las lineas
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip()) #el metodo strip quita los espacios en blanco,
        # tabuladores y saltos de linea que tengamos al inicio o al final de una cadena


#Leer todo el contenido del archivo utilizando el metodo read
print("Leyendo el contenido con el metodo read")
with open(nombre_archivo, "r") as archivo:
    print(archivo.read().strip())
