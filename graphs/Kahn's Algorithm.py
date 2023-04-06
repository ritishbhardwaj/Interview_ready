# Kahn's algo is topo sort but done in BFS manner

# we are assuming that there is a graph without any components

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        
        indegree=[0 for u in range(V)]
        q=[]
        for i in adj:
            for j in i:
                indegree[j]+=1
        print(indegree)
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        ordering=[]
        while q:
            node=q.pop(0)
            if indegree[node]==0:
                ordering.append(node)
            
            for n in adj[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)

        print(ordering)
        return ordering


    
obj=Solution()
print(obj.topoSort(4,[[],[0],[0],[0]]))