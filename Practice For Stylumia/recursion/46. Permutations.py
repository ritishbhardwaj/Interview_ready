from typing import *
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        final_ans=[]
        def sol(ind,freq,ds:List,arr):
            nonlocal final_ans

            if len(ds)==len(arr):
                final_ans.append(list(ds))
                return
            
            for i in range(len(arr)):
                if freq[i]==0:
                    ds.append(arr[i])
                    freq[i]=1
                    sol(ind+1,freq,ds,arr)
                    ds.pop()
                    freq[i]=0
        
        
        freq=[0 for i in range(len(nums))]
        sol(0,freq,[],nums)
        return final_ans


obj=Solution()
print(obj.permute([1,2,3]))
print(obj.permute([1,0]))