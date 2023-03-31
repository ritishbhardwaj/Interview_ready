from typing import *
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        n=len(mat)
        m=len(mat[0])

        vis=[[0 for i in range(m)] for j in range(n)]
        ans=[[-1 for i in range(m)] for j in range(n)]

        def bfs(grid,delrow,delcol):
            
            q=[]
            for r in range(n):
                for c in range(m):
                    if grid[r][c]==0:
                        q.append((r,c,0))
                        vis[r][c]=1
            while q:
                ini_node=q.pop(0)
                r=ini_node[0]
                c=ini_node[1]
                distance=ini_node[2]

                ans[r][c]=distance

                for i in range(4):
                    nrow=r+delrow[i]
                    ncol=c+delcol[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==0 :
                        q.append((nrow,ncol,distance+1))
                        vis[nrow][ncol]=1
            return ans

        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        ans=bfs(mat,delrow,delcol)

        return ans


obj=Solution()
mat = [[0,0,0],[0,1,0],[0,0,0]]
print(obj.updateMatrix(mat))
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(obj.updateMatrix(mat))