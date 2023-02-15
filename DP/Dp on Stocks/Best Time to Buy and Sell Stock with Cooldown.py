from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        #================ MEMOIZATION =================
        def sol(ind,buy,n,arr,dp):
            if ind >= n:
                return 0
            
            if dp[ind][buy]!=-1: return dp[ind][buy]
            if buy:
                profit=max(-arr[ind]+sol(ind+1,0,n,arr,dp), 0+sol(ind+1,1,n,arr,dp))
            else:
                profit=max(arr[ind]+sol(ind+2,1,n,arr,dp), 0+sol(ind+1,0,n,arr,dp))

            dp[ind][buy]=profit
            return profit

        dp=[[-1 for i in range(2)] for j in range(n+1)]
        ans=sol(0,1,n,prices,dp)
        print(ans)
        return ans
        # TC=2^n    SC= O(n)

        #================== TABULATION ===================
        dp=[[0 for i in range(2)] for j in range(n+1)]
        for i in range(2):
            dp[n][i]=0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    profit=max(-prices[ind]+dp[ind+1][0], 0+dp[ind+1][1])
                else:
                    profit=max(prices[ind]+dp[ind+1][1], 0+dp[ind+1][0])

                dp[ind][buy]=profit
        print(dp[0][1])
        # return dp[0][1]

        # =========== Space Optimize ===============
        ahead=[0 for i in range(2)]
        curr=[0 for i in range(2)]
        ahead[0],ahead[1]=0,0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if buy:
                    profit=max(-prices[ind]+ahead[0], 0+ahead[1])
                else:
                    profit=max(prices[ind]+ahead[1], 0+ahead[0])

                curr[buy]=profit
            ahead=curr
        
        print(ahead[1])
        return ahead[1]

obj=Solution()
obj.maxProfit(prices = [1,2,3,0,2])
obj.maxProfit([1])
