from typing import *
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        

        cnt=0
        ans=[]
        d={}
        for i in range(len(A)):
            if A[i]==B[i]:
                cnt+=1
            else:
                if A[i] in d:
                    cnt+=1
                if B[i] in d:
                    cnt+=1
                
            ans.append(cnt)
            d[A[i]]=1
            d[B[i]]=1

        return ans

print(Solution().findThePrefixCommonArray(A = [2,3,1], B = [3,1,2]))
print(Solution().findThePrefixCommonArray(A = [1,3,2,4], B = [3,1,2,4]))
print(Solution.findThePrefixCommonArray(Solution,A = [1,3,2,4], B = [3,1,2,4]))