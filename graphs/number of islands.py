from typing import *
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        n=len(grid)
        m=len(grid[0])
        cnt=0

        vis=[[0 for i in range(m)] for j in range(n)]

        def bfs(row,col):
            q=[]
            start_coord=(row,col)
            q.append(start_coord)
            vis[row][col]=1

            while q:
                node_c = q.pop(0)
                r,c=node_c[0],node_c[1]

                drow=[-1,0,1]
                dcol=[-1,0,1]

                for delrow in drow:
                    for delcol in dcol:
                        if (delrow==1 and delcol==-1) or (delrow==-1 and delcol==-1) or (delrow==1 and delcol==1) or (delrow==-1 and delcol==1):
                            continue
                        n_row=r+delrow
                        n_col=c+delcol
                        if n_row>=0 and n_row<n and n_col>=0 and n_col<m and  grid[n_row][n_col]=='1' and vis[n_row][n_col]==0:
                            vis[n_row][n_col]=1
                            q.append((n_row,n_col))



        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]=='1':
                    bfs(i,j)
                    cnt+=1
        return cnt

obj=Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
# ans=obj.numIslands(grid)
# print(ans)
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# grid=[[0,1],
#       [1,0],
#       [1,1],
#       [1,0]]
ans=obj.numIslands(grid)
print(ans)