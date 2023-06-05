from typing import *
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans=[]
        for i in range(numRows):
            mini_ans=self.rowSol(i+1)
            ans.append(mini_ans)
        
        return ans


    def rowSol(self,r):
        final=[1]
        ans=1
        for i in range(1,r):
            ans=ans*(r-i)
            ans=ans//i
            final.append(ans)
        return final

obj=Solution()
ans=obj.generate(6)
print(ans)
