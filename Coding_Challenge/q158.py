import heapq

class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        # using prim's algorithm
        vis=[0]*V
        count=0
        heap=[]
        heapq.heappush(heap,(0,0))
        while heap:
            value=heapq.heappop(heap)
            wt=value[0]
            node=value[1]
            if vis[node]==1:
                continue
            vis[node]=1
            count+=wt
            for i in adj[node]:
                adjnode=i[0]
                weight=i[1]
                if vis[adjnode]!=1:
                    heapq.heappush(heap,(weight, adjnode))
        return count
