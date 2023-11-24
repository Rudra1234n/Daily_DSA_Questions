
from typing import List
from queue import Queue
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        result = []  # List to store the BFS traversal
        visited = [False] * V
        queue = Queue()

        # Starting BFS from all unvisited vertices
        for i in range(V):
            if not visited[i]:
                self.solve(adj, visited, i, queue, result)

        return result

    def solve(self, adj, visited, vertex, queue, result):
        queue.put(vertex)
        visited[vertex] = True

        while not queue.empty():
            front = queue.get()
            result.append(front)

            for neighbor in adj[front]:
                if not visited[neighbor]:
                    queue.put(neighbor)
                    visited[neighbor] = True