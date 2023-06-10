from collections import Counter
from sys import maxsize

#=================== MY SOLUTION =============
class Solution:
    def removeFrequencies(self,s,t):
    
        for ch in t:
            if ch not in s:
                print(0)
                break
        else:
            count=0
            n_s=dict(Counter(s))
            new_set_s=list(n_s.items())
            new_set_s.sort(key=lambda x:x[1])
            for k,v in new_set_s:
                if k in t:
                    count+=v
                    break
            print(count)

obj=Solution()
obj.removeFrequencies("mononom","mon")
obj.removeFrequencies("aabbcza","abcd")
obj.removeFrequencies("aaab","ccc")
obj.removeFrequencies("abacbc","bca")
obj.removeFrequencies("abdadccacd","edac")

print()
#========== CLASS KA SOLUTION ===================

class Solution:
    def removeFrequencies(self,s,t):

        freq_s=dict(Counter(s))
        freq_t=dict(Counter(t))

        ans=maxsize
        countert = Counter(t)
        counters = Counter(s).most_common()
        print(counters,"=================")
        counters=Counter(s)

        q=counters["m"]
        # q1=freq_s["m"]
        for k in countert:
            first=counters[k]
            sec=countert[k]
            ans=min(ans,counters[k]//countert[k])
        
        print(ans)
        return min(counters[k]//countert[k] for k in countert)


obj=Solution()
# print(obj.removeFrequencies("mononom","mon"))
print(obj.removeFrequencies("aabbcza","abcd"))
print(obj.removeFrequencies("aaab","ccc"))
print(obj.removeFrequencies("abacbc","bca"))
print(obj.removeFrequencies("abdadccacd","edac"))


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

s="abcd"
st=set(s)
print("st== ",st)
lst=list(s)
print(lst)
a=list("ansb")
print(a)