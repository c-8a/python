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
        print("Alumno(a) {} está en la posicion {}".format(lista_de_alumnos[posicion_del_alumno], posicion_del_alumno))
if __name__ == "__main__":
    main()


#Algoritmos de clasificación
#insertion sort
def insertion_sort(arr, n):
    for i in range(1, n): ## posición actual y elemento
        current_position = i
        current_element = arr[i] 
## iterar hasta llega al primer elemento o
## el elemento actual es más pequeño que el elemento anterior
        while current_position > 0 and current_element < arr[current_position - 1]:
## actualizar el elemento actual con el elemento anterior
            arr[current_position] = arr[current_position - 1]
## moviéndose a la posición anterior
            current_position -= 1
## actualizar el elemento de posición actual
        arr[current_position] = current_element

#if __name__ == '__main__':
## inicialización del array
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
insertion_sort(arr, 9)
## imprimiendo el array
print(str(arr))


#selection sort
def selection_sort(arr, n):
    for i in range(n):
## para almacenar el índice del elemento mínimo
        min_element_index = i
        for j in range(i + 1, n): # para i=0; [1, 2, 3, 4, 5, 6, 7, 8]
## comprobando y reemplazando el índice mínimo del elemento
            if arr[j] < arr[min_element_index]: 
                min_element_index = j
## intercambiando el elemento actual con el elemento mínimo
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]

#if __name__ == '__main__':
## inicialización del array
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
selection_sort(arr, 9)
## imprimiendo el array
print(str(arr))


#Bubble Sort
def bubble_sort(arr, n):
    for i in range(n): # n=9; [0, 1, 2, 3, 4, 5, 6, 7, 8]
## iterando de 0 a n-i-1 ya que los últimos i elementos ya están ordenados
        for j in range(n - i - 1): #9-0-1 = 8 [0, 1, 2, 3, 4, 5, 6, 7]
## comprobando el siguiente elemento
            if arr[j] > arr[j + 1]:
## intercambiando los elementos adyacentes
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

#if __name__ == '__main__':
## inicialización del array
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
bubble_sort(arr, 9)
## imprimiendo el array
print(str(arr))


#Merge Sort

def merge(arr, left_index, mid_index, right_index):
## matrices izquierda y derecha
    left_array = arr[left_index:mid_index+1]
    right_array = arr[mid_index+1:right_index+1]
## obtener las longitudes de matriz izquierda y derecha
    left_array_length = mid_index - left_index + 1
    right_array_length = right_index - mid_index
## índices para fusionar dos matrices
    i = j = 0
## índice para el reemplazo de elementos de matriz
    k = left_index
## iterando sobre las dos submatrices
    while i < left_array_length and j < right_array_length:
## comparar los elementos de las matrices izquierda y derecha
        if left_array[i] < right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1
## agregando elementos restantes de las matrices izquierda y derecha
    while i < left_array_length:
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < right_array_length:
        arr[k] = right_array[j]
        j += 1
        k += 1

def merge_sort(arr, left_index, right_index):
## caso base para función recursiva
    if left_index >= right_index:
        return
    ## encontrar el índice medio
    mid_index = (left_index + right_index) // 2
    ## llamadas recursivas
    merge_sort(arr, left_index, mid_index)
    merge_sort(arr, mid_index + 1, right_index)
    ## fusionando las dos sub-matrices
    merge(arr, left_index, mid_index, right_index)

#if __name__ == '__main__':
## inicialización de matriz
arr = [3, 4, 7, 8, 1, 9, 5, 2, 6]
merge_sort(arr, 0, 8)
## imprimiendo la matriz
print(str(arr))