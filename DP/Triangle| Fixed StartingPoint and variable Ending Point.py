from typing import *

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        def sol(r,c,mat,dp):
            if r==len(mat)-1:
                return mat[r][c]
            if dp[r][c]!=-1:
                return dp[r][c]

            down=mat[r][c]+sol(r+1,c,mat,dp)
            diagnol=mat[r][c]+sol(r+1,c+1,mat,dp)

            ans=min(down,diagnol)
            dp[r][c]=ans
            return ans 

        #initially both row and column are (0,0)
        row=0
        col=0
        dp=[[-1 for i in range(len(triangle[-1])+1)] for j in range(len(triangle)+1)]
        ans=sol(row,col,triangle,dp)
        # return ans,'memoization'
        
        #======== TABULATION ==========
        
        
    

obj=Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# triangle = [[-10]]
print(obj.minimumTotal(triangle=triangle))