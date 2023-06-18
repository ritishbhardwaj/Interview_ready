class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        map={0:-1}
        p=0
        l=0
        for i in range(len(arr)):
            
            p+=arr[i]
            diff=p-k
            if diff in map:
               l=max(l,i-map[diff])
            if p not in map:
                map[p]=i
        
        return l
            
print(Solution().lenOfLongSubarr([1,4,3,3,5,5],6,16))