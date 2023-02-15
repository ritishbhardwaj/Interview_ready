from typing import *
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        n=len(prices)
        #================ MEMOIZATION =================
        def sol(ind,buy,n,arr,dp):
            if ind >= n:
                return 0
            
            if dp[ind][buy]!=-1: return dp[ind][buy]
            if buy:
                profit=max(-arr[ind]+sol(ind+1,0,n,arr,dp), 0+sol(ind+1,1,n,arr,dp))
            else:
                profit=max(arr[ind]-fee+sol(ind+1,1,n,arr,dp), 0+sol(ind+1,0,n,arr,dp))

            dp[ind][buy]=profit
            return profit

        dp=[[-1 for i in range(2)] for j in range(n+1)]
        ans=sol(0,1,n,prices,dp)
        print(ans)
        return ans

obj=Solution()
obj.maxProfit(prices = [1,3,2,8,4,9], fee = 2)
obj.maxProfit(prices = [1,3,7,5,10,3], fee = 3)