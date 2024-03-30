class Solution:

    def shortestDistance(self, rows, cols, grid, target_row, target_col):
        if grid[0][0] == 0 or grid[target_row][target_col] == 0:
            return -1
        path_length, queue, neighbors = 0, [[0, 0]], [[0, -1], [-1, 0], [1, 0], [0, 1]]

        while queue:
            next_queue = []
            for row, col in queue:
                if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                    continue
                if row == target_row and col == target_col:
                    return path_length
                grid[row][col] = 0
                next_queue.extend([[row, col - 1], [row - 1, col], [row + 1, col], [row, col + 1]])
            queue, path_length = next_queue, path_length + 1
        return -1
