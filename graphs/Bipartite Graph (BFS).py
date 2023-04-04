from typing import *
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        m=len(graph[0])
        color=[-1 for i in range(n)]

        for i in range(n):
            if color[i]==-1:
                if self.check(graph,color,i)==False:
                    return False
        return True
    
    def check(self,grid,color,start):
        q=[]
        q.append(start)  #0th node append karva dii
        color[start]=0
        while q:
            node=q.pop(0)

            for n in grid[node]:
                #if the adjacent node is not yet colored 
                # color it with another color
                if color[n]==-1:
                    color[n]= not color[node]
                    q.append(n)
                elif color[n]==color[node]:
                    return False
        
        return True


obj=Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(obj.isBipartite(graph))
graph = [[1,3],[0,2],[1,3],[0,2]]
print(obj.isBipartite(graph))