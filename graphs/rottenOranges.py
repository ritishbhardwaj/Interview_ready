from typing import *
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        n=len(grid)   # n represents row
        m=len(grid[0])  # m represents col

        vis=[[0]*m for i in range(n)]
        q=deque([])
        cnt_Fresh=0
        for i in range(n):
            for j in range(m):

                if grid[i][j]==2:
                    vis[i][j]=2
                    q.append(((i,j),0))
                
                if grid[i][j]==1:
                    cnt_Fresh+=1
        
        tm=0    #time
        drow=[-1,0,1,0]
        dcol=[0,1,0,-1]
        cnt=0

        #bfs traversal
        while q:
            r=q[0][0][0]
            c=q[0][0][1]
            t=q[0][1]
            tm=max(tm,t)
            q.popleft()

            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]

                if (nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==0 and grid[nrow][ncol]==1):
                    q.append(((nrow,ncol),t+1))
                    vis[nrow][ncol]==2
                    cnt+=1
        if cnt!=cnt_Fresh:
            return -1
        return tm

obj=Solution()
ans=obj.orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]])
print(ans)
# ans=obj.orangesRotting(grid = [[2,1,1],[0,1,1],[1,0,1]])
# print(ans)
# ans=obj.orangesRotting(grid = [[0,2]])
# print(ans)