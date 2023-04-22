from queue import PriorityQueue
from typing import List
from sys import maxsize as maxx
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        
        # mini=maxx
        # def sol(ind,target,arr,src):
        #     if src==target:
        #         return 1    
        #     if src>100000:
        #         src=src%(100000)
            
        #     if ind==len(arr)-1:
        #         if src*arr[ind]==end:
        #             return 1
        #         return 0

        #     not_take=sol(ind+1,target,arr,src)
        #     take=sol(ind,target,arr,src*arr[ind])

        #     return min(mini,take+not_take)

        # ans=sol(0,end,arr,start)
        # return ans

        pq=PriorityQueue()
        cost=[maxx for i in range(100000+1)]

        pq.put((start,0))   #(node, steps)
        cost[start]=0

        while pq:
            query=pq.get()
            node=query[0]
            st=query[1]

            num=node
            for i in range(len(arr)):
                new_num=num*arr[i]
                if new_num>100000:
                    new_num%=100000
                if st+1<cost[new_num]:
                    cost[new_num]=st+1
                    if new_num==end:
                        return st+1
                    pq.put((new_num,st+1))
        return -1




obj=Solution()
print(obj.minimumMultiplications(arr=[2, 5, 7],start = 3, end = 30))
print(obj.minimumMultiplications(arr = [3, 4, 65],start = 7, end = 66175))