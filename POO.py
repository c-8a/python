#Ejemplo de programación estructurada
# Definimos unos cuantos clientes

clientes= [
    {'Nombre': 'Hector',
    'Apellidos':'Costa Guzman',
    'dni':'11111111A'},
    {'Nombre': 'Juan',
    'Apellidos':'González Márquez',
    'dni':'22222222B'}
]

# Creamos una función que muestra un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'],c['Apellidos']))
            return
    
    print('Cliente no encontrado')

# Creamos una función que borra un cliente en una lista a partir del DNI
def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes):
        if (dni == c['dni']):
            del( clientes[i] )
            print(str(c),"> BORRADO")
            return
    print('Cliente no encontrado')

### Fíjate muy bien cómo se utiliza el código estructurado
print("==LISTADO DE CLIENTES==")
print(clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
mostrar_cliente(clientes, '11111111A')
mostrar_cliente(clientes, '11111111Z')

print("\n==BORRAR CLIENTES POR DNI==")
borrar_cliente(clientes, '22222222V')
borrar_cliente(clientes, '22222222B')

print("\n==LISTADO DE CLIENTES==")
print(clientes)






###Ejemplo orientado a objetos
### No intentes entender este código, sólo fíjate en cómo se utiliza abajo
# Creo una estructura para los clientes

class Cliente:
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

# Y otra para las empresas
class Empresa:
    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

### Ahora utilizaré ambas estructuras
# Creo un par de clientes
hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")

# Creo una empresa con los clientes iniciales
empresa = Empresa(clientes=[hector, juan])

# Muestro todos los clientes
print("==LISTADO DE CLIENTES==")
print(empresa.clientes)

print("\n==MOSTRAR CLIENTES POR DNI==")
# Consulto clientes por DNI
empresa.mostrar_cliente("11111111A")
empresa.mostrar_cliente("11111111Z")
print("\n==BORRAR CLIENTES POR DNI==")

# Borro un cliente por DNI
empresa.borrar_cliente("22222222V")
empresa.borrar_cliente("22222222B")

# Muestro de nuevo todos los clientes
print("\n==LISTADO DE CLIENTES==")
print(empresa.clientes)



class CocheMemita():
    # Declaración de atributos
    largo = 250
    ancho = 120
    ruedas = 4
    peso = 900
    color = "rojo"
    is_enMarcha = False

    # Declaración de métodos
    def arrancar(self): # self hace referencia a la instancia de clase.
        self.is_enMarcha = True # Es como si pusiésemos miCoche.is_enMarcha = True

    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"


# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche = CocheMemita()
miCoche2 = CocheMemita()

# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
print("El largo del coche es de", miCoche.largo, "cm.")
miCoche.arrancar()
print(miCoche.estado())

# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("El coche está arrancado:", miCoche.arrancar())

# Modificamos el valor de una propiedad
miCoche2.ruedas = 10
print("El coche2 tiene:" ,
miCoche2.ruedas, "ruedas.")




# CREACIÓN DE LA CLASE
class Usuario():

    # Declaración de atributos
    nombre = "Angel"
    edad = 47
    login = "admin"
    password = "1234"
    email = "angel@loquesea.com"
    telefono = 666666666

    # Declaración de métodos
    def resumen(self): # self hace referencia a la instancia de clase.
        print(f'Los datos del usuario son:\n'
            f'Nombre: {self.nombre}\n'
            f'Edad: {self.edad}\n'
            f'Login: {self.login}\n'
            f'Password: {self.password}\n'
            f'Email: {self.email}\n'
            f'Teléfono: {self.telefono}')
        
    def cambiaEdad(self):
        edadIntroducida = int(input("Introduce edad entre 18-100:"))
        if 18 < edadIntroducida < 100:
            self.edad = edadIntroducida
            print("Edad introducida correcta")
            return ""
        else:
            print("La edad introducida no es correcta.")
            self.cambiaEdad()
            return ""
        
    def muestraEdad(self):
        print('La edad del usuario es:', self.edad, 'años.')
        return ""

# Creación de una instancia de la clase Usuario a la que llamaremos administrador
administrador = Usuario()

 # Una vez creado el objeto administrador, hacemos uso del método “resumen()” perteneciente a la clase Usuario
administrador.resumen()

# Usamos los métodos cambiaEdad() y muestraEdad() de la clase Usuario.
print(administrador.cambiaEdad())
print(administrador.muestraEdad())

# Creación de la clase Coche
class Coche():
    # Declaración del constructor de la clase Coche
    def __init__(self):
        self.largo = 250
        self.ancho = 120
        self.ruedas = 4
        self.peso = 900
        self.color = "rojo"
        self.is_enMarcha = False

# Declaración de métodos
    def arrancar(self): #self hace referencia a la instancia de clase.
        self.is_enMarcha = True #Es como si pusiésemos miCoche.is_enMarcha = True
    def estado(self):
        if (self.is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"
    def __del__(self):
        print("Acabas de llamar al método destructor. El objeto acaba de ser eliminado")
        
# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
coche_1 = Coche()

# Acceso a un atributo de la clase Coche. Nomenclatura del punto.
coche_1.ruedas = 7
print("El largo del coche es de" , coche_1.largo, "cm.")
coche_1.arrancar()
print(coche_1.estado())

# Acceso a un método de la clase Coche. Nomenclatura del punto.
print("El coche está arrancado:" , coche_1.arrancar())



###Herencia

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.color = "Negro"
        self.arrancado = False
        self.parado = True

    def arrancar(self):
        self.arrancado = True
        self.parado = False
    
    def parar(self):
        self.parado = True
        self.arrancado = False
    
    def resumen(self):
        print("Marca:", self.marca, "\n", 
                "Modelo:", self.modelo, "\n",
                "Color:", self.color, "\n",
                "Está arrancado:", self.arrancado,"\n",
                "Está parado:", self.parado
                )

miCoche = Vehiculo("Renault", "Megane")
miCoche.arrancar()
miCoche.resumen()

#class Moto(Vehiculo):
#    pass

#miMoto = Moto("Kawasaki", "Ninja")
#miMoto.resumen()


# Clase "Nieta"
class Moto(Vehiculo):
    is_carenado = False
#Método propio de la clase Moto, no heredado del padre.
    def poner_carenado(self):
        self.is_carenado = True
#La clase Moto sobrescribe el método resumen() heredado del padre
    def resumen(self):
        print("El modelo es una moto", "\n",
            "Marca:", self.marca, "\n",
            "Modelo:", self.modelo, "\n",
            "Color:", self.color, "\n",
            "Está arrancado:", self.arrancado,"\n",
            "Está parado:", self.parado, "\n",
            "Tiene carenado:", self.is_carenado
        )
    
miMoto = Moto("Kawasaki", "Ninja")
miMoto.resumen()

class kwad(Moto):
    pass

miKwad = kwad("Linhai", "LH 500")
miKwad.resumen()



class Persona():
    
    def __init__(self, nombre, edad, lugar):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar
    
    def descripcion(self):
        print("El nombre es ", self.nombre, ", tiene ", self.edad, " anyos", " y es de ", self.lugar)

class Empleado(Persona):
    
    def __init__(self, salario, antiguedad, nombre_emp, edad_emp, lugar_epm):
        super().__init__(nombre_emp, edad_emp, lugar_epm)
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, ", antiguedad: ", self.antiguedad)

Angel=Persona("Angel", 43, "Malaga")
Angel.descripcion()

Empleado1=Empleado(2000, 2017, "Manolo", 33, "Madrid")
Empleado1.descripcion()

    
###Jerarquía de clases sin usar super(), sobrescribiendo los atributos del padre:

class Padre(): #Creamos la clase Padre
    def __init__(self, ojos, cejas): #Definimos los Atributos en el constructor de la clase
        self.ojos = ojos
        self.cejas = cejas

class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #Definimos los atributos en el constructor
        self.ojos = ojos #Sobreescribimos cada atributo
        self.cejas = cejas
        self.cara = cara #Especificamo el nuevo atributo para Hijo

Tomas = Hijo('Marrones', 'Negras', 'Larga') #Instanciamos
print (Tomas.ojos, Tomas.cejas, Tomas.cara) #Imprimimos los atributos del objeto


### Encapsulacion

class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."
    
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()



class Coche:
# Método constructor
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False

# Declaración de métodos
    def arrancar(self): # self hace referencia a la instancia de clase.
        self.__is_enMarcha = True # Es como si pusiésemos miCoche.is_enMarcha = True

    def estado(self):
        if (self.__is_enMarcha == True):
            return "El coche está arrancado"
        else:
            return "El coche está parado"

# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.
miCoche = Coche()
miCoche.__ruedas = 9
print("Mi coche tiene", miCoche.__ruedas, "ruedas.")


### Polimorfismo

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'
# def mostrar_detalles(self):
# return self.__str__()
    
def imprimir_detalles(objeto):
# print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)
gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)




class Animal:
    def hacer_sonido(self):
        pass  # Método vacío, se sobrescribirá en las subclases

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Muu"

# Función que demuestra el polimorfismo
def escuchar_animal(animal):
    return animal.hacer_sonido()

# Crear objetos de diferentes animales
mi_perro = Perro()
mi_gato = Gato()
mi_vaca = Vaca()

# Llamar a la función con diferentes objetos
print(escuchar_animal(mi_perro))  # Salida: Guau
print(escuchar_animal(mi_gato))  # Salida: Miau
print(escuchar_animal(mi_vaca))  # Salida: Muu

#otra forma de hacerlo
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    print(animal.hacer_sonido())