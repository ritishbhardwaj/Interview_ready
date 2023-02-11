from functools import *
from typing import *
import math
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        def sol(i,j1,j2,grid,dp):
            if j1<0 or j2<0 or j1>=m or j2>=m:
                return 0-math.inf
            if i==n-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            if dp[i][j1][j2]!= -1: return dp[i][j1][j2]
            directions=[-1,0,1]
            maxi=0-math.inf
            for dir1 in directions:
                for dir2 in directions:
                    if j1==j2:
                        val=grid[i][j1]
                    else:
                        val=grid[i][j1]+grid[i][j2]
                    val= val+sol(i+1,j1+dir1,j2+dir2,grid,dp)
                    maxi=max(maxi,val)  
                    dp[i][j1][j2]=maxi     
            return maxi
        m=len(grid[0])  # total columns
        n=len(grid)    # total rows
        dp=[[[-1 for i in range(m)] for j in range(m)] for k in range(n)]
        ans=sol(0,0,m-1,grid,dp)
        return ans


# def sol(i,j1,j2,grid,dp):
#         if j1<0 or j2<0 or j1>=m or j2>=m:
#             return 0-math.inf
#         if i==n-1:
#             if j1==j2:
#                 return grid[i][j1]
#             else:
#                 return grid[i][j1]+grid[i][j2]
#         # if dp[i][j1][j2]!= -1: return dp[i][j1][j2]
#         directions=[-1,0,1]
#         maxi=0-math.inf
#         for dir1 in directions:
#             for dir2 in directions:
#                 if j1==j2:
#                     val=grid[i][j1]
#                 else:
#                     val=grid[i][j1]+grid[i][j2]
#                 val= val+sol(i+1,j1+dir1,j2+dir2,grid,dp)
#                 maxi=max(maxi,val)  
#                 # dp[i][j1][j2]=maxi     
#         return maxi
        
grid = [[8,8,10,9,1,7],[8,8,1,8,4,7],[8,6,10,3,7,7],[3,0,9,3,2,7],[6,8,9,4,2,5],[1,1,5,8,8,1],[5,6,5,2,9,9],[4,4,6,2,5,4],[4,4,5,3,1,6],[9,2,2,1,9,3]]

obj=Solution()
print(obj.cherryPickup(grid=grid))
# m=len(grid[0])  # total columns
# n=len(grid)    # total rows
# dp=[[[-1 for i in range(m)] for j in range(m)] for k in range(n)]
# ans=sol(0,0,m-1,grid,dp)
# print(ans)