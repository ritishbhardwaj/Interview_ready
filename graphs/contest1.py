from typing import *
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        final=0
        maxi=0
        def dfs(r,c,grid,vis,tr,tc,val):
            nonlocal maxi
            vis[r][c]=1
            maxi+=val
            for ad in range(4):
                nr=r+tr[ad]
                nc=c+tc[ad]
                if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and vis[nr][nc]==0 and grid[nr][nc]!=0:
                    dfs(nr,nc,grid,vis,tr,tc,grid[nr][nc])
                
                
            
        
        
        vis=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        tr=[-1,0,1,0]
        tc=[0,1,0,-1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if vis[i][j]==0 and grid[i][j]!=0:
                    # vis(grid[i][j])=1
                    dfs(i,j,grid,vis,tr,tc,grid[i][j])
                    final=max(maxi,final)
                    maxi=0
        return final
    

obj=Solution()
print(obj.findMaxFish(grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))