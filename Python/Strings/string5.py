class Solution:
    def longestPalin(self, S):
        ans = S[0]
        for i in range(len(S)):
            j = i+len(ans)+1
            while j<len(S)+1:
                p = S[i:j]
                if p == p[::-1]:
                    ans = p
                j += 1
        return ans
