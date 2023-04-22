'''this is the implementation of floydd warshall algorithm'''

from sys import maxsize as maxx
from typing import *
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        dist=[[maxx for i in range(n)] for j in range(n)]

        for i in edges:
            dist[i[0]][i[1]]=i[2]
            dist[i[1]][i[0]]=i[2]

        for i in range(n):
            dist[i][i]=0

        print(dist)
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via]==maxx or dist[via][i]==maxx:
                        continue
                    dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
        
        print(dist)

        cntCity=n
        cityNo=-1
        for city in range(n):
            cnt=0
            for adjcity in range(n):
                if dist[city][adjcity]<=distanceThreshold:
                    cnt+=1
            
            if cnt<=cntCity:
                cntCity=cnt
                cityNo=city
        
        return cityNo

obj=Solution()
print(obj.findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4))
print(obj.findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2))