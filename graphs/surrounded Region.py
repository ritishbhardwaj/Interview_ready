from typing import *

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n=len(board)
        m=len(board[0])
        vis=[[0 for i in range(m)] for j in range(n)]

        def dfs(grid,row,col,delrow,delcol):
            vis[row][col]=1
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==0 and  grid[nrow][ncol]=='O':
                    dfs(grid,nrow,ncol,delrow,delcol)

        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]

        # EITHER USE THIS TO TRAVERSE OVER THE BOUNDARIES
        for j in range(m):
            if vis[0][j]==0 and board[0][j]=="O":
                dfs(board,0,j,delrow,delcol)
            if vis[n-1][j]==0 and board[n-1][j]=="O":
                dfs(board,0,j,delrow,delcol)
        for i in range(n):
            if vis[i][0]==0 and board[i][0]=="O":
                dfs(board,0,j,delrow,delcol)
            if vis[i][m-1]==0 and board[i][m-1]=="O":
                dfs(board,0,j,delrow,delcol)
        #or
        # USE THIS ONE TO TRAVERSE OVER THE BOUNDARIES(MINE ONE)
        for i in range(n):
            for j in range(m):
                if ((i==0) or (i==n-1) or (j==0) or (j==m-1)) and vis[i][j]==0 and board[i][j]=='O':
                    dfs(board,i,j,delrow,delcol) 
                    

        print(vis)
        for r in range(n):
            for c in range(m):
                if board[r][c]=='O' and vis[r][c]==0:
                    board[r][c]='X'
        return board



obj=Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
print(obj.solve(board))
# board = [["X"]]
# print(obj.solve(board))

print()
import math
a=math.gcd(18)
print(a)