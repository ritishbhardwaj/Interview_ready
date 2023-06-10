from typing import *
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        intervals.sort()
        ans=[]

        for i in range(len(intervals)):

            if ans==[] or intervals[i][0]>ans[-1][1] :
                ans.append(intervals[i])
            
            else:
                ans[-1][1]=max(ans[-1][1],intervals[i][1])
        
        return ans
    

obj=Solution()
print(obj.merge(intervals = [[1,3],[2,6],[8,10],[15,18]]))