class Solution:
    def numberOfPaths (self, m, n):
        MOD = (10 ** 9)+ 7
        path = 1
        for i in range(n, (m + n - 1)):
            path = (i * path) % MOD
            inv = pow(i -n + 1, MOD - 2, MOD)
            path = path * inv
     
        return path % MOD
