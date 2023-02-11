from typing import *
from math import inf
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def sol(mat,dp,r,c):
            if r<0 or c<0 or c>=len(mat[0]):
                return inf

            if r==0 :
                return mat[r][c]

            if dp[r][c]!=-1 : return dp[r][c]

            up=mat[r][c]+sol(mat,dp,r-1,c)
            ld=mat[r][c]+sol(mat,dp,r-1,c-1)
            rd=mat[r][c]+sol(mat,dp,r-1,c+1)

            ans=min(up,ld,rd)                              # to find max falling path 
            dp[r][c]=ans                                   # change 'min' to 'max'  And  'inf' to '0-inf' :)

            return ans
        
        r=len(matrix)
        c=len(matrix[0])
        dp=[[-1 for i in range(c+1)] for j in range(r+1)]
        ans=inf
        for i in range(0,c):
            ans=min(ans,sol(matrix,dp,r-1,i))
        return ans
        


matrix = [[-19,57],[-40,-5]]
boj=Solution()
print(boj.minFallingPathSum(matrix=matrix))