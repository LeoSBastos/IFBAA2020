from random import sample
from random import seed
import sys

sys.setrecursionlimit(10**6)

def quickSort(lista, melhorCaso = False):
    menos = []
    listaPivos = []
    mais = []
    if len(lista) <= 1:
        return lista
    else:
        if melhorCaso:
            pivo = lista[len(lista)//2]
        else:
            pivo = lista[0]
        for i in lista:
            if i < pivo:
                menos.append(i)
            elif i > pivo:
                mais.append(i)
            else:
                listaPivos.append(i)
        return quickSort(menos, melhorCaso) + listaPivos + quickSort(mais, melhorCaso)


def popularEntradasAleatorias(ind):
    seed("1")
    entradas = []
    for i in range(ind):
        entradas.append(sample(range(-1000000, 1000000), 10 ** (i+1)))
    return entradas

def popularEntradasCasos(ind):
    entradas = []
    for i in range(ind):
        entradas.append([x for x in range(10 ** (i+1))])
    return entradas