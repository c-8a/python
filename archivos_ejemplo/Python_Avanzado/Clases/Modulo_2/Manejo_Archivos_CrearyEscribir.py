#Crear un archivo

nombre_archivo = "mi_archivo.txt"

#Abrir el archivo en modo escritura (w)

# Esta es una manera de trabajar con archivos
# somos nosotros los responsables de cerrar el archivo al finalizar

#archivo = open(nombre_archivo, "w")
#archivo.write("Hola, como estás?\n")
#archivo.write("Se agrega más informacion al archivo\n")
#archivo.close()

#Con el bloque "with" +...+ "as" + ...
#nos despreocupamos de tener que cerrar los recursos de ese bloque

with open(nombre_archivo, "w") as archivo:
    archivo.write("Hola, como estás?\n")
    archivo.write("Se agrega más informacion al archivo\n")

print (f"Se creó el archivo {nombre_archivo}")


#Crear archivo en modo exclusivo
#si ya existe, arroja una excepcion
nombre_archivo = "mi_archivo.txt"

try:
    with open(nombre_archivo, "x") as archivo:
        archivo.write("Escritura en modo exclusivo\n")
        archivo.write("Espero que sirva\n")
        print(f"Se ha creado el archivo: {nombre_archivo}")
except FileExistsError as e:
    print(f"El archivo {nombre_archivo} ya existe")
    print(f"Detalle del error: {e}")

