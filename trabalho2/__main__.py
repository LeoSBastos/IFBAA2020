from read import *
from knapsack import Knapsack
if __name__ == "__main__":
    file = Read("entradas/entrada1.csv")
    data = file.read()
    for chunk in data:
        knap = Knapsack(chunk)
        break
    knap.allLights()
    print(knap.lightIndexes)
