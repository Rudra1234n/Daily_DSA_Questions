from heapq import *
class Solution:
    def dijkstra(self, V, adj, S):
        heap=[]
        heappush(heap,[0,S])
        vis=[float("inf")]*V
        vis[S]=0
        while heap:
            a=heappop(heap)
            dis=a[0]
            node=a[1]
            for i in adj[node]:
                d=i[1]
                n=i[0]
                if dis+d<vis[n]:
                    vis[n]=d+dis
                    heappush(heap,[vis[n],n])
        return vis
                
