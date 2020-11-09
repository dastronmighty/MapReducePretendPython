#!/opt/anaconda3/bin/python

import numpy as np

from MapReduce import MapReduce

class MatrixMultiplication(MapReduce):
    def __init__(self):
        super().__init__()
        pass

    def Map(self, v):
        """
        Code to split matrix parts in labeled parts
        """
        a = v[0]
        b = v[1]
        if len(a[0]) != len(b):
            raise RuntimeError("Not compatible")
        L, M, N = len(a), len(a[0]), len(b[0])
        for k in range(N):
            for i in range(L):
                for j in range(M):
                    self.emit((i, k), ("A", j, a[i][j]))
        for i in range(L):
            for j in range(M):
                for k in range(N):
                    self.emit((i, k), ("B", j, b[j][k]))

    def Reduce(self, k, v):
        #l ←length(tuples)/2 a vals ← array(0, l) b vals ← array(0, l)
        l = round(len(v)/2)
        a_vals = [0 for i in range(l)]
        b_vals = [0 for i in range(l)]

        for val in v:
            idx = val[1]
            if val[0] == "A":
                a_vals[idx] = val[2]
            else:
                b_vals[idx] = val[2]

        s = 0
        for i in range(l):
            s = s + (a_vals[i] * b_vals[i])
        self.emit(k, s)


A = np.loadtxt("./matA.txt",delimiter=",")
B = np.loadtxt("./matB.txt",delimiter=",")

"""
Run the Map reduce code with the Two matrices as input

Note: the run code will iterate through the input and since we want both matrices
to goto mat we wrap them as a tuple
in a list so then the tuple gets passed once to Map
"""
MatMul = MatrixMultiplication()
result = MatMul.run([(A, B)])

print(f"MapReduce Returned: {result}\n\n")

## THIS IS JUST A FANCY THING TO MAKE THE RESULTING MATRIX LOOK NICE
res_mat = [[0 for i in range(len(B[0]))] for j in range(len(A))]
for idx in list(result.keys()):
    res_mat[idx[0]][idx[1]] = result[idx][0]
res_mat = np.array(res_mat)
print(f"if we pop result into matrix we get:\n{res_mat}")
