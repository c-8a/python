class GestionContactos:

    def __init__(self):
        self.__nombre_archivo = "Agenda_Contactos.txt"
        self.__agenda = []
        try:
            with open(self.__nombre_archivo, "x", encoding="utf-8") as archivo:
                print(f"Se ha creado el archivo: {self.__nombre_archivo}")
        except FileExistsError as e:
            try:
                with open(self.__nombre_archivo, "r", encoding="utf-8") as archivo:
                    for linea in archivo:
                        self.__agenda.append(linea)
            except Exception as e:
                print(f"Error al leer la agenda: {e}")
        except Exception as e:
            print(f"Error al inicializar la agenda: {e}")

    def get_nombreArchivo(self):
        return self.__nombre_archivo

    def get_agenda(self):
        return self.__agenda

    def set_agenda(self, agenda):
        self.__agenda = agenda

    def agregar_contacto(self, contacto):
        self.__agenda.append(f"{contacto.get_nombre()}\n")
        self.__agenda.append(f"{contacto.get_telefono()}\n")
        self.__agenda.append(f"{contacto.get_email()}\n")
        self.__agenda.append("\n")

    def mostrar_contactos(self):
        contador = 0
        for linea in self.get_agenda():
            print(f"- {linea}", end="")
            linea_vacia = linea.strip()
            if not linea_vacia:
                contador += 1
        print(f"Se encontraron {contador} contactos")

    def buscar_contacto(self, nombre):
        encontrado = False
        agenda = self.get_agenda()
        localizacion = []
        i = 0
        while i < len(agenda):
            linea = agenda[i]
            if nombre.lower() in linea.lower():
                print(f"Nombre: {linea}", end="")
                print(f"Teléfono: {agenda[i+1]}", end="")
                print(f"Email: {agenda[i+2]}", end="")
                encontrado = True
                localizacion.append(i)
            i += 4
        if not encontrado:
            print(f"Contacto \"{nombre}\" no encontrado en la agenda")
        else:
            print(f"{len(localizacion)} contactos encontrados en la agenda")
            return localizacion

    def eliminar_contacto(self, nombre):
        localizacion = self.buscar_contacto(nombre)
        if len(localizacion) == 0:
            return
        elif len(localizacion) == 1:
            print("¿Está seguro de querer eliminar el contacto?")
            if input("Y | N: ").lower() == "y":
                agenda = self.get_agenda()
                i = 0
                lineas_filtradas = []
                while i < len(agenda):
                    if i not in localizacion:
                        lineas_filtradas.append(agenda[i])
                        i += 1  # Pasar a la siguiente línea
                    else:
                        i += 4  # Saltar las siguientes 4 líneas (incluida la actual)
                self.set_agenda(lineas_filtradas)
                print(f"Se eliminó el contacto {nombre} de la agenda.")
        else:
            print("Demasiados contactos encontrados, intente de nuevo")

    def guardar_agenda(self):
        try:
            with open(self.get_nombreArchivo(), "w", encoding="utf-8") as archivo:
                archivo.writelines(self.get_agenda())
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")