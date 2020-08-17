import methods


if __name__ == "__main__":
    entradas = methods.popularEntradas(6)
    for i, ent in enumerate(entradas):
        entradas[i] = methods.quickSort(ent)
        print(entradas[i])
