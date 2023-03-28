from typing import *
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n=len(isConnected)   # number of vertices
        m=len(isConnected[0])

        cnt=0
        vis=[0 for i in range(n)]
        adjls=[set() for j in range(n)]

        #creating adjancy list

        for i in range(n):
            for j in range(m):
                if isConnected[i][j]==1 and i!=j:
                    adjls[i].add(j)
                    adjls[j].add(i)
        print(adjls)

        def dfs(node):
            vis[node]=1
            for subnode in adjls[node]:
                if not vis[subnode]:
                    dfs(subnode)

        for i in range(n):
            if vis[i]==0:
                cnt+=1
                dfs(i)
        print(cnt)
        return  cnt


obj=Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
obj.findCircleNum(isConnected)