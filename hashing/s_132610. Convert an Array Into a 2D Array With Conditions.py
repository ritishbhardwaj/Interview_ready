from typing import *
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        n = len(nums)
        for i in range(n):
            ins = False
            for j in range(len(ans)):
                ch = False
                for k in range(len(ans[j])):
                    if ans[j][k] == nums[i]:
                        ch = True
                if not ch:
                    ans[j].append(nums[i])
                    ins = True
                    break
            if not ins:
                ans.append([nums[i]])
        return ans
    
obj=Solution()
print(obj.findMatrix(nums = [1,3,4,1,2,3,1]))
print(obj.findMatrix(nums = [1,2,3,4]))