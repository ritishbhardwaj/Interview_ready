class Solution:

    def solve(self, A, B):
        
        hashmap={0:1}   # (frontXOR , its count)

        xr=0
        cnt=0
        for i in range(len(A)):
            xr^=A[i]
            x=xr^B

            if x in hashmap:
                cnt+=hashmap[x]
            
            if xr in hashmap:
                hashmap[xr]+=1
            if xr not in hashmap:
                hashmap[xr]=1
        
        print(cnt)
        return cnt
            


obj=Solution()
obj.solve(A = [4, 2, 2, 6, 4],B = 6)
obj.solve(A = [5, 6, 7, 8, 9],B = 5)

# print(4^6)