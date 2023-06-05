from typing import *
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        ans=0
        prefixSum=0
        # for num in nums:
        #     sum+=num
        #     diff= sum-k
        #     if diff in hashmap:
        #         ans+=hashmap[diff]
        #     hashmap[sum]=1+hashmap.get(sum,0)
        # return ans
        cnt=0
        for i in range(len(nums)):
            prefixSum+=nums[i]
            diff_Xminusk=prefixSum-k
            if diff_Xminusk in hashmap:
                cnt+=hashmap[diff_Xminusk]
            hashmap[prefixSum]=1+hashmap.get(prefixSum,0)
        print(cnt)
        return cnt


    
obj=Solution()
obj.subarraySum(nums = [1,1,1], k = 2)
obj.subarraySum(nums = [1,2,3], k = 3)