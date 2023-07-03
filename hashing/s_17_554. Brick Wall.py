
from typing import *
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cr={}   #  {cracks : appearence in number of rows}
        
        for i in range(len(wall)):
            wall[i]=tuple(wall[i])
        
        if len(set(wall))==1:
            return len(wall)
            
        length_of_full_wall=sum(wall[0])
        for i in range(len(wall)):
            s=0
            for j in range(len(wall[i])):
                s+=wall[i][j]
                if s==length_of_full_wall:
                    continue
                if s in cr:
                    cr[s]+=1
                else:
                    cr[s]=1
        
        # mx=sorted(cr.values())[]
        mx=max(cr.values())
        return len(wall)-mx

obj=Solution()
print(obj.leastBricks(wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
print(obj.leastBricks(wall = [[1],[1],[1]]))



st=['cba','abc']
print(sorted(st))
st=["matter","cat"]
print(sorted(st))

val=chr(97)
print(val)