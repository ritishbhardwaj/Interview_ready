from typing import *
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def sol(row,col,dp,obstacleGrid):
            if row>=0 and col>=0 and obstacleGrid[row][col]==1:
                return 0
            if row==0 and col==0:
                return 1
            # if row>=0 and col>=0 and obstacleGrid[row][col]==1:    # this statement should come above of the this one's above condition. because suppose if there is [[1]] then answer is 0 but here the answer comes out to be 1
            #     return 0
            if row<0 or col<0: 
                return 0
            if dp[row][col]!= -1: return dp[row][col]
            if row>=0:
                l=sol(row-1,col,dp,obstacleGrid)
            if col>=0:
                r=sol(row,col-1,dp,obstacleGrid)
            dp[row][col]=l+r
            return dp[row][col]
            # return l+r
        m=len(obstacleGrid) #m is basically rows
        n=len(obstacleGrid[0])  # n is basically columns
        dp=[[-1 for i in range(n)] for j in range(m)]
        # ans=sol(m-1,n-1,dp,obstacleGrid)
        # return ans
        
        #===========TABULATION ================
        dp=[[0 for i in range(n)] for j in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1: dp[i][j]=0
                elif i==0 and j==0: dp[i][j]=1
                else:
                    l,r=0,0
                    if i>0:
                        l=dp[i-1][j]
                    if j>0:
                        r=dp[i][j-1]
                    
                    dp[i][j]=l+r
        # return dp[m-1][n-1]      
        
        # =========== SPACE OPTIMIZATION ================
        prev=[0 for i in range(n+1)]
        curr=[0 for i in range(n+1)]
        for i in range(m):
            # curr=[0 for i in range(n+1)]
            for j in range(n):
                if obstacleGrid[i][j]==1: curr[j]=0
                elif i==0 and j==0: curr[j]=1
                else:
                    l,r=0,0
                    if i>0:
                        l=prev[j]
                    if j>0:
                        r=curr[j-1]
                    
                    curr[j]=l+r
            prev=curr[:]
        return prev[n-1],'space optimize'  
                   

obj=Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(obj.uniquePathsWithObstacles(obstacleGrid=obstacleGrid))