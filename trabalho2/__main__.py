import argparse
import time

from read import *
from knapsack import Knapsack

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Trabalho 2 de Análise de Algoritmo - Problema da Mochila")
    parser.add_argument(
        "inputFilename", metavar="INPUT_FILENAME", type=str, nargs="+", help="O nome do arquivo de entrada, e.g. entrada1.csv")
    parser.add_argument(
        "outputFilename", metavar="OUTPUT_FILENAME", type=str, nargs="+", help="O nome do arquivo de saída, e.g. saida1.txt"
    )
    args = parser.parse_args()
    file = Read(args.inputFilename[0])
    data = file.read()
    with open(args.outputFilename[0], "w") as file:
        for i, chunk in enumerate(data):
            print(f'Trabalhando no caso {i+1}')
            file.write(f"Teste de caso número {i+1}\n")
            knap = Knapsack(chunk)
            start_time = time.time()
            knap.allLights()
            file.write(
                f'Valor dos menores pesos e seu tempo: {knap.lightValue} ({time.time() - start_time})\n')
            start_time = time.time()
            knap.costBenefit()
            file.write(
                f'Valor dos melhores custo-benefícios e seu tempo: {knap.costBenefitValue} ({time.time() - start_time})\n')
            start_time = time.time()
            knap.dynamic()
            file.write(
                f'Valor do algoritmo dinâmico e seu tempo: {knap.optimizedValue} ({time.time() - start_time})\n')
            file.write("----------\n")
