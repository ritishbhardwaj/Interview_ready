from collections import defaultdict
class Solution:
    def countSubarray(self, N, A, L, R):

        m=defaultdict()
        for i in range(L,R+1):
            m[i]=1
        print(m)

        

obj=Solution()
obj.countSubarray(N = 3, L = 3, R = 8,A = [1, 4, 6])
obj.countSubarray(N = 4, L = 4, R = 13,A = [2, 3, 5, 8])