#User function Template for python3

class Solution:
    
    #Function to find number of strongly connected components in the graph.
    def kosaraju(self, V, adj):
        
        vis=[0 for u in range(V)]
        __st=[]   # it is stack, top element represent the first node

        for i in range(V):
            if vis[i]==0:
                node=i
                self.dfs(node,vis,adj,__st)

        print(__st)
        #reversing the graph
        adjR=[[] for i in range(V)]
        for i in range(V):
            vis[i]=0
            for n in adj[i]:
                adjR[n].append(i)
        
        print(adjR)

        scc=0
        while __st:
            node=__st.pop()
            if vis[node]==0:
                scc+=1
                self.dfs3(node,vis,adjR)

        return scc
    
    def dfs(self,node,vis,adj,st:list):
        vis[node]=1

        for n in adj[node]:
            if vis[n]==0:
                self.dfs(n,vis,adj,st)

        st.append(node)
    
    def dfs3(self,node,vis,adj):
        vis[node]=1

        for n in adj[node]:
            if vis[n]==0:
                self.dfs3(n,vis,adj)


obj=Solution()
V=5
adj=[[2, 3], [0], [1], [4], []]
print(obj.kosaraju(V,adj))