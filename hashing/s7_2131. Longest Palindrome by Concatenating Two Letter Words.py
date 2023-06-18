from collections import *
from typing import *
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        c=Counter(words)

        cnt=0
        flag=False
        for i in range(len(words)):
            rword=words[i][::-1]
            original_word=words[i]
            if rword != original_word :
                if rword in c:
                    var=min(c[rword],c[original_word])
                    cnt+=var*4
                    del c[original_word]
                    del c[rword]
            elif rword==original_word:
                sub_cnt=c[rword]
                if sub_cnt%2==0:
                    cnt+=2*sub_cnt
                else:
                    if flag==False:
                        cnt+=2*sub_cnt
                        flag =True
                    else:
                        cnt+=(sub_cnt-1)*2
                del c[rword]
        
        return cnt
    
obj=Solution()
print(obj.longestPalindrome(words = ["lc","cl","gg"]))
print(obj.longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))
print(obj.longestPalindrome( words = ["cc","ll","xx"]))