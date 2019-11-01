import timeout


@timeout.timeout(900)
def run(V):
    insertionSort(V)


def insertionSort(lista):
    for i in range(1, len(lista)):
        j = i
        while ((lista[j].uid < lista[j - 1].uid) and (j > 0)):
            aux = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j = j - 1

    return lista

def insertion_Sort(arr):

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while arr[j].uid > temp.uid and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp