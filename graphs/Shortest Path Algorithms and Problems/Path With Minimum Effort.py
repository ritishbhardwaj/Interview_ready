from queue import PriorityQueue
from sys import maxsize as maxx
from typing import *
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n=len(heights)
        m=len(heights[0])
        dist=[[maxx for i in range(m)] for j in range(n)]
        pq=PriorityQueue()
        pq.put((0,0,0))  #(0-> distance , [0,0] -> coordinates(row,col))
        dist[0][0]=0

        delrow=[-1,0,1,0]
        delcol=[0,-1,0,1]

        while pq:
            query=pq.get()
            row=query[1]
            col=query[2]
            diff=query[0]

            if row==n-1 and col==m-1:
                return diff

            for i in range(4):
                nr=row+delrow[i]
                nc=col+delcol[i]

                if nr>=0 and nr<n and nc>=0 and nc<m :
                    newEffort=max(diff,abs(heights[row][col]-heights[nr][nc]))
                    if newEffort<dist[nr][nc]:
                        dist[nr][nc]=newEffort
                        pq.put((newEffort,nr,nc))
        return 0

obj=Solution()
print(obj.minimumEffortPath(heights = [[1,2,2],[3,8,2],[5,3,5]]))
print(obj.minimumEffortPath(heights = [[1,2,3],[3,8,4],[5,3,5]]))
print(obj.minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))