import methods


if __name__ == "__main__":
    casoAleatorio = methods.popularEntradas(6)
    #piorCaso = methods.readFile('piorCaso.txt');
    #melhorCaso = methods.readFile('melhorCaso.txt');
    for i in range(len(casoAleatorio)):
        casoAleatorio[i] = methods.quickSort(casoAleatorio[i])
        print(casoAleatorio[i])
    # for i in range(len(piorCaso)):
    #     piorCaso[i] = methods.quickSort(piorCaso[i])
    #     print(piorCaso[i])
    # for i in range(len(melhorCaso)):
    #     melhorCaso[i] = methods.quickSort(melhorCaso[i])
    #     print(melhorCaso[i])