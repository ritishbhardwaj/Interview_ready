from typing import *
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        ele={}
        for i in range(n):
            for j in range(m):
                ele[mat[i][j]]=(i,j)
        
        r={}
        c={}
        for i in range(len(arr)):
            if arr[i] in ele:
                row,col=ele[arr[i]]
                if row in r:
                    r[row]+=1
                else:
                    r[row]=1
                if r[row]==m:
                    return i
                if col in c:
                    c[col]+=1
                else:
                    c[col]=1
                if c[col]==n:
                    return i
            # if m in r.values() or n in c.values():
            #     return i
        


obj=Solution()
print(obj.firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))
print(obj.firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))