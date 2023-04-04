from typing import *
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n=len(graph)
        m=len(graph[0])
        color=[-1 for i in range(n)]

        def dfs(grid,color,start,c):
            color[start]=c
            for node in grid[start]:
                if color[node]==-1 :
                    dfs(grid,color,node,not c)
                        # return False
                elif color[node]==color[start]:
                    return False
            return True

        for i in range(n):
            if color[i]==-1:
                if dfs(graph,color,i,0)==False:
                    return False
        return True
    


obj=Solution()
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
print(obj.isBipartite(graph))
graph = [[1,3],[0,2],[1,3],[0,2]]
print(obj.isBipartite(graph))