from typing import *
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def compare(s1,s2):
            if len(s1)!=len(s2)+1:
                return False
            
            first,sec=0,0
            while first<len(s1):
                if sec<len(s2) and s1[first]==s2[sec] :
                    first+=1
                    sec+=1
                else:
                    first+=1
            if first==len(s1) and sec==len(s2):
                return True
            else:
                return False
            
        words.sort(key=len)   # [1,2,4,7,8,14,16]
        dp=[1 for i in range(len(words))]

        maxi=1
        for ind in range(1,len(words)):
            for prev in range(0,ind):
                a=words[ind]
                b=words[prev]
                if compare(words[ind],words[prev]) and 1+dp[prev]>dp[ind]:
                    dp[ind]=dp[prev]+1
            
            if dp[ind]>maxi:
                maxi=dp[ind]
        print(maxi)
        return maxi

obj=Solution()
obj.longestStrChain(words = ["a","b","ba","bca","bda","bdca"])
obj.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"])
obj.longestStrChain(["a","ab","ac","bd","abc","abd","abdd"])