from timeout import timeout


@timeout(900)
def run(V):
    timSort(V)


def timSort(vector):
    size = len(vector)
    n = 32
    s = n
    while s < size:
        for left in range(0, size, 2 * s):
            mid = left + s
            right = min((left + 2 * s), size)
            if s == n:
                insertion_Sort(vector, left, mid)
                insertion_Sort(vector, mid, right)
            merge(vector, left, mid, right)

        s = s * 2


def insertionSort(lista, l, r):
    r = min(r, len(lista) - 1)
    for i in range(l, r + 1):
        j = i
        while ((lista[j].uid < lista[j - 1].uid) and (j > 0)):
            aux = lista[j]
            lista[j] = lista[j - 1]
            lista[j - 1] = aux
            j = j - 1


def insertion_Sort(arr, left, right):
    right = min(right, len(arr) - 1)
    for i in range(left + 1, right + 1):
        temp = arr[i]
        j = i - 1
        while arr[j].uid > temp.uid and j >= left:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def merge(V, l, m, r):
    i = 0
    j = 0
    k = l
    L = V[l:m]
    R = V[m:r]
    l_L = len(L)
    l_R = len(R)

    while i < l_L and j < l_R:
        if L[i].uid < (R[j]).uid:
            V[k] = L[i]
            i += 1
        else:
            V[k] = R[j]
            j += 1
        k += 1

    while i < l_L:
        V[k] = L[i]
        i += 1
        k += 1
    while j < l_R:
        V[k] = R[j]
        j += 1
        k += 1
