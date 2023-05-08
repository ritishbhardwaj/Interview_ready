from typing import *
# class Solution:
#     def rearrangeArray(self, nums: List[int]) -> List[int]:
#         ans=[0 for i in range(len(nums))]
#         pos=0
#         neg=1
#         for i in range(len(nums)):
#             if nums[i]<0:
#                 ans[neg]=nums[i]
#                 neg+=2
#             else:
#                 ans[pos]=nums[i]
#                 pos+=2
#         print(ans)
#         return ans

'''VAriety II'''
class Solution:
    def rearrange(self,arr, n=0):
        # code 0here
        ans=[]
        posi=[]
        negi=[]
        for i in range(len(arr)):
            if arr[i]>=0:
                posi.append(arr[i])
            else:
                negi.append(arr[i])
        l=len(posi) if len(posi)<len(negi) else len(negi) if len(posi)>len(negi) else len(arr)
        flag=0
        for i in range(l):
            if flag==0:
                ans.append(posi[i])
                flag=1
            else:
                ans.append(negi[i])
                flag=0
        for i in range(len(ans)):
            arr[i]=ans[i]

        print(posi)
        print(negi)
        print(ans)
        print()

obj=Solution()
obj.rearrange([3,1,-2,-5,2,-4])
obj.rearrange( [-1,1])
obj.rearrange([-5 ,-2 ,5 ,2 ,4 ,7 ,1 ,8 ,0 ,-8])
