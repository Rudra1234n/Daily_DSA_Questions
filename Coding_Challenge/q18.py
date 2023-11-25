from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        paths=deque()
        visited=[False]*len(adj)
        q=deque()
        q.append(0)
        visited[0]=True
        
        while (len(q)>0):
            src=q.popleft()
            paths.append(src)
            
            for i in adj[src]:
                if visited[i]==False:
                    q.append(i)
                    visited[i]=True
        
        return paths