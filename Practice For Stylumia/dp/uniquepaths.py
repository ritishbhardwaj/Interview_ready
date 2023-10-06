from typing import *

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:      # m: rows    n: columns


        def sol(row,col,dp):
            
            if row==0 and col==0:
                return 1
            
            if row<0 or col<0:
                return 0
            if dp[row][col]!=-1:return dp[row][col]
            up=sol(row-1,col,dp)
            left=sol(row,col-1,dp)

            res=up+left
            dp[row][col]=res
            return res

        dp=[[-1 for i in range(n+2)] for j in range(m+2)]
        ans=sol(m-1,n-1,dp)
        return ans
        

obj=Solution()
print(obj.uniquePaths(3,7))
print(obj.uniquePaths(3,2))