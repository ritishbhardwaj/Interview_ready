from typing import *

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        adjL=[[] for i in range(n)]
        for i in range(len(edges)):
            adjL[edges[i][0]].append(edges[i][1])
            adjL[edges[i][1]].append(edges[i][0])
        print(adjL)

        dist=[float('inf') for i in range(n)]
        vis=[0 for i in range(n)]
        q=[]
        q.append(src)
        dist[src]=0
        vis[src]=1
        while q:
            node=q.pop(0)
            d=dist[node]

            for n in adjL[node]:
                
                if vis[n]==0:
                    dist[n]= min(dist[n],d+1)
                    vis[n]+=1
                    q.append(n)

        print(dist)
        return dist

obj=Solution()
#N= number nodes, M= number of edges 
print(obj.shortestPath(n = 9, m= 10,
edges=[[0,1],[0,3],[3,4],[4 ,5]
,[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
,src=0))