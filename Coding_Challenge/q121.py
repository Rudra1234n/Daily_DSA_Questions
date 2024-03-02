class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
        row, col = len(grid), len(grid[0])
        vis = set()
        queue = []
        fresh = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh +=1
                    
         
        #case all boxes have zeroes.
        if not queue:
            return 0
            
        time = 0
        direction = [(1,0), (-1, 0), (0,-1), (0,1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
               r, c = queue.pop(0)
               
               for i, j in direction:
                   newr, newc = r+i, c+j
                   if newr >= 0 and newr < row and newc >= 0 and newc < col and grid[newr][newc] == 1:
                       queue.append((newr, newc))
                       grid[newr][newc] = 2
                       fresh -=1
                       
            time+=1
                       

        if fresh > 0: return -1            
        return time
