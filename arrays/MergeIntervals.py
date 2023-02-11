from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ds=[]
        fianl_ans=[]
        n=len(intervals)
        return self.sol(ds,fianl_ans,n,intervals)
    def sol(self,ds,final_ans,n,arr):
        ds.append(list(arr[0]))
        # for i in range(1,n):
        i=1
        while i < n:
            if arr[i][0]<=ds[-1][1]:
                ds[-1][0]=ds[-1][0]
                ds[-1][1]=max(ds[-1][1],arr[i][1])
                final_ans.append(list(ds[-1]))

                print(ds[-1])
                i+=1
            else:
                # ds=[]
                ds.append(list(arr[i]))
                
        print(final_ans)
        print(ds)
        return ds

obj=Solution()
intervals = [[1,4],[5,6]]
obj.merge(intervals)