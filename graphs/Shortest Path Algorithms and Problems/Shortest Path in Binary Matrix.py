from sys import maxsize as maxx
from typing import *
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        q=[]
        print(n,m)
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        if grid[0][0]==1:
            return -1
        q.append((0,0,0))

        distGrid=[[maxx for i in range(len(grid[0]))] for j in range(len(grid))]
        distGrid[0][0]=0
        flag=True
        while q and flag:
            query=q.pop(0)
            dis=query[0]
            row=query[1]
            col=query[2]

            for r in delrow:
                for c in delcol:
                    nr=row+r
                    nc=col+c
                    if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and grid[nr][nc]==0 and dis+1<distGrid[nr][nc]:
                        distGrid[nr][nc]=dis+1
                        if nr==len(grid) and nc==len(grid[0]):
                            return dis+1
                        q.append((dis+1,nr,nc))
                        
        return distGrid[n-1][m-1]+1 if distGrid[n-1][m-1]!=maxx else -1

    


obj=Solution()
grid = [[0,1],[1,0]]
print(obj.shortestPathBinaryMatrix(grid))
print(obj.shortestPathBinaryMatrix(grid = [[0,0,0],[1,1,0],[1,1,0]]))
print(obj.shortestPathBinaryMatrix(grid = [[1,0,0],[1,1,0],[1,1,0]]))