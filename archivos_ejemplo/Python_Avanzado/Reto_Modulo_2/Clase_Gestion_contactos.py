class GestionContactos:

    def __init__(self):
        self.nombre_archivo = "Agenda_Contactos.txt"

    def agregar_contacto(self, contacto):
        try:
            with open(self.nombre_archivo, "a", encoding='utf-8') as archivo:
                archivo.write(f"{contacto.get_nombre()}\n")
                archivo.write(f"{contacto.get_telefono()}\n")
                archivo.write(f"{contacto.get_email()}\n\n")
                print("Contacto agendado exitosamente\n")
        except Exception as e:
            print(f"Error al agregar contacto: {e}")

    def mostrar_contactos(self):
        contador = 0
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo.readlines():
                    print(f"- {linea}", end="")
                    linea_sin_espacios = linea.strip()
                    if not linea_sin_espacios:
                        contador += 1
                print(f"Se encontraron {contador} contactos")
        except Exception as e:
            print(f"Error al abrir o leer el archivo: {e}")

    def buscar_contacto(self, nombre):
        encontrado = False
        contador = 0
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                for i, linea in enumerate(archivo):
                    if nombre.lower() in linea.lower():
                        contador += 1
                        print(f"Nombre: {linea}", end = "")
                        print(f"Telefono: {next(archivo)}", end = "")
                        print(f"Email: {next(archivo)}")
                        encontrado = True
                if not encontrado:
                    print(f"Contacto \"{nombre}\" no encontrado en la agenda")
                else:
                    print(f"{contador} contactos encontrados en la agenda")
        except Exception as e:
            print(f"Error al abrir o leer el archivo {e}")


    def eliminar_contacto(self, nombre):
        encontrado = False
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                for i, linea in enumerate(archivo):
                    if nombre.lower() in linea.lower():
                        print(f"Nombre: {linea}", end = "")
                        print(f"Telefono: {next(archivo)}", end = "")
                        print(f"Email: {next(archivo)}")
                        encontrado = True
                        break
                if not encontrado:
                    print(f"Contacto \"{nombre}\" no encontrado en la agenda")
                else:
                    print("¿Está seguro de querer eliminar el contacto?")
                    if input("Y | N") == "Y":
                        pass
                    else:
                        return
        except Exception as e:
            print(f"Error al abrir o leer el archivo {e}")


