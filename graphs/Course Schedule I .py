from typing import *
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(numCourses)]
        for i in prerequisites:
            adj[i[0]].append(i[1])

        V=numCourses
        indegree=[0 for u in range(V)]
        q=[]
        for i in adj:
            for j in i:
                indegree[j]+=1
        print(indegree)
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        ordering=[]
        while q:
            node=q.pop(0)
            if indegree[node]==0:
                ordering.append(node)
            
            for n in adj[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)

        print(ordering)

        return len(ordering)==V


obj=Solution()
numCourses = 2
prerequisites = [[1,0]]
# prerequisites=[[1, 0],
#                  [2, 0],
#                  [3, 1],
#                  [3, 2]]
print(obj.canFinish(numCourses,prerequisites))