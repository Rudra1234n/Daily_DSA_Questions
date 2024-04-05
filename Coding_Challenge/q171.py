class Solution:
    def total_cost(self, cost):
        n = len(cost)
        if n == 1:
            return 0
        
        dp = [[float('inf')] * n for _ in range(1 << n)]
        dp[1][0] = 0
        
        for mask in range(1 << n):
            for u in range(n):
                if not (mask & (1 << u)):
                    continue
                for v in range(n):
                    if mask & (1 << v) or u == v:
                        continue
                    dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + cost[u][v])
        
        min_cost = float('inf')
        for i in range(1, n):
            min_cost = min(min_cost, dp[(1 << n) - 1][i] + cost[i][0])
        
        return min_cost
