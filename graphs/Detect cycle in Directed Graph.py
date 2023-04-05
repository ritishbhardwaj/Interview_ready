class Solution:    
    def isCyclic(self, V, adj):

        def dfs(node,mat,vis,pathvis):
            vis[node]=1
            pathvis[node]=1

            for n in mat[node]:
                if vis[n]==1 and pathvis[n]==1:
                    return True
                elif vis[n]==0 :
                    if dfs(n,mat,vis,pathvis)==True:
                        return True
            pathvis[node]=0
            return False

        vis=[0 for u in range(V+1)]
        pathvis=[0 for u in range(V+1)]
        for i in range(V):
            if vis[i]==0:
                if dfs(i,adj,vis,pathvis)==True:
                    return True
        return False


obj=Solution()
V,E=4 ,4
adjL=[[1],[2],[3],[3]]
print(obj.isCyclic(V,adjL))

V,E=3,2
adjL=[[1],[2]]
print(obj.isCyclic(V,adjL))