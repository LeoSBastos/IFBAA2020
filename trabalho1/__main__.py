import time
import methods


if __name__ == "__main__":
    casoAleatorio = methods.popularEntradasAleatorias(6)
    piorCaso = melhorCaso = methods.popularEntradasCasos(6);
    for i in range(len(casoAleatorio)):
        start_time = time.time()
        casoAleatorio[i] = methods.quickSort(casoAleatorio[i])
        print("---Caso Aleatório[{}]: {:.4f} seconds ---".format(i+1,(time.time() - start_time)))
    start_time = time.time()   
    for i in range(len(piorCaso)):
        piorCaso[i] = methods.quickSort(piorCaso[i])
    print("---Pior Caso[{}]: ${:.4f} seconds ---" % (i+1,time.time() - start_time))
    start_time = time.time()   
    for i in range(len(melhorCaso)):
        melhorCaso[i] = methods.quickSort(melhorCaso[i], True)
    print("---Melhor Caso[{}]: ${:.4f} seconds ---" % (i+1,time.time() - start_time))