class DisjointSet_:

    def __init__(self,n) -> None:
        self.rank=[0 for i in range(n+1)]
        self.parent=[int(i) for i in range(n+1)]
        self.size=[int(i) for i in range(n+1)]

    # Path Compression
    def findUPair(self,node):
        if node==self.parent[node]:
            return node
        self.parent[node]=self.findUPair(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u,v):
        ulp_u=self.findUPair(u)     # ultimate parent of u ko dhundo
        ulp_v=self.findUPair(v)     # ultimate parent of v ko dhundo

        if ulp_u==ulp_v:   # agar ultimate parent of u and v same hai toh iska matlab hai ki u and v belongs to the same 
             return               #component hence present in same graph, so no need to do anything and just return
        
        
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.parent[ulp_u]=ulp_v
        elif self.rank[ulp_v]<self.rank[ulp_u]:
            self.parent[ulp_v]=ulp_u
        else:
            self.parent[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
    
    def unionBySize(self,u,v):
        ulp_u=self.findUPair(u)
        ulp_v=self.findUPair(v)

        if ulp_u==ulp_v:
            return
        
        if self.size[ulp_u]<self.size[ulp_v]:
            self.parent[ulp_u]=ulp_v
            self.size[ulp_v]+=self.size[ulp_u]
        else:
            self.parent[ulp_v]=ulp_u
            self.size[ulp_u]+=self.size[ulp_v]
        

        

obj=DisjointSet_(7)
obj.unionByRank(1,2)
obj.unionByRank(2,3)
obj.unionByRank(4,5)
obj.unionByRank(6,7)
obj.unionByRank(5,6)
if obj.findUPair(3)==obj.findUPair(7):
    print("same")
else:
    print("notSame")
obj.unionByRank(3,7)
if obj.findUPair(3)==obj.findUPair(7):
    print("same")
else:
    print("notSame")

print()

obj=DisjointSet_(7)
obj.unionBySize(1,2)
obj.unionBySize(2,3)
obj.unionBySize(4,5)
obj.unionBySize(6,7)
obj.unionBySize(5,6)
if obj.findUPair(3)==obj.findUPair(7):
    print("same")
else:
    print("notSame")
obj.unionBySize(3,7)
if obj.findUPair(3)==obj.findUPair(7):
    print("same")
else:
    print("notSame")