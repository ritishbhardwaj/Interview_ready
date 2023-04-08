from typing import *
class Solution:
    def findOrder(self,dit, N, K):
        ascii=97
        english_order1=dict()
        english_order2=dict()
        for i in range(K):
            english_order1[chr(ascii)]=i
            english_order2[i]=chr(ascii)
            ascii+=1
        
        adjL=[[] for i in range(K)]
        # print(adjL)
        for i in range(N-1):
            s1=dit[i]
            s2=dit[i+1]
            l=min(len(s1),len(s2))
            for j in range(l):
                if s1[j]==s2[j]:
                    continue
                else:
                    adjL[english_order1[s1[j]]].append(english_order1[s2[j]])
                    break
        # print(english_order)
        # print(adjL)
        # Topo Sort begins here
        V=K
        q=[]
        indegree=[0 for i in range(V)]
        
        for i in range(V):
            for j in adjL[i]:
                indegree[j]+=1
        # print(indegree)
        ordering=[]
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            node=q.pop(0)
            if indegree[node]==0:
                ordering.append(english_order2[node])
            
            for n in adjL[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        
        # print(ordering)
        return ordering


obj=Solution()
N = 5
K = 4
dit = ["baa","abcd","abca","cab","cad"]
print(obj.findOrder(dit,N,K))