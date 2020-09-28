import pandas as pd


class Read:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        data = pd.read_csv(self.filename, sep=",", header=None, names=[
                           "Index", "Value", "Weight", "Optimized"], chunksize=1000)
        return data
