from Lib import *

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.countPartitions(len(nums),target,nums)


    def countPartitions(self, n, d, arr):
            s=sum(arr)
            if s-d<0 or (s-d)%2!=0: return 0
            k= (s-d)//2        #k is denoted as target 
            prev=[0 for i in range(k+1)]
            curr=[0 for i in range(k+1)]
            if arr[0]==0 : 
                prev[0]=2
            else:
                prev[0]=1
            if arr[0]<=k and arr[0]!=0:
                prev[arr[0]]=1
            for ind in range(1,n):
                for target in range(k+1):
                    not_taken=prev[target]
                    taken =0
                    if arr[ind]<=target:
                        taken=prev[target-arr[ind]] 
                    curr[target]=taken +not_taken
                prev=curr[:]    
                    
            return prev[k]