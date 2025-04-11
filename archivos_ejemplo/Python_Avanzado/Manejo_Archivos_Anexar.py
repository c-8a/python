#Anexar informacion sin sobreescribir un archivo


nombre_archivo = "mi_archivo.txt"

with open(nombre_archivo, "a") as archivo:
    archivo.write("se añade una linea al archivo\n")
    archivo.write("se añade otra")

print(f"Se ha anexado informacion al archivo: {nombre_archivo}")
