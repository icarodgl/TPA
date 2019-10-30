import math
import heap as hs
import insertionsort as sl


def run(A):
    introsort(A)


def introsort(Lista):
    tamanho = len(Lista)
    depthLimit = math.floor(math.log(tamanho, 2))
    pivo = tamanho-1

    if tamanho < 16:
        sl.run(Lista)
        return
    if pivo > depthLimit:
        hs.run(Lista)
        return
    introsort(Lista[0:pivo])
    introsort(Lista[pivo+1:tamanho])