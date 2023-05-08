import sys
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        ans=[A[-1]]
        maxi=A[-1]
        
        for i in range(len(A)-2,0-1,-1):
            if A[i]>=maxi:
                ans.append(A[i])
                maxi=A[i]
        return ans[::-1]
    
obj=Solution()
print(obj.leaders([16,17,4,3,5,2,0],7))