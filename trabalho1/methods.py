from random import sample
from random import seed


def quickSort(lista, indicePivo = 0):
    menos = []
    listaPivos = []
    mais = []
    if len(lista) <= 1:
        return lista
    else:
        pivo = lista[indicePivo]
        for i in lista:
            if i < pivo:
                menos.append(i)
            elif i > pivo:
                mais.append(i)
            else:
                listaPivos.append(i)
        menos = quickSort(menos)
        mais = quickSort(mais)
        return menos + listaPivos + mais


def popularEntradas(ind):
    seed("1")
    entradas = []
    for i in range(ind):
        entradas.append(sample(range(-1000000, 1000000), 10 ** (i+1)))
    return entradas
