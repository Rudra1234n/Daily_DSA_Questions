class Solution():
    def maxCoins(self, N, a):
        y = [[0 for i in range(N + 2)] for j in range(N + 2)]
        a.insert(0, 1)
        a.append(1)
        for i in range(0, N - 1 + 1):
            for start in range(1, N - i + 1):
                end = start + i
                res = 0
                for k in range(start, end + 1):
                    temp = y[start][k - 1] + a[start - 1] * a[k] * a[end + 1] + y[k + 1][end]
                    res = max(res, temp)
                y[start][end] = res
        return y[1][N]
