import numpy as np
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        p=len(matrix)
        f=len(matrix[0])
        zero_matrix = [[0]*p for _ in range(f)]
        for i in range(f):
            for j in range(p):
                zero_matrix[i][j]=matrix[j][i]
        return zero_matrix
