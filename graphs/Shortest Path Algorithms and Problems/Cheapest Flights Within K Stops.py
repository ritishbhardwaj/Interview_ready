from sys import maxsize as maxx
from queue import PriorityQueue
from typing import *
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        pq=PriorityQueue()
        
        adjL=[[] for i in range(n)]
        for i in flights:
            adjL[i[0]].append((i[1],i[2]))
        q=[(0,src,0)]
        pq.put((0,src,0))

        dist=[maxx for i in range(n)]
        dist[src]=0

        while q:
            query=q.pop(0)
            stop=query[0]
            node=query[1]
            cost=query[2]

            if stop>k:
                continue
        
            for n in adjL[node]:
                adjnode=n[0]
                edw=n[1]
                 
                if cost+edw <dist[adjnode] and stop<=k:
                    dist[adjnode]=cost+edw
                    q.append((stop+1,adjnode,cost+edw))


        if dist[dst]==maxx:
            return -1
        return dist[dst]

obj=Solution()
print(obj.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
print(obj.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
print(obj.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0))
