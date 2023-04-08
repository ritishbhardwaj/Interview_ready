from typing import *
from sys import maxsize as maxx
class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adjL=[[] for i in range(n)]
        for i in range(len(edges)):
            adjL[edges[i][0]].append((edges[i][1],edges[i][2]))
        print(adjL)

        #TOPO sort
        stack=[]
        vis=[0 for i in range(n)]

        def dfs(node,st:List,vis):
            vis[node]=1
            for n in adjL[node]:
                if not vis[n[0]]:
                    dfs(n[0],st,vis)
            st.append(node)

        for i in range(n):
            if not vis[i]:
                dfs(i,stack,vis)
        
        print(stack,"this is stack so count from last index")

        dist=[maxx for i in range(n)]
        dist[stack[-1]]=0
        while stack:
            node=stack.pop()
            d=dist[node]
            for n in adjL[node]:
                n_node=n[0]
                n_d=n[1]
                if d+n_d < dist[n_node]:
                    dist[n_node]=d+n_d
        
        print(dist)
        return dist


obj=Solution()
n = 6
m= 7
edge=[[0,1,2],[0,4,1],[4,5,4]
,[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
print(obj.shortestPath(n,m,edge))


n=5 
m=5
edge=[[0, 1, 2,],
[2, 1, 2],
[2, 4, 2],
[1, 4, 8],
[1, 3, 6]]
print(obj.shortestPath(n,m,edge))