from typing import *
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v=len(graph)
        vis=[0 for i in range(v)]
        pathvis=[0 for i in range(v)]
        check=[0 for i in range(v)]
        safeStates=[]

        def dfsCheck(node,mat,vis,pathvis,check):
            vis[node]=1
            pathvis[node]=1
            check[node]=0

            for n in mat[node]:
                if pathvis[n]==1 and vis[n]==1:
                    return True
                elif vis[n]==0:
                    if dfsCheck(n,mat,vis,pathvis,check)==True:
                        return True
            
            check[node]=1
            pathvis[node]=0
            return False

        for i in range(v):
            if vis[i]==0:
                node=i
                dfsCheck(node,graph,vis,pathvis,check)

        for i in range(len(check)):
            if check[i]==1:
                safeStates.append(i)
        
        return safeStates

obj=Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(obj.eventualSafeNodes(graph))
graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
print(obj.eventualSafeNodes(graph))