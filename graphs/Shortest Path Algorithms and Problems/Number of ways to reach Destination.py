from queue import PriorityQueue
from typing import List
from collections import defaultdict
import sys
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adjL=[[] for i in range(n)]
        for i in roads:
            adjL[i[0]].append((i[1],i[2]))

        pq=PriorityQueue()
        pq.put((0,0))     # dist,node

        ways=[0 for i in range(n)]
        dist=[sys.maxsize for i in range(n)]
        dist[0]=0
        print(adjL)
        while pq:
            query=pq.get()
            node=query[1]
            dis=query[0]

            for nn in adjL[node]:
                newNode=nn[0]
                newDis=nn[1]
                # if newNode==n-1 and newDis<=dist[newNode]:
                #     ways[newNode]= ways[node]+1
                if newDis+dis<dist[newNode]:
                    ways[newNode]+=1
                    # ways[newNode]=ways[node]
                    dist[newNode]=newDis+dis
                    pq.put((newDis+dis,newNode))
                elif newDis+dis==dist[newNode]:
                    ways[newNode]+=ways[node]
        print(ways)
        return ways

        

obj=Solution()
print(obj.countPaths(7,[[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
print(obj.countPaths(6,[[0,5,8],[0,2,2],[0,1,1],[1,3,3],[1,2,3],[2,5,6],[3,4,2],[4,5,2]]))