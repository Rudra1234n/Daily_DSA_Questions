class Solution:
    def CountWays(self, s):
        mod = 10**9 + 7
        dp = [-1] * (len(s) + 1)
        
        def decode(pos):
            n = len(s)
            if pos == n:
                return 1
            if s[pos] == '0':
                return 0
            if dp[pos] != -1:
                return dp[pos]
            
            count = decode(pos + 1) % mod
            if pos < n - 1 and int(s[pos:pos+2]) <= 26:
                count = (count + decode(pos + 2)) % mod
            
            dp[pos] = count
            return dp[pos] % mod
        
        return decode(0)
