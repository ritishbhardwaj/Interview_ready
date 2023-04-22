from sys import maxsize as maxx
#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        
        dist=[maxx for i in range(V)]
        dist[S]=0
        for i in range(V-1):
            for j in edges:
                u=j[0]
                v=j[1]
                wt=j[2]
                
                if dist[u]!=maxx and dist[u]+wt<dist[v]:
                    dist[v]=dist[u]+wt
        for j in edges:
            u=j[0]
            v=j[1]
            wt=j[2]
            
            if dist[u]!=maxx and dist[u]+wt<dist[v]:
                return [-1]
        
        return dist
    
obj=Solution()
E = [[0,1,9]]
S = 0
print(obj.bellman_ford(2,E,S))
E = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
S = 2
print(obj.bellman_ford(3,E,S))

V=3

E=[[0 ,1, -1],
[1, 0, 3],
[1, 2, 4],
[2, 0, 3]]
S=0
print(obj.bellman_ford(V,E,S))

V=7
E=[[0 ,1 ,2]
,[0 ,2 ,-2]
,[0 ,3 ,-1]
,[0 ,4 ,-6]
,[0 ,6 ,2]
,[1 ,0 ,-2]
,[1 ,2 ,4]
,[1 ,4 ,-7]
,[1 ,6 ,10]
,[2 ,0 ,-8]
,[2 ,1 ,10]
,[2 ,6 ,-8]
,[3 ,1 ,-1]
,[3 ,4 ,4]
,[4 ,1 ,-11]
,[4 ,2 ,-10]
,[4 ,3 ,-4]
,[5 ,0 ,1]
,[5 ,2 ,8]
,[5, 3 ,-3]
,[5 ,4 ,3]
,[5 ,6, 6]
,[6 ,0 ,9]
,[6 ,1 ,1]
,[6, 3 ,-11]]
S=3
print(obj.bellman_ford(V,E,S))  