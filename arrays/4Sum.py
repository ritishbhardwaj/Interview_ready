from typing import *

#================BETTER SOLUTION=================
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        # nums.sort()
        ans=[]        
        for i in range(n):
            for j in range(i+1,n):
                Set=set()
                for k in range(j+1,n):
                    summ=nums[i]+nums[j]+nums[k]
                    fourth=target-summ
                    if fourth in Set:
                        sub=sorted([nums[i],nums[j],nums[k],fourth])
                        if sub not in ans:
                            ans.append(sub)
                    Set.add(nums[k])
        
        return ans
    
obj=Solution()
print(obj.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(obj.fourSum(nums = [2,2,2,2,2], target = 8))


#=============== OPTIMAL SOLUTION =============

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n=len(nums)
        nums.sort()
        ans=[]

        for i in range(n):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,n):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue

                k=j+1
                l=n-1

                while k<l:
                    summ=nums[i]+nums[j]+nums[k]+nums[l]
                    if summ==target:
                        sub=[nums[i],nums[j],nums[k],nums[l]]
                        ans.append(sub)
                        k+=1
                        l-=1
                        
                        while k<l and nums[k]==nums[k-1]:
                            k+=1
                        while k<l and nums[l]==nums[l+1]:
                            l-=1

                    elif summ<target:
                        k+=1
                    else:
                        l-=1
        return ans
    
obj=Solution()
print(obj.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
print(obj.fourSum(nums = [2,2,2,2,2], target = 8))