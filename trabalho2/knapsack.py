from queue import PriorityQueue


class Knapsack:
    def __init__(self, chunk):
        self.chunk = chunk
        self.knapsackSize = 10000
        self.objectSize = 1000
        self.lightQueue = PriorityQueue()
        self.costBenefitQueue = PriorityQueue()
        self.lightValue = 0
        self.costBenefitValue = 0
        self.optimizedValue = 0
        self.weights = []
        self.values = []

    def allLights(self):
        for r in self.chunk.itertuples():
            self.lightQueue.put((r[3], r[2]))
        knapsackSizeLeft = self.knapsackSize
        while not self.lightQueue.empty():
            weigth, value = self.lightQueue.get()
            if (knapsackSizeLeft - weigth) < 0:
                continue
            self.lightValue += value
            knapsackSizeLeft -= weigth

    def costBenefit(self):
        for r in self.chunk.itertuples():
            self.costBenefitQueue.put((-1*(r[2]/r[3]), (r[3], r[2])))
        knapsackSizeLeft = self.knapsackSize
        while not self.costBenefitQueue.empty():
            costBenefitValue, (weigth, value) = self.costBenefitQueue.get()
            if (knapsackSizeLeft - weigth) <= 0:
                continue
            self.costBenefitValue += value
            knapsackSizeLeft -= weigth

    def dynamic(self):
        for r in self.chunk.itertuples():
            self.weights.append(r[3])
            self.values.append(r[2])
        matrix = [[0 for x in range(self.knapsackSize+1)]
                  for m in range(self.objectSize+1)]
        for i in range(1, self.objectSize+1):
            for j in range(1, self.knapsackSize+1):
                if(self.weights[i-1] <= j):
                    if(self.values[i-1] +
                       matrix[i-1][j-self.weights[i-1]] > matrix[i - 1][j]):
                        matrix[i][j] = self.values[i - 1] + \
                            matrix[i - 1][j - self.weights[i - 1]]
                    else:
                        matrix[i][j] = matrix[i - 1][j]
                else:
                    matrix[i][j] = matrix[i-1][j]
        self.optimizedValue = matrix[self.objectSize][self.knapsackSize]
