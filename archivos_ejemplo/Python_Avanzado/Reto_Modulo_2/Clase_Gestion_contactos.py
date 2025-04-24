from Python_Memos.archivos_ejemplo.Python_Avanzado.Reto_Modulo_2.Clase_Contactos import Contacto


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
                    nombre = ""
                    telefono = ""
                    email = ""
                    contador = 0
                    for linea in archivo:
                        if contador % 4 == 0:
                            nombre = linea.strip()
                        elif contador % 4 == 1:
                            telefono = linea.strip()
                        elif contador % 4 == 2:
                            email = linea.strip()
                            contacto = Contacto(nombre, telefono, email)
                            self.__agenda.append(contacto)
                        elif contador % 4 == 3:
                            pass
                        contador += 1
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
        self.__agenda.append(contacto)
        self.guardar_agenda()

    def mostrar_contactos(self):
        for contacto in self.get_agenda():
            print(contacto)
        print(f"Se encontraron {len(self.get_agenda())} contactos")

    def buscar_contacto(self, nombre):
        encontrado = False
        agenda = self.get_agenda()
        localizacion = []
        i = 0
        while i < len(agenda):
            contacto = agenda[i]
            if nombre.lower() in contacto.get_nombre().lower():
                localizacion.append(i)
                print(f"{len(localizacion)}:")
                print(contacto)
                encontrado = True
            i += 1
        if not encontrado:
            print(f"Contacto \"{nombre}\" no encontrado en la agenda")
        else:
            print(f"{len(localizacion)} contactos encontrados en la agenda")
            return localizacion

    def eliminar_contacto(self, nombre):
        localizacion = self.buscar_contacto(nombre)
        if len(localizacion) > 0:
            if len(localizacion) > 1:
                print("Ingrese el indice del contacto que desea eliminar")
                indice = int(input("Ingrese '0' para eliminar todas las coincidencias: "))
                while 0 > indice > len(localizacion):
                    indice = int(input("Ingrese un indice válido: "))
                if indice != 0:
                    localizacion_filtrada = [valor for valor in localizacion if valor == indice]
                    localizacion = localizacion_filtrada
                    print("¿Está seguro de querer eliminar el contacto?")
                else:
                    print("¿Está seguro de querer eliminar los contactos?")
            if input("Y | N: ").lower() == "y":
                agenda = self.get_agenda()
                i = 0
                contactos_filtrados = []
                while i < len(agenda):
                    if i not in localizacion:
                        contactos_filtrados.append(agenda[i])
                    i += 1  # Pasar a la siguiente línea
                self.set_agenda(contactos_filtrados)
                print(f"Se eliminó el contacto {nombre} de la agenda.")
                self.guardar_agenda()
        else:
            return

    def guardar_agenda(self):
        agenda = self.get_agenda()
        try:
            with open(self.get_nombreArchivo(), "w", encoding="utf-8") as archivo:
                for contacto in agenda:
                    archivo.write(str(contacto)+"\n")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")