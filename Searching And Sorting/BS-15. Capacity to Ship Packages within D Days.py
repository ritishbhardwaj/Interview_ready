from typing import *
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low,high=max(weights),sum(weights)
        ans=high

        while low<=high:
            mid=(low+high)//2   #mid is reflecting the capacity of ship that we are assuming

            #ab hum calculate karenge the number of days required to carry all the weights with this capacity
            number_of_days=self.ans(weights,mid)

            if number_of_days <= days:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans,low
        
    def ans(self,arr:List[int],capacity):
        days=1
        load=0
        
        #traversing the array
        for i in range(len(arr)):
            
            if load+arr[i] > capacity:
                days+=1
                load=arr[i]
            else:
                load+=arr[i]

        return days

obj=Solution()
print(obj.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5))
print(obj.shipWithinDays(weights = [1,2,3,1,1], days = 4))
print(obj.shipWithinDays(weights = [3,2,2,4,1,4], days = 3))