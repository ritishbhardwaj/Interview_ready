from typing import List
class Solution:
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:

        n=len(adj)
        m=len(adj[0])

        vis=[0 for j in range(n)]

        def dfs(node,parent,adj,vis):
            vis[node]=1
            for subnode in adj[node]:
                if vis[subnode]==0:
                    if dfs(subnode,node,adj,vis)==True:
                        return True
                elif subnode!=parent:
                    return True
            return False

        for i in range(V):
            if not vis[i]:
                if dfs(i,-1,adj,vis)==True:
                    return True
        return False    



obj=Solution()
V = 5
E = 5
adj = [[1], [0, 2, 4], [1, 3], [2 ,4], [1 ,3]]
ans=obj.isCycle(V,adj)
print(ans)
adj = [[1], [0, 2], [1, 3], [2 ,4], [3]]
ans=obj.isCycle(V,adj)
print(ans)