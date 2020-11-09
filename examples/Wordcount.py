#!/opt/anaconda3/bin/python
from MapReduce import MapReduce

class WCMR(MapReduce):
    def __init__(self):
        super().__init__()
        pass

    def Map(self, v):
        line = v.strip()
        line = line.lower()
        # split the line into words
        words = line.split()
        # increase counters
        for word in words:
            self.emit(word, 1)

    def Reduce(self, k, v):
        total = 0
        for val in v:
            total+=val
        self.emit(k, total)

wcMR = WCMR()
with open("./test.txt") as f:
    result = wcMR.run(f.readlines())
print(result)
