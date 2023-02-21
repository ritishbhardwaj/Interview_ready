import sys
from typing import *
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        m=len(cuts)    #original length of cuts
        cuts.append(n)
        cuts.append(0)
        cuts.sort()

        def sol(i,j,arr,dp):
            
            if i > j: return 0

            if dp[i][j]!=-1:
                return dp[i][j]

            mini=sys.maxsize
            for ind in range(i,j+1):
                cost=arr[j+1]-arr[i-1]+  sol(i,ind-1,arr,dp) + sol(ind+1,j,arr,dp)
                mini=min(cost,mini)

            dp[i][j]=mini
            
            return mini

        # dp=[[-1 for i in range(m+1)] for j in range(m+1)]
        # ans=sol(1,len(cuts)-2,cuts,dp)
        # return ans

        #=============== MEMOIZATION ==================

        dp=[[0 for i in range(m+2)] for j in range(m+2)]
        for i in range(m,0,-1):
            for j in range(1,m+1):
                if i>j :
                    continue
                mini=sys.maxsize
                for ind in range(i,j+1):
                    cost=cuts[j+1]-cuts[i-1]+  dp[i][ind-1] +dp[ind+1][j]
                    mini=min(cost,mini)
                dp[i][j]=mini

        return dp[1][len(cuts)-2]



obj=Solution()
ans=obj.minCost(n = 7, cuts = [1,3,4,5])
print(ans)
ans=obj.minCost(n = 9, cuts = [5,6,1,4,2])
print(ans)