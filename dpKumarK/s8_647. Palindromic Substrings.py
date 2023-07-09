from typing import *

class Solution:
    def countSubstrings(self, s: str) -> int:

        cnt=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                # print(s[i:j])
                if s[i:j]==s[i:j][::-1]:
                    cnt+=1
        
        return cnt
            
obj=Solution()
cases=["aaa","abc","aaabcc"]
for c in cases:
    # print(obj.countSubstrings("aaabcc"))
    print(obj.countSubstrings(c))