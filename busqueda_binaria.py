from array import array
def importar_lista(archivo):
    lista = []
    with open(archivo) as tf:
        lines = tf.read().split('","')
    for line in lines:
        lista.append(line)
    return lista

def buscar(lista, nombre_buscado):
    tamano_de_lista = len(lista)
    inicio = 0
    fin=tamano_de_lista-1
    while inicio<=fin:
        medio=(inicio+fin)//2
        if lista[medio] == nombre_buscado:
            return medio
        elif lista[medio] < nombre_buscado:
            inicio=medio+1
        elif lista[medio] > nombre_buscado:
            fin = medio-1
    return -1

def main():
    lista_de_alumnos = sorted(importar_lista('../data/lista_alumnos'))
    for i in range(0,3500):
        posicion_del_alumno = buscar(lista_de_alumnos, "Zoraida")
        print("Alumno(a) {} está en la posicion{}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))
if __name__ == "__main__":
    main()