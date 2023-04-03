import sys
from typing import *
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0 for i in range(m)] for j in range(n)]

        def dfs(baseR,baseC,grid,vis,t:List,r,c):
            vis[r][c]=1
            t.append((r-baseR,c-baseC))

            delrow=[-1,0,1,0]
            delcol=[0,-1,0,1]

            for i in range(4):
                nrow=r+delrow[i]
                ncol=c+delcol[i]

                if  nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==0 and grid[nrow][ncol]==1:
                    dfs(baseR,baseC,grid,vis,t,nrow,ncol)


        s=set()
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]==1:
                    t=[]
                    dfs(i,j,grid,vis,t,i,j)
                    s.add(tuple(t))
        return len(s)





obj=Solution()
grid = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]
print(obj.countDistinctIslands(grid))

grid= [ [1, 1, 0, 1, 1],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 1]]
print(obj.countDistinctIslands(grid))