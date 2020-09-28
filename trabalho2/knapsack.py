from queue import PriorityQueue


class Knapsack:
    def __init__(self, chunk):
        self.chunk = chunk
        self.lightQueue = PriorityQueue()
        self.costBenefitQueue = PriorityQueue()
        for r in self.chunk.itertuples():
            self.lightQueue.put((r[3], r[1]))
            self.costBenefitQueue.put((-1*(r[2]/r[3]), r[1]))
        self.optimizedIndexes = []
        for r in self.chunk:
            if r[4] == 1:
                self.optimizedIndexes.append(r[1])
        self.lightIndexes = []
        self.knapsackSize = 10000

    def allLights(self):
        knapsackSizeLeft = self.knapsackSize
        while knapsackSizeLeft > 0:
            weigth, index = self.lightQueue.get()
            if (knapsackSizeLeft - weigth) < 0:
                break
            self.lightIndexes.append(index)
            knapsackSizeLeft -= weigth
