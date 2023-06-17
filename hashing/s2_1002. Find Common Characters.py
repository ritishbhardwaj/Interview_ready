from collections import Counter
from typing import *
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq={}
        for i in range(ord("a"),ord("z")+1):
            min_freq[chr(i)]=1000
        
        for i in range(len(words)):
            c=Counter(words[i])
            for j in range(ord("a"),ord("z")+1):
                if chr(j) in min_freq and (chr(j) not in c):
                    min_freq[chr(j)]=0
                else:
                    min_freq[chr(j)]=min(min_freq[chr(j)],c[chr(j)])
        
        # print(min_freq)
        ans=""
        for k,v in min_freq.items():
            if v!=0:
                temp=k*v
                ans+=temp
        ans=list(ans)
        # print(ans)
        return ans



obj=Solution()
obj.commonChars(words = ["bella","label","roller"])
obj.commonChars(words = ["cool","lock","cook"])