from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr=prices[:]
        mini,profit=arr[0],0
        for i in range(1,len(prices)):
            cost=arr[i]-mini
            profit=max(cost,profit)
            mini=min(mini,arr[i])
        print(profit)
        return profit


obj=Solution()
print(obj.maxProfit(prices = [7,1,5,3,6,4]))
print(obj.maxProfit([7,6,4,3,1]))