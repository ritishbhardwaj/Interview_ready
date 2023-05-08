from typing import *


'''Leetcode Problem'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        '''Method I    O(2*n*m)'''
        row=[]
        col=[]
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    col.append(j)
                    row.append(i)
        for i in range(n):
            for j in range(m):
                if (i in row) or (j in col):
                    matrix[i][j]=0

        '''Method II '''


        for i in matrix:
            print(*i)
        print()
        


obj=Solution()
obj.setZeroes(matrix = [[1,1,1],[1,0,1],[1,1,1]])
obj.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]])