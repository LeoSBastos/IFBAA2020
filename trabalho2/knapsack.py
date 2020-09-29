from queue import PriorityQueue


class Knapsack:
    def __init__(self, chunk):
        self.chunk = chunk
        self.knapsackSize = 10000
        self.lightQueue = PriorityQueue()
        self.costBenefitQueue = PriorityQueue()
        self.optimizedIndexes = []
        self.lightIndexes = []
        self.costBenefitIndexes = []
        self.optimizedWeight = 0
        for r in self.chunk.itertuples():
            self.lightQueue.put((r[3], r[1]))
            self.costBenefitQueue.put((-1*(r[2]/r[3]), (r[3], r[1])))

    def allLights(self):
        knapsackSizeLeft = self.knapsackSize
        while knapsackSizeLeft > 0:
            weigth, index = self.lightQueue.get()
            if (knapsackSizeLeft - weigth) < 0:
                break
            self.lightIndexes.append(index)
            knapsackSizeLeft -= weigth

    def costBenefit(self):
        knapsackSizeLeft = self.knapsackSize
        while not self.costBenefitQueue.empty():
            if knapsackSizeLeft == 0:
                break
            value, (weigth, index) = self.costBenefitQueue.get()
            if (knapsackSizeLeft - weigth) < 0:
                continue
            self.costBenefitIndexes.append(index)
            knapsackSizeLeft -= weigth

    def dynamic(self):
        return
