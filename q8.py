from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        def adjList_to_adjMap(adj, V):
            adj_map = {}
            for i in range(V):
                adj_map[i] = adj[i]
            return adj_map

        adj_map = adjList_to_adjMap(adj, V)
        parent = {}  # to keep track of previous nodes/vertices
        q = []  # list of tuples to keep node and parent
        visited = set()  # to keep track of visited nodes

        for start_node in adj_map:
            if start_node not in visited:
                q.append((start_node, None))
                visited.add(start_node)
                while q:
                    node, par = q.pop(0)
                    parent[node] = par
                    for neighbor in adj_map[node]:
                        if neighbor not in visited:
                            q.append((neighbor, node))  # Set the parent to the current node
                            visited.add(neighbor)
                        elif parent[node] != neighbor:
                            return True  # There is a cycle

        return False