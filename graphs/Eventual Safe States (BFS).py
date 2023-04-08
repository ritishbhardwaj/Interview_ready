from typing import *
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        v=len(graph)
        adjR=[[] for i in range(v)]

        # reversing the edges
        for i in range(len(graph)):
            for j in graph[i]:
                adjR[j].append(i)
        
        for i in adjR:
            print(i)
        print(adjR)

        # Creation of Indegree
        indegree=[0 for i in range(v)]
        for i in adjR:
            for j in i:
                indegree[j]+=1

        q=[]
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        print(indegree)
        safeStates=[]
        while q:
            node=q.pop(0)
            if indegree[node]==0:
                safeStates.append(node)
            
            for n in adjR[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        
        safeStates.sort()
        return safeStates




obj=Solution()
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(obj.eventualSafeNodes(graph))