from typing import *
class NumMatrix:

    def __init__(self, matrix:List[List]):
        self.matrix = matrix
        matrix.insert(0, [0 for _ in range(len(matrix[0]))])    
        for row in matrix:
            row.insert(0, 0)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.matrix[row1 - 1][col1 - 1] + self.matrix[row2][col2] - self.matrix[row2][col1 - 1] - self.matrix[row1 - 1][col2]


# Your NumMatrix object will be instantiated and called as such:

obj = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
queries=[[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
for q in queries:
    print(obj.sumRegion(q[0],q[1],q[2],q[3]))
# matrix=[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# n=len(matrix)
# m=len(matrix[0])
# ref=[[0 for i in range(m)]]
# matrix=ref+matrix
# a=[[1,2,3]]
# b=[[4,5,6]]
# print(matrix)