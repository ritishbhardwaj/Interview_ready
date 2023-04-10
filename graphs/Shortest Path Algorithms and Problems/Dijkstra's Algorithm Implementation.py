from sys import maxsize as maxx
from queue import PriorityQueue 
class Solution:
    def dijkstra(self, V, adj, S):
        pq=PriorityQueue()
        dist=[maxx for i in range(V)]

        dist[S]=0
        pq.put(item=(0,S))
        
        while not pq.empty():
            query=pq.get()
            dis=query[0]
            node=query[1]

            for n in adj[node]:
                nnode=n[0]
                ndis=n[1]
                if dist[nnode]>dis+ndis:
                    dist[nnode]=ndis+dis
                    pq.put((dist[nnode],nnode))

        return dist

obj=Solution()
V = 3
E = 3
adj = [[[1, 1], [2, 6]], [[2, 3], [0, 1]], [[1, 3], [0, 6]]]
S = 2
print(obj.dijkstra(V,adj,S))
