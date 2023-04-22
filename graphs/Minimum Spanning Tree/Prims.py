from typing import *
from queue import PriorityQueue
#User function Template for python3

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        vis=[0 for u in range(V)]
        AdjL=[[] for i in range(V)]
        # for i in adj:
        #     AdjL[i[0]].append([i[1],i[2]])
        #     AdjL[i[1]].append([i[0],i[2]])
        AdjL=adj
        # print(AdjL)
        s=0
        pq=PriorityQueue()
        pq.put((0,0,-1))

        edgesRelation=[]
        # print(vis)
        while not pq.empty():
            query=pq.get()
            wt=query[0]  #weight of edge
            node=query[1]  
            parent=query[2]
            
            if vis[node]==1:
                continue

        
            s+=wt   #s is sum of weights
            vis[node]=1
            edgesRelation.append([node,parent])
            # print(vis)
            # print(s)
            
            for n in AdjL:
                newnode=n[0]
                newwt=n[1]
                if not vis[newnode]:
                    pq.put((newwt,newnode,node))
        
        return s



obj=Solution()
V=3 
E=3
adjL=[[0, 1, 5]
,[1, 2 ,3],
[0, 2 ,1]]
print(obj.spanningTree(V,adjL))

V=2
adjL=[[0, 1, 5]]
print(obj.spanningTree(V,adjL))