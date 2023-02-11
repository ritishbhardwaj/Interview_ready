from math import *
from typing import *
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        def sol(ind,N,arr,dp):
            if ind==0:
                return N*arr[0]
            
            if dp[ind][N]!=-1: return dp[ind][N]
            not_take=0+sol(ind-1,N,arr,dp)
            take=-inf
            rodLength=ind+1
            if rodLength<=N and N!=0:
                take=cuts[ind]+sol(ind,N-rodLength,arr,dp)

            ans=max(take,not_take)
            dp[ind][N]=ans
            return ans
        
        # n is also rod ki length
        l=len(cuts)
        dp=[[-1 for i in range(n+2)] for j in range(n+1)]
        ans=sol(l-1,n,cuts,dp)
        print(ans)
        return ans



obj=Solution()
n = 5
cuts = [2,5,7,8,10]
ans=obj.minCost(n,cuts)
print(ans)
