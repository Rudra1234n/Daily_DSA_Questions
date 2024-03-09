class Solution:
    def bfs(self,matrix,i,j,visited,n,m,corner,dx,dy) :
        q = []
        q.append([i,j])
        
        while q :
            temp = q.pop(0)
            
            for i in range(4) :
                x = temp[0] + dx[i]
                y = temp[1] + dy[i]
                
                
                if x >= 0 and y >= 0 and x < n and y < m and matrix[x][y] == 1 and visited[x][y] == False :
                    visited[x][y] = True
                    q.append([x,y])
                    if x == 0 or y ==0 or x == n-1 or y == m-1 :
                        corner[0] = True
    def closedIslands(self, matrix, N, M):
        visited = [[False for j in range(M)] for i in range(N)]
        dx = [-1,0,1,0]
        dy = [0,-1,0,1]
        corner = [False]
        for i in range(N) :
            for j in range(M) :
                if (i*j == 0 or i == N-1 or j == M-1) and matrix[i][j] == 1 and visited[i][j] == False :
                    self.bfs(matrix,i,j,visited,N,M,corner,dx,dy)
        res = 0
        for i in range(1,N-1) :
            for j in range(1,M-1) :
                if visited[i][j] == False and matrix[i][j] == 1 :
                    #corner = [False]
                    self.bfs(matrix,i,j,visited,N,M,corner,dx,dy)
                    res += 1
        return res
