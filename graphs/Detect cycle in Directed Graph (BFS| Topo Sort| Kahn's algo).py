class Solution:    
    def isCyclic(self, V, adj):
        indegree=[0 for i in range(V)]

        for i in adj:
            for j in i:
                indegree[j]+=1
        
        print(indegree)
        q=[]
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        print(q)
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
        if len(ordering)<V:
            return True
        return False




obj=Solution()
V,E=4 ,4
adjL=[[1],[2],[3],[3]]
print(obj.isCyclic(V,adjL))

