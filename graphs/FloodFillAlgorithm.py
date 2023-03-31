import copy
from typing import *
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        newImagegrid=copy.deepcopy(image)
        n=len(newImagegrid)
        m=len(newImagegrid[0])

        vis=[[0 for i in range(m)] for j in range(n)]

        def dfs(grid,sr,sc,oldColor,newColor,delrow,delcol):
            
            vis[sr][sc]=1
            grid[sr][sc]=newColor
            for i in range(4):
                nrow=sr+ delrow[i]
                ncol=sc+delcol[i]

                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and grid[nrow][ncol]==oldColor and vis[nrow][ncol]==0:
                    dfs(grid,nrow,ncol,oldColor,newColor,delrow,delcol)
        
        oldColor=newImagegrid[sr][sc]
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        dfs(newImagegrid,sr,sc,oldColor,color,delrow,delcol)

        image=newImagegrid
        return image


image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
color = 2
obj=Solution()
print(obj.floodFill(image,sr,sc,color))


image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
color = 0
print(obj.floodFill(image,sr,sc,color))