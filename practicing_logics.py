from typing import *
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts.insert(0,0)
        cuts.append(n)
        
        def solve(i,j,arr,dp):
            if i>j:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]

            mini=float("inf")
            for k in range(i,j+1):
                score=arr[j+1]-arr[i-1] + solve(i,k-1,arr,dp)+ solve(k+1,j,arr,dp)
                mini=min(mini,score)
            
            dp[i][j]=mini
            return mini

        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        ans=solve(1,len(cuts)-2,cuts,dp)
        print(ans)
        return ans

obj=Solution()
obj.minCost( n = 9, cuts = [5,6,1,4,2])
obj.minCost(n = 7, cuts = [1,3,4,5])

'''   _ _ _ _ _ _ _ _ _   '''
'''  |_|_|_|_|_|_|_|_|_|  '''