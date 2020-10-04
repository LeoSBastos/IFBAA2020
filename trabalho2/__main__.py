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
        time_light = open("saidas/time_light.csv", "a")
        time_cost = open("saidas/time_cost.csv", "a")
        time_optimized = open("saidas/time_optimized.csv", "a")
        value_light = open("saidas/value_light.csv", "a")
        value_cost = open("saidas/value_cost.csv", "a")
        value_optimized = open("saidas/value_optimized.csv", "a")
        for i, chunk in enumerate(data):
            print(f'Trabalhando no caso {i+1}')
            file.write(f"Teste de caso número {i+1}\n")
            knap = Knapsack(chunk)
            start_time = time.time()
            knap.allLights()
            final_time = time.time() - start_time
            time_light.write(f"{final_time},")
            value_light.write(f"{knap.lightValue},")
            file.write(
                f'Valor dos menores pesos e seu tempo: {knap.lightValue} ({final_time})\n')
            start_time = time.time()
            knap.costBenefit()
            final_time = time.time() - start_time
            time_cost.write(f"{final_time},")
            value_cost.write(f"{knap.costBenefitValue},")
            file.write(
                f'Valor dos melhores custo-benefícios e seu tempo: {knap.costBenefitValue} ({final_time})\n')
            start_time = time.time()
            knap.dynamic()
            final_time = time.time() - start_time
            time_optimized.write(f"{final_time},")
            value_optimized.write(f"{knap.optimizedValue},")
            file.write(
                f'Valor do algoritmo dinâmico e seu tempo: {knap.optimizedValue} ({final_time})\n')
            file.write("----------\n")
        time_light.close()
        time_cost.close()
        time_optimized.close()
        value_light.close()
        value_cost.close()
        value_optimized.close()
