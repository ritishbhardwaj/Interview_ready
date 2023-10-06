from typing  import *
from collections import Counter 

class Solution:
    def largestVariance(self, s):
        
        li=[]
        maxi=0
        def sol(ind,prev,string:str,dp):
            nonlocal li,maxi
            # if dp[ind][prev]!=-1:
            #     return
            if ind==len(string):
                if ind==prev:
                    return 
                else:
                    ss=string[prev:ind]
                    if ss!='':
                        li.append(ss)
                        c=Counter(ss)
                        val=sorted(c.values())
                        # print(val)
                        if len(val)>1:
                            v=val[-1]-val[0]
                            maxi=max(maxi,v)
                            li.append(ss)
                    # print(ss)
                    return


            if dp[ind][prev]!=-1:
                return
            
            ss=string[prev:ind]
            if ss!='':
                li.append(ss)
                c=Counter(ss)
                val=sorted(c.values())
                # print(val)
                if len(val)>1:
                    v=val[-1]-val[0]
                    maxi=max(maxi,v)

            take=sol(ind+1,prev,string,dp)
            nottake=sol(ind+1,ind+1,string,dp)
            dp[ind][prev]=1
            return 
        
        dp=[[-1 for i in range(len(s)+1)] for j in range(len(s)+1)]
        ans=sol(0,0,s,dp)
        # print(len(li))
        return maxi

        dp=[[0 for i in range(len(s)+1)] for j in range(len(s)+1)]


        for ind in range(len(s)-1,-1,-1):
            for prev in range(len(s)-1,-1,-1):
                pass
            
        
obj=Solution()
print(obj.largestVariance("abba"))
print(obj.largestVariance( "aababbb"))
print(obj.largestVariance( "abcde"))
print(obj.largestVariance('abcabcabccd'))
print(obj.largestVariance("eclxprpsikqrrejlmrssdmyutotguuxnftfwzlidgesnhtqdtmhkdhmqfltxcsctrgdjmmkboazjwfgdpiiqoacvrhhxbbqspfnkvhjztompwicltxoyssjhuiuamqpdrhvcetfmczldpozxebprmpwtcpcunmtiomzgwwylonkonomlgasxhbssjohlatvpjkuoighojbdepxtpfqudbjmjugggyiggvoascelgoknsjqnltxlicopzlkfyqgaejmugariqpnuymkskoazesdbjhdhgapmglcqcyglcqnbndbepfavzssgkxsxfwl"))
