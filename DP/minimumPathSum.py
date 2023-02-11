from sys import maxsize
from typing import *
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        def f(row,col,mat,dp):
            if row==0 and col==0:
                return mat[0][0]
            if row<0 or col<0 :
                return maxsize
            if dp[row][col]!= -1 : return dp[row][col]
            up=mat[row][col]+ f(row-1,col,mat,dp)
            left=mat[row][col]+ f(row,col-1,mat,dp)

            ans=min(up,left)
            dp[row][col]=ans
            return ans
            
        row=len(grid)
        col=len(grid[0])
        dp=[[-1 for i in range(col)] for j in range(row)]
        ans=f(row-1,col-1,grid,dp)
        return ans

obj=Solution()
grid = [[1,2,3],[4,5,6]]
ans=(obj.minPathSum(grid=grid))
print(ans)