from typing import *

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n=len(prices)

        #====MEMOIZATION ======

        def sol(ind,buy,cap,prices,dp,n):
            
            if cap==0:
                return 0
            if ind==n:
                return 0
            if dp[ind][buy][cap]!=-1 :
                return dp[ind][buy][cap]
            
            if buy :
                profit=max(-prices[ind]+sol(ind+1,0,cap,prices,dp,n),
                            sol(ind+1,1,cap,prices,dp,n))
            else:
                profit=max(prices[ind]+sol(ind+1,1,cap-1,prices,dp,n),
                            sol(ind+1,0,cap,prices,dp,n))

            dp[ind][buy][cap]=profit

            return profit

        # dp=[[[-1 for i in range(k+1)] for j in range(2)] for k in range(n+1)]
        # ans=sol(0,1,2,prices,dp,n)
        # print(ans)
        # return ans

        #========= TABULATION ===============
        dp=[[[0 for i in range(k+1)] for j in range(2)] for m in range(n+1)]
        for ind in range(n+1):
            for buy in range(2):
                dp[ind][buy][0]=0
        
        for buy in range(2):
            for cap in range(k+1):
                dp[n][buy][cap]=0
        
        for ind in range(n-1,-1,-1):
            for buy in range(2):    # in tabulation the buy would be 0|1 bcoz in recursion it was 1->0
                for cap in range(1,k+1):
                    if buy :
                        profit=max(-prices[ind]+dp[ind+1][0][cap],
                                    0+dp[ind+1][1][cap])
                    else:
                        profit=max(prices[ind]+dp[ind+1][1][cap-1],
                                    0+dp[ind+1][0][cap])

                    dp[ind][buy][cap]=profit

                    # return profit
        print(dp[0][1][k])
        # return (dp[0][1][2])

        #=========== SPACE OPTIMIZATION=======
        after=[[0 for i in range(k+1)] for j in range(2)]
        curr=[[0 for i in range(k+1)] for j in range(2)]
        for ind in range(n-1,-1,-1):
            for buy in range(2):    # in tabulation the buy would be 0|1 bcoz in recursion it was 1->0
                for cap in range(1,k+1):
                    if buy :
                        profit=max(-prices[ind]+after[0][cap],
                                    0+after[1][cap])
                    else:
                        profit=max(prices[ind]+after[1][cap-1],
                                    0+after[0][cap])

                    curr[buy][cap]=profit
            after=curr
                    # return profit
        print(curr[1][k])
        print('break')
        return (curr[1][k])


obj=Solution()
obj.maxProfit(k = 2, prices = [2,4,1])
obj.maxProfit(k = 2, prices = [3,2,6,5,0,3])
